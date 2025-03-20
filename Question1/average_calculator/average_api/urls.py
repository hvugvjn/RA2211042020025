from django.urls import path
from .views import calculate_average, home

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('api/calculate/', calculate_average, name='calculate_average'),
]
