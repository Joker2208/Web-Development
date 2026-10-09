from django.test import TestCase
from django.urls import reverse

from .models import Category, Enquiry, Jewel


class CatalogueTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        rings = Category.objects.create(name="Rings")
        necklaces = Category.objects.create(name="Necklaces")
        cls.ring = Jewel.objects.create(name="Gold Ring", category=rings, material="gold", price=1000, description="x", is_featured=True)
        cls.chain = Jewel.objects.create(name="Silver Chain", category=necklaces, material="silver", price=500, description="y")
        cls.hidden = Jewel.objects.create(name="Hidden", category=rings, material="gold", price=900, description="z", is_available=False)

    def test_pages_load(self):
        for name in ("home", "catalogue", "about", "contact"):
            self.assertEqual(self.client.get(reverse(name)).status_code, 200)

    def test_slug_is_unique_for_duplicate_names(self):
        twin = Jewel.objects.create(name="Gold Ring", category=self.ring.category, material="gold", price=1, description="d")
        self.assertNotEqual(twin.slug, self.ring.slug)

    def test_unavailable_items_are_hidden(self):
        self.assertNotContains(self.client.get(reverse("catalogue")), "Hidden")
        self.assertEqual(self.client.get(self.hidden.get_absolute_url()).status_code, 404)

    def test_filter_search_and_sort(self):
        resp = self.client.get(reverse("catalogue"), {"category": "rings"})
        self.assertContains(resp, "Gold Ring"); self.assertNotContains(resp, "Silver Chain")
        resp = self.client.get(reverse("catalogue"), {"q": "chain"})
        self.assertContains(resp, "Silver Chain"); self.assertNotContains(resp, "Gold Ring")
        resp = self.client.get(reverse("catalogue"), {"sort": "low"})
        self.assertEqual([j.name for j in resp.context["page"]], ["Silver Chain", "Gold Ring"])

    def test_detail_page(self):
        self.assertContains(self.client.get(self.ring.get_absolute_url()), "Gold Ring")

    def test_enquiry_saved(self):
        resp = self.client.post(reverse("contact"), {"name": "Asha", "email": "a@example.com", "message": "Price?", "jewel": self.ring.pk})
        self.assertRedirects(resp, reverse("contact"))
        self.assertEqual(Enquiry.objects.get().jewel, self.ring)

    def test_enquiry_requires_valid_email(self):
        resp = self.client.post(reverse("contact"), {"name": "A", "email": "bad", "message": "hi"})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Enquiry.objects.count(), 0)
