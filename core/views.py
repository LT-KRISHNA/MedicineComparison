from django.shortcuts import render, redirect
from .models import Medicine
from .services import MedicineSearchService, PriceComparisonService, AlternativeFinderService
from .forms import MedicineSearchForm


def home(request):
    """
    Display the search homepage
    """
    form = MedicineSearchForm()
    return render(request, 'home.html', {'form': form})


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
