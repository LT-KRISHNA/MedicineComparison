# Medicine Price Comparison & Alternative Suggestion System

A Django-based web application that helps users find the best prices for medicines and discover cheaper alternatives with identical compositions.

## Features

- 🔍 Search medicines by brand name (case-insensitive, partial matching)
- 💰 Compare prices across multiple pharmacies
- 💊 Find alternative medicines with the same composition
- 📊 Calculate potential savings
- 📱 Responsive design with Bootstrap 5
- ⚡ Fast search with database indexing

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
- 30 medicines covering 8 different compositions
- 7 Indian pharmacies (Apollo Pharmacy, MedPlus, Netmeds, PharmEasy, 1mg, Wellness Forever, Fortis Healthcare Pharmacy)
- 159+ price records with realistic price variations in INR (10-40% difference)
- Multiple medicines per composition to demonstrate alternatives feature

Example compositions:
- Paracetamol 500mg: Crocin, Dolo 650, Calpol, Metacin
- Ibuprofen 400mg: Brufen, Combiflam, Ibugesic
- Omeprazole 20mg: Omez, Omeprazole, Ocid

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
