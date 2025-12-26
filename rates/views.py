from django.shortcuts import render
from django.http import JsonResponse
from .models import ExchangeRate
from datetime import datetime
import requests

def index(request):
    """Page d'accueil - Visualisation des taux de change"""
    rates = ExchangeRate.objects.all()[:730]  # 2 ans de données max
    
    context = {
        'rates': rates,
        'last_update': rates.first().date if rates.exists() else None
    }
    return render(request, 'rates/index.html', context)

def update_rates(request):
    """Récupérer les vrais taux depuis l'API"""
    try:
        # API gratuite pour les taux de change
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # Calculer les taux vers MRU
        today = datetime.now().date()
        
        rates_data = {
            'USD': data['rates']['MRU'],
            'EUR': data['rates']['MRU'] / data['rates']['EUR'],
            'CNY': data['rates']['MRU'] / data['rates']['CNY']
        }
        
        # Sauvegarder dans la base de données
        for currency, rate in rates_data.items():
            ExchangeRate.objects.update_or_create(
                date=today,
                currency=currency,
                defaults={'rate': round(rate, 4), 'source': 'API ExchangeRate'}
            )
        
        return JsonResponse({
            'status': 'success',
            'message': f'Taux mis à jour : USD={rates_data["USD"]:.2f}, EUR={rates_data["EUR"]:.2f}, CNY={rates_data["CNY"]:.2f} MRU',
            'date': str(today)
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Erreur lors de la récupération des taux : {str(e)}'
        }, status=500)
