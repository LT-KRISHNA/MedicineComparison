# Design Document: Medicine Price Comparison & Alternative Suggestion System

## Overview

The Medicine Price Comparison & Alternative Suggestion System is a Django-based web application that helps users find the best prices for medicines and discover cheaper alternatives with identical compositions. The system follows a clean 3-tier architecture (Presentation, Application, Data) and uses Django's MVT (Model-View-Template) pattern.

The core workflow is:
1. User searches for a medicine by brand name
2. System displays all pharmacies selling that medicine, sorted by price
3. System identifies and displays alternative medicines with the same composition
4. System calculates and highlights potential savings

## Architecture

### 3-Tier Architecture

**Presentation Layer (Templates + Static Files)**
- HTML templates using Django template language
- Bootstrap 5 for responsive UI components
- JavaScript for client-side interactivity
- CSS for custom styling

**Application Layer (Views + Business Logic)**
- Django views handling HTTP requests/responses
- Business logic services for price comparison and alternative identification
- Form handling and validation
- Query optimization and data aggregation

**Data Layer (Models + ORM)**
- Django models defining database schema
- Django ORM for database operations
- Model managers for complex queries
- Database indexing for performance

### Django Project Structure

```
medcompare/                 # Project root
├── manage.py
├── medcompare/            # Project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                  # Main application
│   ├── __init__.py
│   ├── models.py         # Data models
│   ├── views.py          # View controllers
│   ├── urls.py           # URL routing
│   ├── forms.py          # Form definitions
│   ├── services.py       # Business logic
│   ├── admin.py          # Django admin config
│   ├── management/       # Custom commands
│   │   └── commands/
│   │       └── seed_data.py
│   └── migrations/
├── templates/
│   ├── base.html         # Base template
│   ├── home.html         # Search page
│   └── results.html      # Results page
└── static/
    ├── css/
    │   └── custom.css
    └── js/
        └── main.js
```

## Components and Interfaces

### Data Models

**Medicine Model**
```python
class Medicine(models.Model):
    brand_name = CharField(max_length=200, db_index=True)
    composition = CharField(max_length=500, db_index=True)
    strength = CharField(max_length=100)
    manufacturer = CharField(max_length=200)
    created_at = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.brand_name} ({self.composition})"
```

**Pharmacy Model**
```python
class Pharmacy(models.Model):
    name = CharField(max_length=200, unique=True)
    website_url = URLField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```

**Price Model**
```python
class Price(models.Model):
    medicine = ForeignKey(Medicine, on_delete=CASCADE, related_name='prices')
    pharmacy = ForeignKey(Pharmacy, on_delete=CASCADE, related_name='prices')
    price = DecimalField(max_digits=10, decimal_places=2)
    last_updated = DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = [['medicine', 'pharmacy']]
        indexes = [
            Index(fields=['medicine', 'price']),
        ]
    
    def __str__(self):
        return f"{self.medicine.brand_name} at {self.pharmacy.name}: ${self.price}"
```

### Business Logic Services

**MedicineSearchService**
```python
class MedicineSearchService:
    @staticmethod
    def search_medicines(query: str) -> QuerySet[Medicine]:
        """
        Search for medicines by brand name (case-insensitive, partial match)
        Returns: QuerySet of matching Medicine objects
        """
        if not query:
            return Medicine.objects.none()
        
        return Medicine.objects.filter(
            brand_name__icontains=query
        ).order_by('brand_name')
```

**PriceComparisonService**
```python
class PriceComparisonService:
    @staticmethod
    def get_price_comparison(medicine_id: int) -> dict:
        """
        Get all prices for a medicine, sorted by price ascending
        Returns: {
            'medicine': Medicine object,
            'prices': List of Price objects sorted by price,
            'lowest_price': Decimal,
            'highest_price': Decimal,
            'savings_percentage': Decimal
        }
        """
        medicine = Medicine.objects.get(id=medicine_id)
        prices = medicine.prices.select_related('pharmacy').order_by('price')
        
        if not prices.exists():
            return {
                'medicine': medicine,
                'prices': [],
                'lowest_price': None,
                'highest_price': None,
                'savings_percentage': 0
            }
        
        lowest = prices.first().price
        highest = prices.last().price
        
        if highest > 0:
            savings = ((highest - lowest) / highest) * 100
        else:
            savings = 0
        
        return {
            'medicine': medicine,
            'prices': list(prices),
            'lowest_price': lowest,
            'highest_price': highest,
            'savings_percentage': round(savings, 2)
        }
```

**AlternativeFinderService**
```python
class AlternativeFinderService:
    @staticmethod
    def find_alternatives(medicine_id: int) -> List[dict]:
        """
        Find alternative medicines with same composition, excluding the original
        Returns: List of dicts with {
            'medicine': Medicine object,
            'lowest_price': Decimal,
            'pharmacy_name': str
        } sorted by lowest_price ascending
        """
        medicine = Medicine.objects.get(id=medicine_id)
        
        # Find medicines with same composition, excluding current medicine
        alternatives = Medicine.objects.filter(
            composition=medicine.composition
        ).exclude(id=medicine_id)
        
        # For each alternative, get the lowest price
        results = []
        for alt in alternatives:
            lowest_price_record = alt.prices.select_related('pharmacy').order_by('price').first()
            
            if lowest_price_record:
                results.append({
                    'medicine': alt,
                    'lowest_price': lowest_price_record.price,
                    'pharmacy_name': lowest_price_record.pharmacy.name
                })
        
        # Sort by lowest price
        results.sort(key=lambda x: x['lowest_price'])
        
        return results
```

### Views

**HomeView**
```python
def home(request):
    """
    Display the search homepage
    """
    return render(request, 'home.html')
```

**SearchView**
```python
def search(request):
    """
    Handle medicine search and display results
    """
    query = request.GET.get('q', '').strip()
    
    if not query:
        return redirect('home')
    
    medicines = MedicineSearchService.search_medicines(query)
    
    context = {
        'query': query,
        'medicines': medicines,
        'count': medicines.count()
    }
    
    return render(request, 'search_results.html', context)
```

**ResultsView**
```python
def results(request, medicine_id):
    """
    Display price comparison and alternatives for a specific medicine
    """
    try:
        comparison_data = PriceComparisonService.get_price_comparison(medicine_id)
        alternatives = AlternativeFinderService.find_alternatives(medicine_id)
        
        context = {
            'medicine': comparison_data['medicine'],
            'prices': comparison_data['prices'],
            'lowest_price': comparison_data['lowest_price'],
            'highest_price': comparison_data['highest_price'],
            'savings_percentage': comparison_data['savings_percentage'],
            'alternatives': alternatives
        }
        
        return render(request, 'results.html', context)
    
    except Medicine.DoesNotExist:
        return redirect('home')
```

### URL Configuration

```python
# core/urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('results/<int:medicine_id>/', views.results, name='results'),
]
```

### Forms

```python
class MedicineSearchForm(forms.Form):
    query = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search for medicine by brand name...',
            'autocomplete': 'off'
        })
    )
```

## Data Models

### Entity Relationship

```
Medicine (1) ----< (N) Price (N) >---- (1) Pharmacy

Medicine:
- id (PK)
- brand_name (indexed)
- composition (indexed)
- strength
- manufacturer
- created_at

Pharmacy:
- id (PK)
- name (unique)
- website_url
- created_at

Price:
- id (PK)
- medicine_id (FK, indexed)
- pharmacy_id (FK)
- price (indexed with medicine_id)
- last_updated
- UNIQUE(medicine_id, pharmacy_id)
```

### Database Indexing Strategy

1. **Medicine.brand_name**: B-tree index for fast case-insensitive searches using `icontains`
2. **Medicine.composition**: B-tree index for fast alternative lookups
3. **Price (medicine_id, price)**: Composite index for efficient price sorting per medicine
4. **Price (medicine_id, pharmacy_id)**: Unique constraint prevents duplicate price entries

### Sample Data Structure

The seed data will include:
- 20+ medicines covering 5-6 different compositions
- 5-7 pharmacies with realistic names
- 60+ price records showing price variations (10-40% difference between highest and lowest)
- Multiple medicines per composition to demonstrate alternatives feature

Example:
- Paracetamol 500mg: Tylenol, Panadol, Calpol (same composition, different brands)
- Ibuprofen 400mg: Advil, Motrin, Nurofen (same composition, different brands)


## Correctness Properties

A property is a characteristic or behavior that should hold true across all valid executions of a system - essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.

### Property 1: Case-insensitive partial search completeness

*For any* medicine in the database and any substring of its brand name (regardless of case), searching for that substring should return the medicine in the results, and all returned results should contain the search query as a substring (case-insensitive).

**Validates: Requirements 1.1, 1.2, 1.3, 1.5**

### Property 2: Price records completeness and ordering

*For any* medicine with price records, retrieving its price comparison data should return all price records for that medicine, sorted in ascending order by price.

**Validates: Requirements 2.1, 2.2**

### Property 3: Lowest price identification

*For any* medicine with price records, the identified lowest price should be less than or equal to all other prices for that medicine, and the pharmacy associated with the lowest price should be marked as highlighted.

**Validates: Requirements 2.3, 3.1**

### Property 4: Savings calculation correctness

*For any* medicine with multiple price records, the savings percentage should equal ((highest_price - lowest_price) / highest_price) * 100, where highest_price is the maximum price and lowest_price is the minimum price across all price records.

**Validates: Requirements 2.5, 3.2, 3.3**

### Property 5: Alternative identification correctness

*For any* medicine, all alternatives should have the exact same composition as the original medicine AND should not include the original medicine itself.

**Validates: Requirements 4.1, 4.2**

### Property 6: Alternative lowest price accuracy

*For any* alternative medicine in the results, the displayed lowest price should be less than or equal to all price records for that alternative medicine.

**Validates: Requirements 4.3**

### Property 7: Alternative sorting correctness

*For any* list of alternatives, the alternatives should be sorted in ascending order by their lowest price.

**Validates: Requirements 4.4**

### Property 8: Model persistence round-trip

*For any* valid Medicine, Pharmacy, or Price object, saving it to the database and then retrieving it should return an object with all the same field values.

**Validates: Requirements 5.1, 5.2, 5.3**

### Property 9: Search result limit enforcement

*For any* search query, the number of returned results should not exceed the configured maximum limit (e.g., 50 results).

**Validates: Requirements 9.3**

### Property 10: Medicine validation rejects empty brand names

*For any* attempt to create or update a Medicine with an empty or whitespace-only brand_name, the system should reject the operation and raise a validation error.

**Validates: Requirements 10.1**

### Property 11: Medicine validation rejects empty compositions

*For any* attempt to create or update a Medicine with an empty or whitespace-only composition, the system should reject the operation and raise a validation error.

**Validates: Requirements 10.2**

### Property 12: Price validation rejects non-positive values

*For any* attempt to create or update a Price with a price value that is zero or negative, the system should reject the operation and raise a validation error.

**Validates: Requirements 10.3**

### Property 13: Pharmacy validation rejects empty names

*For any* attempt to create or update a Pharmacy with an empty or whitespace-only name, the system should reject the operation and raise a validation error.

**Validates: Requirements 10.4**

## Error Handling

### Input Validation Errors

**Empty Search Query**
- Behavior: Redirect to homepage or display empty results
- User feedback: "Please enter a medicine name to search"

**Invalid Medicine ID**
- Behavior: Redirect to homepage with error message
- User feedback: "Medicine not found. Please search again."

**Database Errors**
- Behavior: Log error, display generic error page
- User feedback: "An error occurred. Please try again later."

### Data Validation Errors

**Model Validation**
- Django model validation catches empty required fields
- Raises `ValidationError` with descriptive message
- Admin interface displays validation errors to users

**Form Validation**
- Django form validation on search form
- Client-side validation for immediate feedback
- Server-side validation as final check

### Edge Cases

**No Price Records**
- Display message: "No pricing information available for this medicine"
- Show medicine details but hide price comparison table
- Still show alternatives if available

**No Alternatives**
- Display message: "No alternative medicines found with the same composition"
- Hide alternatives section
- Still show price comparison if available

**Single Price Record**
- Display the single price
- Show "No comparison available" or "Savings: 0%"
- Still show alternatives if available

**Duplicate Price Records**
- Prevented by database unique constraint on (medicine_id, pharmacy_id)
- If attempted, raise IntegrityError
- Admin interface prevents duplicate entries

## Testing Strategy

### Dual Testing Approach

The system will use both unit testing and property-based testing for comprehensive coverage:

**Unit Tests**: Verify specific examples, edge cases, and error conditions
- Test specific search queries with known results
- Test edge cases (empty results, single price, no alternatives)
- Test error handling (invalid IDs, validation errors)
- Test integration between views and services

**Property Tests**: Verify universal properties across all inputs
- Test search behavior with randomly generated medicines and queries
- Test price comparison calculations with random price sets
- Test alternative finding with random compositions
- Test data validation with random invalid inputs

Together, unit tests catch concrete bugs in specific scenarios, while property tests verify general correctness across the input space.

### Property-Based Testing Configuration

**Library**: Use `hypothesis` for Python/Django property-based testing

**Configuration**:
- Minimum 100 iterations per property test
- Each test tagged with comment referencing design property
- Tag format: `# Feature: medicine-price-comparison, Property {number}: {property_text}`

**Example Property Test Structure**:
```python
from hypothesis import given, strategies as st
from hypothesis.extra.django import TestCase

class MedicineSearchPropertyTests(TestCase):
    @given(
        brand_name=st.text(min_size=1, max_size=100),
        query=st.text(min_size=1, max_size=50)
    )
    @settings(max_examples=100)
    def test_case_insensitive_search(self, brand_name, query):
        # Feature: medicine-price-comparison, Property 1: Case-insensitive partial search completeness
        
        # Create medicine with brand_name
        medicine = Medicine.objects.create(
            brand_name=brand_name,
            composition="Test Composition",
            strength="100mg",
            manufacturer="Test Manufacturer"
        )
        
        # If query is substring of brand_name (case-insensitive)
        if query.lower() in brand_name.lower():
            results = MedicineSearchService.search_medicines(query)
            # Medicine should be in results
            assert medicine in results
            
        # All results should contain query (case-insensitive)
        results = MedicineSearchService.search_medicines(query)
        for result in results:
            assert query.lower() in result.brand_name.lower()
```

### Unit Testing Focus Areas

1. **View Integration Tests**
   - Test HTTP request/response flow
   - Test template rendering with context
   - Test URL routing

2. **Service Layer Tests**
   - Test MedicineSearchService with specific queries
   - Test PriceComparisonService with known price sets
   - Test AlternativeFinderService with known compositions

3. **Model Tests**
   - Test model creation and retrieval
   - Test model relationships (ForeignKey)
   - Test model string representations

4. **Edge Case Tests**
   - Empty search results
   - Single price record (no comparison)
   - No alternatives available
   - Invalid medicine ID

5. **Validation Tests**
   - Empty required fields
   - Invalid price values (negative, zero)
   - Duplicate price records

### Test Coverage Goals

- Minimum 80% code coverage
- 100% coverage of business logic services
- All edge cases explicitly tested
- All validation rules tested

### Integration Testing

- Test complete user workflows (search → select → view results)
- Test database queries with realistic data volumes
- Test with seed data to ensure realistic scenarios work

### Manual Testing Checklist

- Responsive design on mobile, tablet, desktop
- Bootstrap components render correctly
- Search autocomplete behavior (if implemented)
- Visual highlighting of cheapest option
- Healthcare disclaimer visibility
- Link navigation between pages
