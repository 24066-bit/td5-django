from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ExchangeRate
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

def index(request):
    """Page d'accueil - Visualisation des taux de change"""
    rates = ExchangeRate.objects.all()[:730]  # 2 ans de données max
    
    context = {
        'rates': rates,
        'last_update': rates.first().date if rates.exists() else None
    }
    return render(request, 'rates/index.html', context)

def update_rates(request):
    """Mise à jour des taux depuis la BCM"""
    try:
        # URL de la BCM pour les taux de change
        url = "https://www.bcm.mr/Taux-de-change"
        
        # Pour l'instant, on crée des données de test
        # Le scraping réel sera ajouté ensuite
        today = datetime.now().date()
        currencies = ['USD', 'EUR', 'CNY']
        test_rates = {'USD': 36.5, 'EUR': 39.8, 'CNY': 5.2}
        
        for currency in currencies:
            ExchangeRate.objects.update_or_create(
                date=today,
                currency=currency,
                defaults={'rate': test_rates[currency], 'source': 'BCM'}
            )
        
        return JsonResponse({'status': 'success', 'message': 'Données mises à jour'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})