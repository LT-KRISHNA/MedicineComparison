from django.db import models
from django.core.exceptions import ValidationError


class Medicine(models.Model):
    brand_name = models.CharField(max_length=200, db_index=True)
    composition = models.CharField(max_length=500, db_index=True)
    strength = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        if not self.brand_name or not self.brand_name.strip():
            raise ValidationError({'brand_name': 'Brand name cannot be empty'})
        if not self.composition or not self.composition.strip():
            raise ValidationError({'composition': 'Composition cannot be empty'})
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.brand_name} ({self.composition})"


class Pharmacy(models.Model):
    name = models.CharField(max_length=200, unique=True)
    website_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Pharmacies'
    
    def clean(self):
        if not self.name or not self.name.strip():
            raise ValidationError({'name': 'Pharmacy name cannot be empty'})
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Price(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='prices')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = [['medicine', 'pharmacy']]
        indexes = [
            models.Index(fields=['medicine', 'price']),
        ]
    
    def clean(self):
        if self.price is not None and self.price <= 0:
            raise ValidationError({'price': 'Price must be greater than zero'})
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.medicine.brand_name} at {self.pharmacy.name}: ₹{self.price}"
