# FastAPI_MVP

MVP **pédagogique** pour découvrir **FastAPI**.
Le repo contient **3 mini‑apps** indépendantes pour apprendre par étapes :

- `main.py` — démo **OAuth2 + JWT** (token d’accès, `/token`, `/users/me`, etc.).
- `upload.py` — **upload de fichiers** (form HTML, `UploadFile`, `File()`).
- `simple__OAuth2.py` — version **ultra simple** d’auth (Bearer token factice).

> ℹ️ **Installation simplifiée** : `fastapi[standard]` **inclut Uvicorn** et les dépendances utiles (multipart, etc.).
> https://fastapi.tiangolo.com/ — “Install with `pip install fastapi[standard]`”.

---

## 🚀 Lancer en local

### 1) Environnement Python
```bash
python -m venv .venv
# Windows (PowerShell)
# .\\.venv\\Scripts\\Activate.ps1
```

### 2) Dépendances
Méthode **simple** (Uvicorn inclus via l’extra standard) :
```bash
pip install "fastapi[standard]" PyJWT passlib[bcrypt]
```
- `fastapi[standard]` → installe FastAPI **+** `uvicorn[standard]` **+** dépendances optionnelles (dont `python-multipart`).
- `PyJWT` → pour encoder/décoder des JWT (utilisé dans `main.py`).
- `passlib[bcrypt]` → hash/verify mot de passe (utilisé dans `main.py`).

---

## ▶️ Démarrer chaque mini‑app

### A) App “OAuth2 + JWT” (fichier `main.py`)
```bash
uvicorn main:app --reload --port 8000
# Swagger: http://localhost:8000/docs
```
Endpoints principaux :
- `POST /token` → récupère un token **JWT** (utilise `fake_users_db` et `passlib`)
- `GET /users/me/` → profil de l’utilisateur **(protégé)** — nécessite `Authorization: Bearer <token>`
- `GET /users/me/items/` → items de l’utilisateur **(protégé)**

> 🔒 **Ne laisse pas `SECRET_KEY` en dur en prod.** Utilise une variable d’environnement ou un `.env` ignoré par Git.

### B) App “Upload de fichiers” (fichier `upload.py`)
```bash
uvicorn upload:app --reload --port 8001
# Swagger: http://localhost:8001/docs
```
- `GET /` → petit formulaire HTML d’upload
- `POST /uploadfile/` → reçoit un `UploadFile` (multipart/form-data)

### C) App “OAuth2 simplifié” (fichier `simple__OAuth2.py`)
```bash
uvicorn simple__OAuth2:app --reload --port 8002
# Swagger: http://localhost:8002/docs
```
- `POST /token` → retourne un “token” **factice** (pas de vraie sécurité)
- `GET /users/me` → route protégée par le “token” factice

---

## 🗂️ Structure actuelle
```
.
├─ main.py
├─ upload.py
├─ simple__OAuth2.py
└─ __pycache__/          # cache Python (peut être ignoré)
```

### .gitignore conseillé
```
__pycache__/
*.pyc
.venv/
.env
data/
```

---

## 🧠 Notes importantes
- **`fastapi[standard]`** inclut **Uvicorn** → pas besoin d’installer `uvicorn` séparément.
- `OAuth2PasswordBearer` **extrait** un token du header `Authorization`, mais ne **vérifie** pas sa validité.
  Dans `simple__OAuth2.py`, le “decode” est **factice**.
  Dans `main.py`, on **vérifie un JWT** signé (lib `PyJWT`) et on hash les mots de passe (`passlib[bcrypt]`).
- Les données utilisateurs sont dans `fake_users_db` (**exemple**). En réel, branche une vraie BDD + gestion de comptes.

---

## 🗺️ Prochaines étapes (idées)
- [ ] Ajouter un **README** détaillé par fichier (docstring en haut).
- [ ] Sauvegarder les fichiers uploadés dans `data/uploads/` et retourner une URL locale.
- [ ] Centraliser les trois mini‑apps dans un dossier `app/` avec des routers (`/auth`, `/upload`, etc.).
- [ ] Ajouter des **tests** (`pytest`) pour `/token` et un upload.
- [ ] Introduire **Pydantic v2** (Field, discriminated unions) pour la validation avancée.
