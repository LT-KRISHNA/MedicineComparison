# Quick Reference Card

## 🚀 Start the System
```bash
python manage.py runserver
```
Visit: **http://127.0.0.1:8000/**

## 🔍 Try These Searches

| Search Term | What You'll See | Savings |
|-------------|-----------------|---------|
| **Crocin** | Branded paracetamol + Generic alternative | 73% (₹22) |
| **Brufen** | Branded ibuprofen + Generic alternative | 73% (₹33) |
| **Omez** | Branded omeprazole + Generic alternative | 71% (₹60) |
| **Glycomet** | Branded metformin + Generic alternative | 72% (₹47) |
| **Generic** | All generic medicines | Various |

## 💊 Medicine Types

| Type | Badge Color | Example | Price Range |
|------|-------------|---------|-------------|
| **Generic** | 🟢 Green | Paracetamol (Generic) | ₹8-15 |
| **Branded** | 🔵 Blue | Crocin | ₹25-35 |

## 🏥 Pharmacies in System

1. **Jan Aushadhi Kendra** - Government, lowest generic prices
2. **Apollo Pharmacy** - Online & retail
3. **MedPlus** - Online & retail
4. **Netmeds** - Online
5. **PharmEasy** - Online
6. **1mg** - Online
7. **Local Medical Store** - Traditional

## 📊 Price Types

| Type | Meaning | Typical For |
|------|---------|-------------|
| **MRP** | Maximum Retail Price | Local stores |
| **Online** | Online pharmacy price | E-commerce |
| **Average** | Average market price | General reference |

## 🎯 Key Features

### Homepage
- ✅ Search bar
- ✅ 5 generic benefits
- ✅ Feature cards

### Search Results
- ✅ Medicine list
- ✅ Generic/Branded labels
- ✅ Quick info cards

### Medicine Details
- ✅ Price comparison table
- ✅ Alternative medicines
- ✅ Savings calculator
- ✅ Generic benefits (if applicable)
- ✅ Detailed information

## 🎨 Visual Cues

| Element | Color | Meaning |
|---------|-------|---------|
| Green border | 🟢 | Generic medicine |
| Green badge | 🟢 | "Generic" label |
| Green highlight | 🟢 | Lowest price |
| Green savings | 🟢 | Money saved |
| Blue badge | 🔵 | "Branded" label |

## 📱 Admin Panel

**URL**: http://127.0.0.1:8000/admin/

### Quick Actions
- **Add Medicine**: Include type (generic/branded)
- **Update Price**: Set price type and amount
- **Edit Benefits**: Modify generic benefits
- **Add Pharmacy**: Include new pharmacy

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run with details
python manage.py test --verbosity=2

# Check system
python manage.py check
```

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| **QUICKSTART.md** | 3-step setup guide |
| **README.md** | Main documentation |
| **GENERIC_MEDICINE_GUIDE.md** | Generic medicine info |
| **SYSTEM_OVERVIEW.md** | Complete overview |
| **IMPLEMENTATION_COMPLETE.md** | What was built |

## 💡 Pro Tips

1. **Search Tips**
   - Use partial names (e.g., "Croc" finds "Crocin")
   - Search is case-insensitive
   - Try searching "Generic" to see all generics

2. **Understanding Savings**
   - Green badges show savings amount
   - Percentage shows relative savings
   - Compare with original medicine price

3. **Generic Benefits**
   - Read on homepage
   - Shown again on results page
   - Explains safety and effectiveness

4. **Price Information**
   - Prices are general/indicative
   - Check with pharmacy for current prices
   - Multiple price types shown

## ⚠️ Important Reminders

- ✅ Prices are **general/indicative**
- ✅ **Consult doctor** before switching
- ✅ **Verify prices** with pharmacy
- ✅ System is **educational** only
- ✅ Not a substitute for **medical advice**

## 🎯 Common Tasks

### Add New Medicine
1. Go to admin panel
2. Click "Medicines" → "Add Medicine"
3. Fill in all fields
4. Select type (generic/branded)
5. Add description, uses, side effects
6. Save

### Update Prices
1. Go to admin panel
2. Click "Prices" → Find medicine
3. Update price value
4. Select price type
5. Save (last_updated auto-updates)

### Modify Generic Benefits
1. Go to admin panel
2. Click "Generic Benefits"
3. Edit title, description, icon
4. Change order number
5. Toggle active status
6. Save

## 📞 Quick Help

**System not starting?**
```bash
python manage.py migrate
python manage.py seed_data
```

**No data showing?**
```bash
python manage.py seed_data
```

**Tests failing?**
```bash
python manage.py test --verbosity=2
```

**Need admin access?**
```bash
python manage.py createsuperuser
```

---

**Keep this card handy for quick reference!** 📋✨
