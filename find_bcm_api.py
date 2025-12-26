import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URLs possibles de l'API BCM
possible_urls = [
    "https://www.bcm.mr/api/taux-de-change",
    "https://www.bcm.mr/api/exchange-rates",
    "https://www.bcm.mr/api/rates",
    "https://www.bcm.mr/taux-de-change.json",
    "https://www.bcm.mr/data/taux-de-change",
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Accept': 'application/json'
}

print("🔍 Recherche de l'API BCM...\n")

for url in possible_urls:
    try:
        print(f"Essai: {url}")
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ Trouvé! Status: {response.status_code}")
            print(f"Content-Type: {response.headers.get('Content-Type')}")
            
            # Essayer de parser en JSON
            try:
                data = response.json()
                print(f"📊 Données JSON:")
                print(json.dumps(data, indent=2, ensure_ascii=False)[:500])
                print("\n" + "="*50 + "\n")
            except:
                print(f"📄 Contenu (texte):")
                print(response.text[:500])
                print("\n" + "="*50 + "\n")
        else:
            print(f"❌ Status: {response.status_code}\n")
            
    except Exception as e:
        print(f"❌ Erreur: {e}\n")

print("\n💡 Astuce: Ouvrez https://www.bcm.mr/Taux-de-change dans votre navigateur")
print("   Puis ouvrez les DevTools (F12) → Onglet 'Network' → Cherchez les requêtes XHR/Fetch")
