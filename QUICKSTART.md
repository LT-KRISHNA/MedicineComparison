# Quick Start Guide

Get the Medicine Price Comparison & Generic Alternative System running in 3 simple steps:

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
- **22 medicines** (11 branded + 11 generic alternatives)
- **7 pharmacies** (including Jan Aushadhi Kendra for generics)
- **103+ price records** with realistic variations in INR
- **5 educational benefits** about generic medicines

## Try It Out

### Search for Branded Medicines
1. Search for "Crocin" (branded paracetamol)
2. Click to see price range: ₹25-35
3. View generic alternative: "Paracetamol (Generic)" at ₹8
4. See savings: **Save ₹22 (73%)**

### Explore Generic Options
1. Search for "Generic"
2. See all generic medicines highlighted in green
3. Compare with branded equivalents
4. Learn about generic medicine benefits

### Popular Searches
- **"Crocin"** - See paracetamol generic alternative (73% savings)
- **"Brufen"** - See ibuprofen generic alternative (73% savings)
- **"Omez"** - See omeprazole generic alternative (71% savings)
- **"Glycomet"** - See metformin generic alternative (72% savings)
- **"Atorva"** - See atorvastatin generic alternative (71% savings)

## Key Features to Explore

### 1. Generic Benefits Section
- Homepage shows 5 key benefits of generic medicines
- Educational content with icons
- Explains bioequivalence and safety

### 2. Price Comparison
- See general price ranges across pharmacies
- Prices marked as MRP, Online, or Average
- Lowest price highlighted in green

### 3. Alternative Finder
- Generic alternatives highlighted in green
- Exact savings shown (amount + percentage)
- Detailed information for each alternative

### 4. Medicine Details
- Description and uses
- Common side effects
- Manufacturer information
- Medicine type (Branded/Generic)

## Admin Access (Optional)

Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```

Then visit: **http://127.0.0.1:8000/admin/**

### Admin Features
- Add/edit medicines with detailed information
- Update price information
- Manage generic benefits content
- Add new pharmacies

## Running Tests

```bash
python manage.py test
```

All 11 tests should pass!

## Understanding the System

### Generic vs Branded
- **Branded**: Original brand name medicines (e.g., Crocin, Brufen)
- **Generic**: Same active ingredient, different name (e.g., Paracetamol Generic)
- **Savings**: Generics typically 30-80% cheaper

### Price Types
- **MRP**: Maximum Retail Price
- **Online**: Typical online pharmacy price
- **Average**: Average market price

### Pharmacies
- **Jan Aushadhi Kendra**: Government pharmacy with lowest generic prices
- **Online**: Apollo, MedPlus, Netmeds, PharmEasy, 1mg
- **Local**: Traditional medical stores

## Important Notes

⚠️ **Disclaimer**: Prices shown are general/indicative. Always:
- Check current prices with your local pharmacy
- Consult your doctor before switching medications
- Verify medicine details with healthcare professionals

✅ **Generic Safety**: All generic medicines are:
- Government approved (CDSCO in India)
- Bioequivalent to branded versions
- Same active ingredient and effectiveness
- Significantly more affordable

## Next Steps

1. **Explore the system** - Try different searches
2. **Read the guides** - Check GENERIC_MEDICINE_GUIDE.md
3. **Customize data** - Add your own medicines via admin
4. **Share feedback** - Help improve the system

---

**Ready to save money on medicines while maintaining quality!** 💊💰
