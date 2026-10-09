# StockPilot - Inventory Management System

Django + Bootstrap 5 + SQLite. Server-rendered pages only (no API, no JavaScript framework).

## Features
- **Stock control rules:** stock-out can never exceed available quantity (checked in the form and re-checked inside a database transaction); product quantity changes only through recorded stock movements; low-stock flag at a per-product reorder level; products with history cannot be deleted.
- **Automated reporting:** dashboard totals, low-stock alerts, stock-by-category report, 30-day in/out summary, CSV export.
- **Role-based access control** (Django groups): Staff = view + record stock; Manager = + add/edit products & reports; Admin = + delete products.
- Full audit trail: every movement stores who did it and when.

## Run it
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo          # creates roles, demo users and sample data
python manage.py runserver
```
Open http://127.0.0.1:8000/ and log in with `demo_staff`, `demo_manager` or `demo_admin` (password `Demo@12345`, demo only).
Create your own admin with `python manage.py createsuperuser` (superusers count as Admin). Users get a role by adding them to the Admin / Manager / Staff group in `/admin/`.

Run tests: `python manage.py test`

## Structure
- `inventory/models.py` Category, Product, StockTransaction
- `inventory/permissions.py` role logic and `role_required` decorator
- `inventory/views.py` all pages, stock rules, report + CSV
- `inventory/templates/` Bootstrap templates
