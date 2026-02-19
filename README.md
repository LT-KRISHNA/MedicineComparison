# Medicine Price Comparison & Generic Alternative System

A Django-based web application that helps users find general price ranges for medicines and discover cheaper generic alternatives with identical compositions. The system educates users about the benefits of generic medicines while providing comprehensive medicine information.

## Features

- 🔍 Search medicines by brand name (case-insensitive, partial matching)
- 💰 View general price ranges across multiple pharmacies
- 💊 Find generic alternatives with the same active ingredient
- 📊 Calculate potential savings (up to 80% with generics)
- 📚 Educational information about generic medicine benefits
- 📱 Responsive design with Bootstrap 5
- ⚡ Fast search with database indexing
- 🏥 Detailed medicine information (uses, side effects, descriptions)

## What's New: Generic Medicine Focus

### Generic vs Branded Comparison
- Clear labeling of generic and branded medicines
- Side-by-side price comparison
- Exact savings calculation (amount and percentage)
- Highlighted generic alternatives in green

### Educational Content
- 5 key benefits of choosing generic medicines
- Detailed medicine descriptions
- Common uses and applications
- Potential side effects information
- Bioequivalence explanation

### Smart Alternative Finder
- Prioritizes generic alternatives
- Shows savings compared to branded versions
- Indicates medicine type (Generic/Branded)
- Links to detailed information for each alternative

## Technology Stack

- Django 4.2
- SQLite database
- Bootstrap 5
- Python 3.8+

## Installation

1. Clone the repository or navigate to the project directory:
```bash
cd medcompare
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run database migrations:
```bash
python manage.py migrate
```

4. Seed the database with sample data:
```bash
python manage.py seed_data
```

5. Create a superuser for admin access (optional):
```bash
python manage.py createsuperuser
```

## Running the Application

Start the development server:
```bash
python manage.py runserver
```

The application will be available at: http://127.0.0.1:8000/

Admin interface: http://127.0.0.1:8000/admin/

## Usage

1. **Search for a Medicine**: Enter a medicine brand name in the search bar on the homepage
2. **View Search Results**: Click on any medicine from the search results
3. **Compare Prices**: See prices from different pharmacies, sorted from lowest to highest
4. **Find Alternatives**: View alternative medicines with the same composition
5. **Save Money**: Identify the cheapest option and potential savings

## Project Structure

```
medcompare/
├── manage.py
├── requirements.txt
├── README.md
├── medcompare/              # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                    # Main application
│   ├── models.py           # Data models (Medicine, Pharmacy, Price)
│   ├── views.py            # View controllers
│   ├── urls.py             # URL routing
│   ├── forms.py            # Form definitions
│   ├── services.py         # Business logic
│   ├── admin.py            # Django admin configuration
│   └── management/
│       └── commands/
│           └── seed_data.py
├── templates/               # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── search_results.html
│   └── results.html
└── static/                  # Static files
    ├── css/
    │   └── custom.css
    └── js/
        └── main.js
```

## Sample Data

The seed data includes:
- 22 medicines (11 branded + 11 generic alternatives)
- 8 different compositions with generic options
- 7 Indian pharmacies including Jan Aushadhi Kendra
- 103+ price records with realistic price variations in INR
- 5 educational benefits about generic medicines

Example comparisons:
- **Paracetamol 500mg**: Crocin (₹30) vs Generic (₹8) - Save 73%
- **Ibuprofen 400mg**: Brufen (₹45) vs Generic (₹12) - Save 73%
- **Omeprazole 20mg**: Omez (₹85) vs Generic (₹25) - Save 71%
- **Metformin 500mg**: Glycomet (₹65) vs Generic (₹18) - Save 72%
- **Atorvastatin 10mg**: Atorva (₹95) vs Generic (₹28) - Save 71%

## Running Tests

Run all tests:
```bash
python manage.py test
```

Run tests with coverage:
```bash
coverage run --source='.' manage.py test
coverage report
```

## Architecture

The application follows a clean 3-tier architecture:

1. **Presentation Layer**: Django templates with Bootstrap 5
2. **Application Layer**: Django views and business logic services
3. **Data Layer**: Django models with ORM

### Key Components

- **MedicineSearchService**: Handles medicine search with case-insensitive partial matching
- **PriceComparisonService**: Retrieves and sorts prices, calculates savings
- **AlternativeFinderService**: Finds medicines with matching compositions

## Healthcare Disclaimer

This tool is for informational purposes only. Always consult with a healthcare professional before making medical decisions.

## License

This project is for educational purposes.
