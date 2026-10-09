from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from .models import Category, Product, StockTransaction
from .permissions import ADMIN, MANAGER, STAFF


class InventoryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        for name in (ADMIN, MANAGER, STAFF):
            Group.objects.create(name=name)
        for username, role in (("a", ADMIN), ("m", MANAGER), ("s", STAFF)):
            user = User.objects.create_user(username, password="pw12345!")
            user.groups.add(Group.objects.get(name=role))
        User.objects.create_user("norole", password="pw12345!")
        cat = Category.objects.create(name="Tools")
        cls.product = Product.objects.create(name="Hammer", sku="HAM-1", category=cat, unit_price=100, quantity=10, reorder_level=3)

    def login(self, username):
        self.client.login(username=username, password="pw12345!")

    # --- role-based access ---
    def test_anonymous_is_redirected_to_login(self):
        resp = self.client.get(reverse("product_list"))
        self.assertRedirects(resp, f"{reverse('login')}?next={reverse('product_list')}")

    def test_user_without_role_is_forbidden(self):
        self.login("norole")
        self.assertEqual(self.client.get(reverse("dashboard")).status_code, 403)

    def test_staff_can_view_but_not_manage(self):
        self.login("s")
        self.assertEqual(self.client.get(reverse("product_list")).status_code, 200)
        self.assertEqual(self.client.get(reverse("product_create")).status_code, 403)
        self.assertEqual(self.client.get(reverse("report")).status_code, 403)

    def test_manager_can_manage_but_not_delete(self):
        self.login("m")
        self.assertEqual(self.client.get(reverse("product_create")).status_code, 200)
        self.assertEqual(self.client.get(reverse("report")).status_code, 200)
        self.assertEqual(self.client.post(reverse("product_delete", args=[self.product.pk])).status_code, 403)

    def test_admin_can_delete_product_without_history(self):
        self.login("a")
        self.client.post(reverse("product_delete", args=[self.product.pk]))
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())

    # --- stock rules ---
    def test_stock_out_cannot_exceed_available(self):
        self.login("s")
        resp = self.client.post(reverse("stock_move"), {"product": self.product.pk, "movement_type": "OUT", "quantity": 11})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "only 10 in stock")
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity, 10)
        self.assertEqual(StockTransaction.objects.count(), 0)

    def test_stock_in_and_out_update_quantity_and_log_user(self):
        self.login("s")
        self.client.post(reverse("stock_move"), {"product": self.product.pk, "movement_type": "IN", "quantity": 5})
        self.client.post(reverse("stock_move"), {"product": self.product.pk, "movement_type": "OUT", "quantity": 12})
        self.product.refresh_from_db()
        self.assertEqual(self.product.quantity, 3)
        self.assertEqual(StockTransaction.objects.count(), 2)
        self.assertEqual(StockTransaction.objects.first().performed_by.username, "s")
        self.assertTrue(self.product.is_low_stock)

    def test_edit_form_does_not_expose_quantity(self):
        self.login("m")
        resp = self.client.get(reverse("product_edit", args=[self.product.pk]))
        self.assertNotIn("quantity", resp.context["form"].fields)

    # --- reporting ---
    def test_csv_report(self):
        self.login("m")
        resp = self.client.get(reverse("report_csv"))
        self.assertEqual(resp["Content-Type"], "text/csv")
        self.assertIn("HAM-1", resp.content.decode())
