from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from catalogue.models import Category, Jewel

ITEMS = [
    ("Rings", "Solitaire Diamond Ring", "diamond", 45999, True, "A classic solitaire set in 18k white gold with a brilliant-cut stone."),
    ("Rings", "Twisted Gold Band", "gold", 12999, False, "A slim 22k gold band with a subtle twist pattern, comfortable for daily wear."),
    ("Rings", "Rose Gold Stackable Ring", "rose_gold", 8499, False, "Thin stackable ring in polished rose gold."),
    ("Necklaces", "Pearl Drop Pendant", "gold", 15499, True, "Freshwater pearl pendant on a fine gold chain."),
    ("Necklaces", "Silver Infinity Necklace", "silver", 2999, False, "Sterling silver infinity pendant on an adjustable chain."),
    ("Necklaces", "Diamond Tennis Necklace", "diamond", 89999, True, "A line of round diamonds set in white gold, an evening statement piece."),
    ("Earrings", "Gold Jhumka Earrings", "gold", 18999, True, "Traditional jhumka design in 22k gold with delicate filigree work."),
    ("Earrings", "Silver Hoop Earrings", "silver", 1799, False, "Lightweight sterling silver hoops."),
    ("Earrings", "Platinum Stud Earrings", "platinum", 32999, False, "Minimal round studs in platinum."),
    ("Bracelets", "Gold Chain Bracelet", "gold", 21999, False, "Curb-link chain bracelet in 22k gold with a secure clasp."),
    ("Bracelets", "Rose Gold Charm Bracelet", "rose_gold", 11499, False, "Charm bracelet with three removable charms."),
    ("Bracelets", "Silver Cuff", "silver", 3499, True, "Hand-hammered sterling silver cuff."),
]


class Command(BaseCommand):
    help = "Load sample categories and jewellery (no images - add photos from the admin panel)."

    def add_arguments(self, parser):
        parser.add_argument("--admin", action="store_true", help="Also create a demo superuser (admin / Admin@12345)")

    def handle(self, *args, **options):
        for cat, name, material, price, featured, desc in ITEMS:
            category, _ = Category.objects.get_or_create(name=cat)
            Jewel.objects.get_or_create(name=name, defaults=dict(category=category, material=material, price=price, is_featured=featured, description=desc))
        if options["admin"] and not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "Admin@12345")
        self.stdout.write(self.style.SUCCESS(f"{Jewel.objects.count()} pieces in catalogue."))
