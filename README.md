# fastapi_mvp

MVP **ultra simple** pour découvrir **FastAPI** 🐍  
Objectif : comprendre les routes, la validation et la doc auto **sans complexité** (pas de BDD ni Docker au départ).

## ✨ Fonctionnalités
- `GET /health` — ping de santé (`{"status":"ok"}`)
- `POST /process` — upload d’image (multipart) → renvoie des **métadonnées** (format, largeur, hauteur, taille) et **sauvegarde** le fichier en local
- **Swagger UI** auto à `/docs`

## 🧰 Stack
- **Python 3.11+**
- **FastAPI**
- **Uvicorn**
- **Pillow** (lecture basique d’images)
- **python-multipart** (upload)

## 🚀 Lancer en local

```bash
# 1) Cloner
git clone https://github.com/<ton-user>/fastapi_mvp.git
cd fastapi_mvp

# 2) Environnement
python -m venv .venv

# 3) Dépendances
pip install multipart passlib pyjwt

# 4) Lancer le serveur
uvicorn backend.app.main:app --reload --port 8000
