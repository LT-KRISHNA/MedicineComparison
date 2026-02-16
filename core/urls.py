from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('results/<int:medicine_id>/', views.results, name='results'),
]
