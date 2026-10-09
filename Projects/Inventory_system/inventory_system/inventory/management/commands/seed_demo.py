import random

from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand

from inventory.models import Category, Product, StockTransaction
from inventory.permissions import ADMIN, MANAGER, STAFF

DEMO_PASSWORD = "Demo@12345"  # demo data only - change or delete these users for real use

PRODUCTS = {
    "Electronics": [("USB-C Cable 1m", "ELE-001", 199, 120, 30), ("Wireless Mouse", "ELE-002", 549, 8, 15), ("20000mAh Power Bank", "ELE-003", 1499, 25, 10), ("HDMI Adapter", "ELE-004", 349, 4, 10)],
    "Stationery": [("A4 Paper Ream", "STA-001", 289, 60, 20), ("Ball Pen (Box of 50)", "STA-002", 250, 14, 12), ("Spiral Notebook", "STA-003", 79, 200, 50)],
    "Furniture": [("Office Chair", "FUR-001", 4999, 6, 5), ("Study Desk", "FUR-002", 6499, 3, 4)],
    "Cleaning": [("Floor Cleaner 5L", "CLE-001", 420, 30, 10), ("Microfibre Cloth Pack", "CLE-002", 150, 9, 15)],
}


class Command(BaseCommand):
    help = "Create the Admin/Manager/Staff roles, three demo users, and sample inventory data."

    def handle(self, *args, **options):
        groups = {name: Group.objects.get_or_create(name=name)[0] for name in (ADMIN, MANAGER, STAFF)}
        for username, role in (("demo_admin", ADMIN), ("demo_manager", MANAGER), ("demo_staff", STAFF)):
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(DEMO_PASSWORD)
                user.save()
            user.groups.set([groups[role]])
        for cat_name, items in PRODUCTS.items():
            cat, _ = Category.objects.get_or_create(name=cat_name)
            for name, sku, price, qty, reorder in items:
                Product.objects.get_or_create(sku=sku, defaults=dict(name=name, category=cat, unit_price=price, quantity=qty, reorder_level=reorder))
        if not StockTransaction.objects.exists():
            staff = User.objects.get(username="demo_staff")
            random.seed(1)
            for p in Product.objects.all()[:6]:
                qty = random.randint(5, 20)
                StockTransaction.objects.create(product=p, movement_type="IN", quantity=qty, note="Initial delivery", performed_by=staff)
                p.quantity += qty
                p.save(update_fields=["quantity"])
        self.stdout.write(self.style.SUCCESS(f"Seeded. Users: demo_admin / demo_manager / demo_staff  password: {DEMO_PASSWORD}"))
