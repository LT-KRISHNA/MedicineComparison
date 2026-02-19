from django.db import models
from django.core.exceptions import ValidationError


class Medicine(models.Model):
    MEDICINE_TYPE_CHOICES = [
        ('branded', 'Branded'),
        ('generic', 'Generic'),
    ]
    
    brand_name = models.CharField(max_length=200, db_index=True)
    composition = models.CharField(max_length=500, db_index=True)
    strength = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=200)
    medicine_type = models.CharField(max_length=10, choices=MEDICINE_TYPE_CHOICES, default='branded')
    description = models.TextField(blank=True, null=True, help_text="General information about the medicine")
    uses = models.TextField(blank=True, null=True, help_text="Common uses of this medicine")
    side_effects = models.TextField(blank=True, null=True, help_text="Common side effects")
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
    
    def is_generic(self):
        return self.medicine_type == 'generic'


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
    PRICE_TYPE_CHOICES = [
        ('mrp', 'Maximum Retail Price'),
        ('average', 'Average Market Price'),
        ('online', 'Online Price'),
    ]
    
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='prices')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_type = models.CharField(max_length=10, choices=PRICE_TYPE_CHOICES, default='average')
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


class GenericBenefit(models.Model):
    """
    Stores information about benefits of choosing generic medicines
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, help_text="Icon name or emoji")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title
