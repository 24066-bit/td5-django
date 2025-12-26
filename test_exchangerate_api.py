import requests

# API gratuite pour les taux de change
url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(url, timeout=10)
    data = response.json()
    
    # Convertir pour avoir USD, EUR, CNY → MRU
    usd_to_mru = data['rates']['MRU']
    eur_to_mru = data['rates']['MRU'] / data['rates']['EUR']
    cny_to_mru = data['rates']['MRU'] / data['rates']['CNY']
    
    print(f"✅ Taux de change actuels vers MRU :")
    print(f"   1 USD = {usd_to_mru:.2f} MRU")
    print(f"   1 EUR = {eur_to_mru:.2f} MRU")
    print(f"   1 CNY = {cny_to_mru:.2f} MRU")
    print(f"\n📅 Date : {data['date']}")
    
except Exception as e:
    print(f"❌ Erreur: {e}")
