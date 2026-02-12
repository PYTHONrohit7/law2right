# ⚖️ Law2Rights — Know the Law, Own Your Rights!

> A modern, comprehensive Legal Awareness Platform and CMS built with Django.

[![Django](https://img.shields.io/badge/Django-5.0-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205-purple)](https://getbootstrap.com/)

## 📖 About The Project

**Law2Rights** is a legal content management system designed to simplify complex legal concepts for common citizens and law students. It features a robust blog engine, legal dictionary, and exam preparation resources.

### ✨ Key Features
* **Modern UI/UX:** Fully responsive design using **Bootstrap 5**.
* **Interactive Content:** Dynamic blog cards, hover effects, and legal case summaries.
* **Advanced Admin Panel:** Customized dashboard using **Django Jazzmin** for easy content management.
* **Rich Text Editing:** Integrated **CKEditor** for writing beautiful legal articles.
* **Search Functionality:** Global search to find acts, articles, and exam tips.
* **Category Management:** Organized content (Indian Penal Code, Constitution, Career Guidance).

---

## 📸 Screenshots

| **Home Page** |
|:---:|
![Law2Rights Homepage](media/posts/Screenshot%202026-02-10%20153145.png)

---

## 🛠️ Tech Stack
* **Backend:** Python, Django Framework
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Utilities:** Pillow (Image handling), Django Crispy Forms

---

## 🚀 Quick Start Guide (Windows)

Follow these steps to set up the project locally on your machine.

### 1. Clone the Repository
Open your terminal or command prompt and run:

```bash
git clone https://github.com/PYTHONrohit7/law2right.git
cd law2right
```

### 2. Create & Activate Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies and keep your system clean.

For Windows (PowerShell):

```powershell
# Create the environment
python -m venv .venv

# Activate it
.\.venv\Scripts\Activate.ps1
```

(Note: If you get a permission error, run `Set-ExecutionPolicy Unrestricted -Scope Process` first)

### 3. Install Dependencies
Install all required Python packages listed in the requirements file.

```powershell
pip install -r requirements.txt
```

### 4. Database Setup
Initialize the database and create an administrator account.

```powershell
# Apply migrations to create database tables
python manage.py migrate

# Create the Superuser (Admin)
python manage.py createsuperuser
```

### 5. (Optional) Seed Initial Data
If you have the custom script to populate categories automatically:

```powershell
python manage.py seed_categories
```

### 6. Run the Server
Start the development server.

```powershell
python manage.py runserver
```

- View Website: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin Dashboard: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📂 Project Structure

```
Law2Rights/
├── core/                 # Core application logic (Views, Models)
├── law2rights/           # Project settings and configuration
├── media/                # User uploaded images (posts, thumbnails)
├── static/               # CSS, JS, and static images
├── templates/            # HTML Templates
├── db.sqlite3            # Database file
├── manage.py             # Django command-line utility
└── requirements.txt      # Project dependencies
```

---

## 🤝 Contributing

1. Fork the project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.
