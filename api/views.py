import requests  # type: ignore
from django.core.cache import cache
from rest_framework.response import Response  # type: ignore
from rest_framework.decorators import api_view  # type: ignore
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

index_view = never_cache(TemplateView.as_view(template_name="index.html"))


def home(request):
    return HttpResponse("<h1>Welcome to the Pokémon API Backend</h1><p>Go to <a href='/api/cards/'>/api/cards/</a> to see card data.</p>")

POKEMON_API_URL = "https://api.pokemontcg.io/v2/cards"

@api_view(['GET'])
def get_pokemon_cards(request):
    cached_data = cache.get("pokemon_cards")

    if cached_data:
        return Response(cached_data)

    response = requests.get(POKEMON_API_URL)
    if response.status_code == 200:
        data = response.json()
        cache.set("pokemon_cards", data, timeout=60 * 60)  # Cache for 1 hour
        return Response(data)

    return Response({"error": "Failed to fetch data"}, status=response.status_code)
