import requests
from bs4 import BeautifulSoup
from datetime import datetime
import urllib3

# Désactiver les warnings SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL de la BCM
url = "https://www.bcm.mr/Taux-de-change"

try:
    # Headers pour simuler un navigateur
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    # Récupérer la page (sans vérifier SSL)
    response = requests.get(url, headers=headers, verify=False, timeout=15)
    response.raise_for_status()
    
    print(f"✅ Connexion réussie! Status code: {response.status_code}")
    
    # Parser le HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Afficher le titre de la page
    print("Titre de la page:", soup.title.string if soup.title else "Pas de titre")
    
    # Chercher les tableaux
    tables = soup.find_all('table')
    print(f"\nNombre de tableaux trouvés: {len(tables)}")
    
    # Afficher le contenu des tableaux
    for i, table in enumerate(tables):
        print(f"\n=== Tableau {i+1} ===")
        rows = table.find_all('tr')
        for j, row in enumerate(rows[:10]):  # Afficher les 10 premières lignes
            cols = row.find_all(['td', 'th'])
            print(f"Ligne {j}: {[col.get_text(strip=True) for col in cols]}")
    
    # Sauvegarder le HTML pour analyse
    with open('bcm_page.html', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    print("\n✅ HTML sauvegardé dans bcm_page.html")
    
except Exception as e:
    print(f"❌ Erreur: {e}")
    import traceback
    traceback.print_exc()
