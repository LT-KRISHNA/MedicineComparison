from typing import List
from django.db.models import QuerySet
from .models import Medicine, Price


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
        ).order_by('brand_name')[:50]


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


class AlternativeFinderService:
    @staticmethod
    def find_alternatives(medicine_id: int) -> List[dict]:
        """
        Find alternative medicines with same composition, excluding the original.
        Prioritizes generic alternatives and calculates savings.
        Returns: List of dicts with {
            'medicine': Medicine object,
            'lowest_price': Decimal,
            'pharmacy_name': str,
            'is_generic': bool,
            'savings_amount': Decimal,
            'savings_percentage': Decimal
        } sorted by lowest_price ascending
        """
        medicine = Medicine.objects.get(id=medicine_id)
        
        # Get the original medicine's lowest price for comparison
        original_lowest = medicine.prices.order_by('price').first()
        original_price = original_lowest.price if original_lowest else None
        
        # Find medicines with same composition, excluding current medicine
        alternatives = Medicine.objects.filter(
            composition=medicine.composition
        ).exclude(id=medicine_id)
        
        # For each alternative, get the lowest price
        results = []
        for alt in alternatives:
            lowest_price_record = alt.prices.select_related('pharmacy').order_by('price').first()
            
            if lowest_price_record:
                savings_amount = 0
                savings_percentage = 0
                
                if original_price:
                    savings_amount = original_price - lowest_price_record.price
                    if original_price > 0:
                        savings_percentage = (savings_amount / original_price) * 100
                
                results.append({
                    'medicine': alt,
                    'lowest_price': lowest_price_record.price,
                    'pharmacy_name': lowest_price_record.pharmacy.name,
                    'is_generic': alt.is_generic(),
                    'savings_amount': round(savings_amount, 2),
                    'savings_percentage': round(savings_percentage, 2)
                })
        
        # Sort: generics first, then by lowest price
        results.sort(key=lambda x: (not x['is_generic'], x['lowest_price']))
        
        return results
