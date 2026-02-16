from django.core.management.base import BaseCommand
from core.models import Medicine, Pharmacy, Price
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Seed the database with sample medicine, pharmacy, and price data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        Price.objects.all().delete()
        Medicine.objects.all().delete()
        Pharmacy.objects.all().delete()

        self.stdout.write('Creating pharmacies...')
        pharmacies = [
            Pharmacy.objects.create(name='Apollo Pharmacy', website_url='https://www.apollopharmacy.in'),
            Pharmacy.objects.create(name='MedPlus', website_url='https://www.medplusmart.com'),
            Pharmacy.objects.create(name='Netmeds', website_url='https://www.netmeds.com'),
            Pharmacy.objects.create(name='PharmEasy', website_url='https://www.pharmeasy.in'),
            Pharmacy.objects.create(name='1mg', website_url='https://www.1mg.com'),
            Pharmacy.objects.create(name='Wellness Forever', website_url='https://www.wellnessforever.com'),
            Pharmacy.objects.create(name='Fortis Healthcare Pharmacy', website_url='https://www.fortishealthcare.com'),
        ]
        self.stdout.write(self.style.SUCCESS(f'Created {len(pharmacies)} pharmacies'))

        self.stdout.write('Creating medicines...')
        medicines_data = [
            # Paracetamol 500mg
            ('Crocin', 'Paracetamol 500mg', '500mg', 'GSK Pharmaceuticals'),
            ('Dolo 650', 'Paracetamol 500mg', '500mg', 'Micro Labs'),
            ('Calpol', 'Paracetamol 500mg', '500mg', 'GSK Pharmaceuticals'),
            ('Metacin', 'Paracetamol 500mg', '500mg', 'Mankind Pharma'),
            
            # Ibuprofen 400mg
            ('Brufen', 'Ibuprofen 400mg', '400mg', 'Abbott India'),
            ('Combiflam', 'Ibuprofen 400mg', '400mg', 'Sanofi India'),
            ('Ibugesic', 'Ibuprofen 400mg', '400mg', 'Cipla'),
            
            # Omeprazole 20mg
            ('Omez', 'Omeprazole 20mg', '20mg', 'Dr. Reddy\'s Laboratories'),
            ('Omeprazole', 'Omeprazole 20mg', '20mg', 'Sun Pharma'),
            ('Ocid', 'Omeprazole 20mg', '20mg', 'Ranbaxy'),
            
            # Metformin 500mg
            ('Glycomet', 'Metformin 500mg', '500mg', 'USV Ltd'),
            ('Obimet', 'Metformin 500mg', '500mg', 'Mankind Pharma'),
            ('Metsmall', 'Metformin 500mg', '500mg', 'Ajanta Pharma'),
            
            # Atorvastatin 10mg
            ('Atorva', 'Atorvastatin 10mg', '10mg', 'Zydus Cadila'),
            ('Storvas', 'Atorvastatin 10mg', '10mg', 'Ranbaxy'),
            ('Lipicure', 'Atorvastatin 10mg', '10mg', 'Intas Pharmaceuticals'),
            
            # Amoxicillin 500mg
            ('Novamox', 'Amoxicillin 500mg', '500mg', 'Cipla'),
            ('Mox', 'Amoxicillin 500mg', '500mg', 'Ranbaxy'),
            ('Amoxycillin', 'Amoxicillin 500mg', '500mg', 'Alkem Laboratories'),
            
            # Azithromycin 500mg
            ('Azithral', 'Azithromycin 500mg', '500mg', 'Alembic Pharmaceuticals'),
            ('Zady', 'Azithromycin 500mg', '500mg', 'Mankind Pharma'),
            ('Azee', 'Azithromycin 500mg', '500mg', 'Cipla'),
            
            # Cetirizine 10mg
            ('Cetrizine', 'Cetirizine 10mg', '10mg', 'Cipla'),
            ('Alerid', 'Cetirizine 10mg', '10mg', 'Cipla'),
            ('Okacet', 'Cetirizine 10mg', '10mg', 'Cipla'),
            
            # Additional common Indian medicines
            ('Pantop', 'Pantoprazole 40mg', '40mg', 'Aristo Pharmaceuticals'),
            ('Pan', 'Pantoprazole 40mg', '40mg', 'Alkem Laboratories'),
            ('Cheston Cold', 'Cetirizine + Paracetamol', 'Combo', 'Cipla'),
            ('Sinarest', 'Paracetamol + Phenylephrine', 'Combo', 'Centaur Pharmaceuticals'),
            ('Vicks Action 500', 'Paracetamol + Caffeine', '500mg', 'Procter & Gamble'),
        ]
        
        medicines = []
        for brand_name, composition, strength, manufacturer in medicines_data:
            medicine = Medicine.objects.create(
                brand_name=brand_name,
                composition=composition,
                strength=strength,
                manufacturer=manufacturer
            )
            medicines.append(medicine)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(medicines)} medicines'))

        self.stdout.write('Creating price records...')
        price_count = 0
        
        for medicine in medicines:
            # Each medicine will have prices at 4-6 random pharmacies
            num_pharmacies = random.randint(4, 6)
            selected_pharmacies = random.sample(pharmacies, num_pharmacies)
            
            # Generate a base price for this medicine (in INR)
            base_price = Decimal(random.uniform(20.0, 500.0))
            
            for pharmacy in selected_pharmacies:
                # Vary the price by -20% to +40% from base price
                variation = Decimal(random.uniform(0.8, 1.4))
                price = (base_price * variation).quantize(Decimal('0.01'))
                
                Price.objects.create(
                    medicine=medicine,
                    pharmacy=pharmacy,
                    price=price
                )
                price_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {price_count} price records'))
        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))
