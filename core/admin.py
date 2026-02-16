from django.contrib import admin
from .models import Medicine, Pharmacy, Price


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'composition', 'strength', 'manufacturer', 'created_at']
    search_fields = ['brand_name', 'composition', 'manufacturer']
    list_filter = ['manufacturer', 'created_at']
    ordering = ['brand_name']


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['name', 'website_url', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['medicine', 'pharmacy', 'price', 'last_updated']
    search_fields = ['medicine__brand_name', 'pharmacy__name']
    list_filter = ['pharmacy', 'last_updated']
    ordering = ['-last_updated']
    autocomplete_fields = ['medicine', 'pharmacy']
