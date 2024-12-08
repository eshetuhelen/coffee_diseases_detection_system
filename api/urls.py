from django.urls import path
from .views import CoffeeLeafImageListView, home

urlpatterns = [
    path('', home, name='home'),  # Standalone home view for API root
    path('images/', CoffeeLeafImageListView.as_view(), name='image-list'),  # API for coffee leaf images
]
