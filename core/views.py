from django.shortcuts import render, redirect
from .models import Medicine, GenericBenefit
from .services import MedicineSearchService, PriceComparisonService, AlternativeFinderService
from .forms import MedicineSearchForm


def home(request):
    """
    Display the search homepage
    """
    form = MedicineSearchForm()
    generic_benefits = GenericBenefit.objects.filter(is_active=True)
    return render(request, 'home.html', {'form': form, 'generic_benefits': generic_benefits})


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


def results(request, medicine_id):
    """
    Display price comparison and alternatives for a specific medicine
    """
    try:
        comparison_data = PriceComparisonService.get_price_comparison(medicine_id)
        alternatives = AlternativeFinderService.find_alternatives(medicine_id)
        generic_benefits = GenericBenefit.objects.filter(is_active=True)
        
        # Check if there are generic alternatives
        has_generic_alternatives = any(alt['is_generic'] for alt in alternatives)
        
        context = {
            'medicine': comparison_data['medicine'],
            'prices': comparison_data['prices'],
            'lowest_price': comparison_data['lowest_price'],
            'highest_price': comparison_data['highest_price'],
            'savings_percentage': comparison_data['savings_percentage'],
            'alternatives': alternatives,
            'generic_benefits': generic_benefits,
            'has_generic_alternatives': has_generic_alternatives,
        }
        
        return render(request, 'results.html', context)
    
    except Medicine.DoesNotExist:
        return redirect('home')
