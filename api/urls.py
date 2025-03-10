from django.urls import path
from .views import get_pokemon_cards, home

urlpatterns = [
    path('', home, name='home'),  # Root path
    path('cards/', get_pokemon_cards, name='get_pokemon_cards'),
]
