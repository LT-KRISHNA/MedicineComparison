# Quick Start Guide

Get the Medicine Price Comparison app running in 3 simple steps:

## Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 2: Setup Database
```bash
python manage.py migrate
python manage.py seed_data
```

## Step 3: Run the Server
```bash
python manage.py runserver
```

Then open your browser to: **http://127.0.0.1:8000/**

## What's Included

The seed data creates:
- 30 medicines (including Crocin, Dolo 650, Brufen, Omez, etc.)
- 7 pharmacies (Apollo, MedPlus, Netmeds, PharmEasy, 1mg, etc.)
- 159+ price records with realistic variations (in INR)

## Try It Out

1. Search for "Crocin" or "Dolo"
2. Click on a medicine to see price comparison
3. View cheaper alternatives with the same composition
4. See potential savings in ₹!

## Admin Access (Optional)

Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```

Then visit: **http://127.0.0.1:8000/admin/**

## Running Tests

```bash
python manage.py test
```

All 11 tests should pass!
