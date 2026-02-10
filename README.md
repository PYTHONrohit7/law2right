Law2Rights
===========

A Django-based CMS for legal articles and news.

Quick start (Windows PowerShell):

1. Create and activate a virtualenv

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Make migrations, create superuser, seed categories

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_categories
```

3. Run server

```powershell
python manage.py runserver
```

Notes:
- Add `core` to `INSTALLED_APPS` (already added).
- Configure `MEDIA_ROOT` and serve media in development (settings already configured).
- Install `Pillow` to enable image uploads.
