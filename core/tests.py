from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from .models import Medicine, Pharmacy, Price
from .services import MedicineSearchService, PriceComparisonService, AlternativeFinderService


class MedicineModelTest(TestCase):
    def test_medicine_creation(self):
        medicine = Medicine.objects.create(
            brand_name='Test Medicine',
            composition='Test Composition',
            strength='100mg',
            manufacturer='Test Manufacturer'
        )
        self.assertEqual(str(medicine), 'Test Medicine (Test Composition)')


class PharmacyModelTest(TestCase):
    def test_pharmacy_creation(self):
        pharmacy = Pharmacy.objects.create(
            name='Test Pharmacy',
            website_url='https://test.com'
        )
        self.assertEqual(str(pharmacy), 'Test Pharmacy')


class PriceModelTest(TestCase):
    def setUp(self):
        self.medicine = Medicine.objects.create(
            brand_name='Test Medicine',
            composition='Test Composition',
            strength='100mg',
            manufacturer='Test Manufacturer'
        )
        self.pharmacy = Pharmacy.objects.create(name='Test Pharmacy')
    
    def test_price_creation(self):
        price = Price.objects.create(
            medicine=self.medicine,
            pharmacy=self.pharmacy,
            price=Decimal('10.99')
        )
        self.assertEqual(price.price, Decimal('10.99'))


class MedicineSearchServiceTest(TestCase):
    def setUp(self):
        Medicine.objects.create(
            brand_name='Tylenol',
            composition='Paracetamol 500mg',
            strength='500mg',
            manufacturer='Johnson & Johnson'
        )
        Medicine.objects.create(
            brand_name='Advil',
            composition='Ibuprofen 400mg',
            strength='400mg',
            manufacturer='Pfizer'
        )
    
    def test_search_case_insensitive(self):
        results = MedicineSearchService.search_medicines('tylenol')
        self.assertEqual(results.count(), 1)
        self.assertEqual(results.first().brand_name, 'Tylenol')
    
    def test_search_partial_match(self):
        results = MedicineSearchService.search_medicines('tyl')
        self.assertEqual(results.count(), 1)
    
    def test_search_empty_query(self):
        results = MedicineSearchService.search_medicines('')
        self.assertEqual(results.count(), 0)


class PriceComparisonServiceTest(TestCase):
    def setUp(self):
        self.medicine = Medicine.objects.create(
            brand_name='Test Medicine',
            composition='Test Composition',
            strength='100mg',
            manufacturer='Test Manufacturer'
        )
        pharmacy1 = Pharmacy.objects.create(name='Pharmacy 1')
        pharmacy2 = Pharmacy.objects.create(name='Pharmacy 2')
        
        Price.objects.create(medicine=self.medicine, pharmacy=pharmacy1, price=Decimal('10.00'))
        Price.objects.create(medicine=self.medicine, pharmacy=pharmacy2, price=Decimal('15.00'))
    
    def test_price_comparison(self):
        result = PriceComparisonService.get_price_comparison(self.medicine.id)
        self.assertEqual(result['lowest_price'], Decimal('10.00'))
        self.assertEqual(result['highest_price'], Decimal('15.00'))
        self.assertEqual(result['savings_percentage'], Decimal('33.33'))


class AlternativeFinderServiceTest(TestCase):
    def setUp(self):
        self.medicine1 = Medicine.objects.create(
            brand_name='Tylenol',
            composition='Paracetamol 500mg',
            strength='500mg',
            manufacturer='Johnson & Johnson'
        )
        self.medicine2 = Medicine.objects.create(
            brand_name='Panadol',
            composition='Paracetamol 500mg',
            strength='500mg',
            manufacturer='GSK'
        )
        pharmacy = Pharmacy.objects.create(name='Test Pharmacy')
        Price.objects.create(medicine=self.medicine2, pharmacy=pharmacy, price=Decimal('8.00'))
    
    def test_find_alternatives(self):
        alternatives = AlternativeFinderService.find_alternatives(self.medicine1.id)
        self.assertEqual(len(alternatives), 1)
        self.assertEqual(alternatives[0]['medicine'].brand_name, 'Panadol')


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.medicine = Medicine.objects.create(
            brand_name='Tylenol',
            composition='Paracetamol 500mg',
            strength='500mg',
            manufacturer='Johnson & Johnson'
        )
    
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Find the Best Medicine Prices')
    
    def test_search_view(self):
        response = self.client.get(reverse('search'), {'q': 'Tylenol'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tylenol')
    
    def test_results_view(self):
        response = self.client.get(reverse('results', args=[self.medicine.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tylenol')
