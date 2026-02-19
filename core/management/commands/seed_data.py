from django.core.management.base import BaseCommand
from core.models import Medicine, Pharmacy, Price, GenericBenefit
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Seed the database with comprehensive medicine data including generic alternatives'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        Price.objects.all().delete()
        Medicine.objects.all().delete()
        Pharmacy.objects.all().delete()
        GenericBenefit.objects.all().delete()

        self.stdout.write('Creating generic benefits information...')
        benefits = [
            GenericBenefit.objects.create(
                title='Same Active Ingredient',
                description='Generic medicines contain the same active pharmaceutical ingredient as branded versions, ensuring identical therapeutic effects.',
                icon='🔬',
                order=1
            ),
            GenericBenefit.objects.create(
                title='Cost Effective',
                description='Generic medicines are typically 30-80% cheaper than branded alternatives, making healthcare more affordable without compromising quality.',
                icon='💰',
                order=2
            ),
            GenericBenefit.objects.create(
                title='Government Approved',
                description='All generic medicines are approved by regulatory authorities (CDSCO in India) and meet the same quality standards as branded drugs.',
                icon='✅',
                order=3
            ),
            GenericBenefit.objects.create(
                title='Bioequivalent',
                description='Generic medicines are bioequivalent to branded versions, meaning they work in the same way and provide the same clinical benefit.',
                icon='⚗️',
                order=4
            ),
            GenericBenefit.objects.create(
                title='Widely Available',
                description='Generic medicines are readily available at most pharmacies and government health centers across India.',
                icon='🏥',
                order=5
            ),
        ]
        self.stdout.write(self.style.SUCCESS(f'Created {len(benefits)} generic benefits'))

        self.stdout.write('Creating pharmacies...')
        pharmacies = [
            Pharmacy.objects.create(name='Apollo Pharmacy', website_url='https://www.apollopharmacy.in'),
            Pharmacy.objects.create(name='MedPlus', website_url='https://www.medplusmart.com'),
            Pharmacy.objects.create(name='Netmeds', website_url='https://www.netmeds.com'),
            Pharmacy.objects.create(name='PharmEasy', website_url='https://www.pharmeasy.in'),
            Pharmacy.objects.create(name='1mg', website_url='https://www.1mg.com'),
            Pharmacy.objects.create(name='Jan Aushadhi Kendra', website_url='https://janaushadhi.gov.in'),
            Pharmacy.objects.create(name='Local Medical Store', website_url=''),
        ]
        self.stdout.write(self.style.SUCCESS(f'Created {len(pharmacies)} pharmacies'))

        self.stdout.write('Creating medicines with detailed information...')
        medicines_data = [
            # Paracetamol 500mg - Branded
            {
                'brand_name': 'Crocin',
                'composition': 'Paracetamol 500mg',
                'strength': '500mg',
                'manufacturer': 'GSK Pharmaceuticals',
                'medicine_type': 'branded',
                'description': 'Crocin is a trusted pain reliever and fever reducer.',
                'uses': 'Used for relief from headache, migraine, toothache, period pain, and fever.',
                'side_effects': 'Generally safe when taken as directed. Rare: allergic reactions, liver damage with overdose.',
                'base_price': 30.0
            },
            {
                'brand_name': 'Dolo 650',
                'composition': 'Paracetamol 500mg',
                'strength': '650mg',
                'manufacturer': 'Micro Labs',
                'medicine_type': 'branded',
                'description': 'Popular fever and pain relief medication.',
                'uses': 'Fever, headache, body ache, and pain relief.',
                'side_effects': 'Minimal side effects when used as prescribed.',
                'base_price': 28.0
            },
            # Paracetamol - Generic
            {
                'brand_name': 'Paracetamol (Generic)',
                'composition': 'Paracetamol 500mg',
                'strength': '500mg',
                'manufacturer': 'Various Generic Manufacturers',
                'medicine_type': 'generic',
                'description': 'Generic paracetamol offers the same effectiveness as branded versions at a fraction of the cost.',
                'uses': 'Pain relief, fever reduction, headache, body ache.',
                'side_effects': 'Same as branded versions - generally safe when used as directed.',
                'base_price': 8.0
            },
            
            # Ibuprofen 400mg - Branded
            {
                'brand_name': 'Brufen',
                'composition': 'Ibuprofen 400mg',
                'strength': '400mg',
                'manufacturer': 'Abbott India',
                'medicine_type': 'branded',
                'description': 'Non-steroidal anti-inflammatory drug (NSAID) for pain and inflammation.',
                'uses': 'Arthritis, muscle pain, dental pain, menstrual cramps, fever.',
                'side_effects': 'Stomach upset, nausea, heartburn. Take with food.',
                'base_price': 45.0
            },
            {
                'brand_name': 'Combiflam',
                'composition': 'Ibuprofen 400mg',
                'strength': '400mg',
                'manufacturer': 'Sanofi India',
                'medicine_type': 'branded',
                'description': 'Combination pain reliever with anti-inflammatory properties.',
                'uses': 'Fever, headache, toothache, muscle pain.',
                'side_effects': 'Stomach discomfort, dizziness.',
                'base_price': 42.0
            },
            # Ibuprofen - Generic
            {
                'brand_name': 'Ibuprofen (Generic)',
                'composition': 'Ibuprofen 400mg',
                'strength': '400mg',
                'manufacturer': 'Various Generic Manufacturers',
                'medicine_type': 'generic',
                'description': 'Generic ibuprofen provides the same anti-inflammatory and pain relief benefits.',
                'uses': 'Pain, inflammation, fever reduction.',
                'side_effects': 'Same as branded - take with food to minimize stomach upset.',
                'base_price': 12.0
            },
            
            # Omeprazole 20mg - Branded
            {
                'brand_name': 'Omez',
                'composition': 'Omeprazole 20mg',
                'strength': '20mg',
                'manufacturer': 'Dr. Reddy\'s Laboratories',
                'medicine_type': 'branded',
                'description': 'Proton pump inhibitor for acid reflux and ulcers.',
                'uses': 'GERD, acid reflux, stomach ulcers, heartburn.',
                'side_effects': 'Headache, nausea, diarrhea, stomach pain.',
                'base_price': 85.0
            },
            {
                'brand_name': 'Pantop',
                'composition': 'Omeprazole 20mg',
                'strength': '20mg',
                'manufacturer': 'Aristo Pharmaceuticals',
                'medicine_type': 'branded',
                'description': 'Reduces stomach acid production.',
                'uses': 'Gastric ulcers, acid reflux, GERD.',
                'side_effects': 'Generally well tolerated.',
                'base_price': 80.0
            },
            # Omeprazole - Generic
            {
                'brand_name': 'Omeprazole (Generic)',
                'composition': 'Omeprazole 20mg',
                'strength': '20mg',
                'manufacturer': 'Various Generic Manufacturers',
                'medicine_type': 'generic',
                'description': 'Generic omeprazole works identically to branded versions for acid control.',
                'uses': 'Acid reflux, GERD, ulcers.',
                'side_effects': 'Same as branded versions.',
                'base_price': 25.0
            },
            
            # Metformin 500mg - Branded
            {
                'brand_name': 'Glycomet',
                'composition': 'Metformin 500mg',
                'strength': '500mg',
                'manufacturer': 'USV Ltd',
                'medicine_type': 'branded',
                'description': 'First-line medication for type 2 diabetes.',
                'uses': 'Type 2 diabetes, PCOS, insulin resistance.',
                'side_effects': 'Nausea, diarrhea, stomach upset (usually temporary).',
                'base_price': 65.0
            },
            {
                'brand_name': 'Obimet',
                'composition': 'Metformin 500mg',
                'strength': '500mg',
                'manufacturer': 'Mankind Pharma',
                'medicine_type': 'branded',
                'description': 'Controls blood sugar levels in diabetes.',
                'uses': 'Type 2 diabetes management.',
                'side_effects': 'GI disturbances, take with meals.',
                'base_price': 60.0
            },
            # Metformin - Generic
            {
                'brand_name': 'Metformin (Generic)',
                'composition': 'Metformin 500mg',
                'strength': '500mg',
                'manufacturer': 'Various Generic Manufacturers',
                'medicine_type': 'generic',
                'description': 'Generic metformin is equally effective for diabetes management at lower cost.',
                'uses': 'Type 2 diabetes, blood sugar control.',
                'side_effects': 'Same as branded - GI side effects may occur initially.',
                'base_price': 18.0
            },
            
            # Atorvastatin 10mg - Branded
            {
                'brand_name': 'Atorva',
                'composition': 'Atorvastatin 10mg',
                'strength': '10mg',
                'manufacturer': 'Zydus Cadila',
                'medicine_type': 'branded',
                'description': 'Statin medication to lower cholesterol.',
                'uses': 'High cholesterol, cardiovascular disease prevention.',
                'side_effects': 'Muscle pain, liver enzyme changes, headache.',
                'base_price': 95.0
            },
            {
                'brand_name': 'Lipicure',
                'composition': 'Atorvastatin 10mg',
                'strength': '10mg',
                'manufacturer': 'Intas Pharmaceuticals',
                'medicine_type': 'branded',
                'description': 'Reduces bad cholesterol and triglycerides.',
                'uses': 'Hyperlipidemia, heart disease prevention.',
                'side_effects': 'Generally well tolerated.',
                'base_price': 90.0
            },
            # Atorvastatin - Generic
            {
                'brand_name': 'Atorvastatin (Generic)',
                'composition': 'Atorvastatin 10mg',
                'strength': '10mg',
                'manufacturer': 'Various Generic Manufacturers',
                'medicine_type': 'generic',
                'description': 'Generic atorvastatin provides the same cholesterol-lowering benefits.',
                'uses': 'High cholesterol, cardiovascular protection.',
                'side_effects': 'Same as branded versions.',
                'base_price': 28.0
            },
            
            # Amoxicillin 500mg - Branded
            {
                'brand_name': 'Novamox',
                'composition': 'Amoxicillin 500mg',
                'strength': '500mg',
                'manufacturer': 'Cipla',
                'medicine_type': 'branded',
                'description': 'Broad-spectrum antibiotic.',
                'uses': 'Bacterial infections, respiratory infections, UTI.',
                'side_effects': 'Diarrhea, nausea, allergic reactions.',
                'base_price': 75.0
            },
            {
                'brand_name': 'Mox',
                'composition': 'Amoxicillin 500mg',
                'strength': '500mg',
                'manufacturer': 'Ranbaxy',
                'medicine_type': 'branded',
                'description': 'Penicillin-type antibiotic.',
                'uses': 'Bacterial infections.',
                'side_effects': 'Allergic reactions possible.',
                'base_price': 70.0
            },
            # Amoxicillin - Generic
            {
                'brand_name': 'Amoxicillin (Generic)',
                'composition': 'Amoxicillin 500mg',
                'strength': '500mg',
                'manufacturer': 'Various Generic Manufacturers',
                'medicine_type': 'generic',
                'description': 'Generic amoxicillin is equally effective against bacterial infections.',
                'uses': 'Bacterial infections, respiratory tract infections.',
                'side_effects': 'Same as branded versions.',
                'base_price': 22.0
            },
            
            # Cetirizine 10mg - Branded
            {
                'brand_name': 'Alerid',
                'composition': 'Cetirizine 10mg',
                'strength': '10mg',
                'manufacturer': 'Cipla',
                'medicine_type': 'branded',
                'description': 'Antihistamine for allergies.',
                'uses': 'Allergic rhinitis, hay fever, urticaria, itching.',
                'side_effects': 'Drowsiness, dry mouth, fatigue.',
                'base_price': 55.0
            },
            # Cetirizine - Generic
            {
                'brand_name': 'Cetirizine (Generic)',
                'composition': 'Cetirizine 10mg',
                'strength': '10mg',
                'manufacturer': 'Various Generic Manufacturers',
                'medicine_type': 'generic',
                'description': 'Generic cetirizine provides the same allergy relief.',
                'uses': 'Allergies, hay fever, skin rashes.',
                'side_effects': 'Same as branded - may cause drowsiness.',
                'base_price': 15.0
            },
            
            # Azithromycin 500mg - Branded
            {
                'brand_name': 'Azithral',
                'composition': 'Azithromycin 500mg',
                'strength': '500mg',
                'manufacturer': 'Alembic Pharmaceuticals',
                'medicine_type': 'branded',
                'description': 'Macrolide antibiotic.',
                'uses': 'Respiratory infections, skin infections, STDs.',
                'side_effects': 'Nausea, diarrhea, stomach pain.',
                'base_price': 120.0
            },
            # Azithromycin - Generic
            {
                'brand_name': 'Azithromycin (Generic)',
                'composition': 'Azithromycin 500mg',
                'strength': '500mg',
                'manufacturer': 'Various Generic Manufacturers',
                'medicine_type': 'generic',
                'description': 'Generic azithromycin is equally effective for bacterial infections.',
                'uses': 'Bacterial infections, respiratory tract infections.',
                'side_effects': 'Same as branded versions.',
                'base_price': 35.0
            },
        ]
        
        medicines = []
        for med_data in medicines_data:
            base_price = med_data.pop('base_price')
            medicine = Medicine.objects.create(**med_data)
            medicine.base_price = base_price  # Store for price generation
            medicines.append(medicine)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(medicines)} medicines'))

        self.stdout.write('Creating price records...')
        price_count = 0
        
        for medicine in medicines:
            # Generic medicines available at Jan Aushadhi and local stores primarily
            if medicine.is_generic():
                selected_pharmacies = [p for p in pharmacies if 'Jan Aushadhi' in p.name or 'Local' in p.name]
                # Add 2-3 online pharmacies too
                selected_pharmacies += random.sample([p for p in pharmacies if p not in selected_pharmacies], 2)
            else:
                # Branded medicines at 4-6 pharmacies
                num_pharmacies = random.randint(4, 6)
                selected_pharmacies = random.sample(pharmacies, num_pharmacies)
            
            base_price = Decimal(medicine.base_price)
            
            for pharmacy in selected_pharmacies:
                # Generic medicines have less price variation
                if medicine.is_generic():
                    variation = Decimal(random.uniform(0.95, 1.10))
                else:
                    variation = Decimal(random.uniform(0.85, 1.25))
                
                price = (base_price * variation).quantize(Decimal('0.01'))
                
                # Determine price type
                if 'Jan Aushadhi' in pharmacy.name:
                    price_type = 'average'
                elif pharmacy.name in ['Apollo Pharmacy', 'MedPlus', 'Netmeds', 'PharmEasy', '1mg']:
                    price_type = 'online'
                else:
                    price_type = 'mrp'
                
                Price.objects.create(
                    medicine=medicine,
                    pharmacy=pharmacy,
                    price=price,
                    price_type=price_type
                )
                price_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {price_count} price records'))
        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))
        self.stdout.write(self.style.SUCCESS('✨ Generic alternatives are now available with detailed benefits!'))
