from django.contrib import admin
from .models import Medicine, Pharmacy, Price, GenericBenefit


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'composition', 'strength', 'manufacturer', 'medicine_type', 'created_at']
    search_fields = ['brand_name', 'composition', 'manufacturer']
    list_filter = ['manufacturer', 'medicine_type', 'created_at']
    ordering = ['brand_name']
    fieldsets = (
        ('Basic Information', {
            'fields': ('brand_name', 'composition', 'strength', 'manufacturer', 'medicine_type')
        }),
        ('Detailed Information', {
            'fields': ('description', 'uses', 'side_effects')
        }),
    )


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['name', 'website_url', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['medicine', 'pharmacy', 'price', 'price_type', 'last_updated']
    search_fields = ['medicine__brand_name', 'pharmacy__name']
    list_filter = ['pharmacy', 'price_type', 'last_updated']
    ordering = ['-last_updated']
    autocomplete_fields = ['medicine', 'pharmacy']


@admin.register(GenericBenefit)
class GenericBenefitAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'description']
    list_filter = ['is_active']
    ordering = ['order', 'title']
