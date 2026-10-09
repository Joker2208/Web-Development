# Aurelia Jewels - Jewellery Store Showcase Website

Django + Bootstrap 5 + SQLite. A responsive product catalogue (no cart or payments, no API).

## Features
- Home page with hero, category tiles and featured pieces
- Collection page: search, category and material filters, sorting, pagination
- Product detail page with related pieces and an "Enquire" button
- Enquiry form saved to the database (view/mark handled in the admin)
- Admin panel to manage categories, jewellery (with image upload) and enquiries
- Fully responsive layout (mobile navbar, fluid grid)

## Run it
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo --admin     # sample products + admin / Admin@12345 (demo only)
python manage.py runserver
```
Site: http://127.0.0.1:8000/  Admin: http://127.0.0.1:8000/admin/
Pieces show a placeholder until you upload photos in the admin panel (Jewels > edit > Image).

Run tests: `python manage.py test`
