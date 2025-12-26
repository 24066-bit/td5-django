# Rapport TD5 - SSH et Docker Compose

## Informations de connexion
- **Serveur SSH** : 144.76.198.221
- **Port SSH** : 24222
- **Username** : etu24066
- **Port applicatif** : 25066 (matricule 24066 + 1000 car 24066 était occupé)

## Commandes SSH utilisées

### Connexion SSH
```bash
ssh -p 24222 etu24066@144.76.198.221
```

### Commandes initiales
```bash
whoami          # etu24066
hostname        # dlab
pwd             # /home/etu24066
mkdir -p td5
cd td5
```

### Vérification des outils
```bash
git --version          # git version 2.47.3
docker --version       # Docker version 29.1.3
docker compose version # v5.0.0
```

### Vérification du port
```bash
ss -ltn | grep -E ':(25066)\s' || echo "OK: port libre"
# Résultat : OK: port libre
```

## Commande SCP
```bash
scp -P 24222 td5-django-v2.tar.gz etu24066@144.76.198.221:~/td5/
```

## Sortie docker compose ps
```
NAME            IMAGE            COMMAND                  SERVICE   CREATED          STATUS          PORTS
td5_web_25066   td5-django-web   "python manage.py ru…"   web       47 seconds ago   Up 45 seconds   127.0.0.1:25066->8000/tcp
```

## Sortie curl
```bash
curl -I http://127.0.0.1:25066

HTTP/1.1 200 OK
Date: Fri, 26 Dec 2025 12:11:59 GMT
Server: WSGIServer/0.2 CPython/3.12.12
Content-Type: text/html; charset=utf-8
```

## Visualisation

L'application affiche les taux de change pour USD, EUR et CNY sur 2 ans.

- USD : 36.5000 MRU
- EUR : 39.8000 MRU
- CNY : 5.2000 MRU
- Source : BCM
- Dernière mise à jour : Dec. 26, 2025

## Tunnel SSH
```bash
ssh -p 24222 -L 8080:127.0.0.1:25066 etu24066@144.76.198.221
```

Accès via navigateur : http://localhost:8080

## Repository GitHub

https://github.com/24066-bit/td5-django
