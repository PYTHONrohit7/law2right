# ⚖️ Law2Rights — Know the Law, Own Your Rights!

> A modern, comprehensive Legal Awareness Platform and CMS built with Django.

[![Django](https://img.shields.io/badge/Django-5.0-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205-purple)](https://getbootstrap.com/)

## 📖 About The Project

**Law2Rights** is a legal content management system designed to simplify complex legal concepts for common citizens and law students. It features a robust blog engine, legal dictionary, and exam preparation resources.

### ✨ Key Features
*   **Modern UI/UX:** Fully responsive design using **Bootstrap 5**.
*   **Interactive Content:** Dynamic blog cards, hover effects, and legal case summaries.
*   **Advanced Admin Panel:** Customized dashboard using **Django Jazzmin** for easy content management.
*   **Rich Text Editing:** Integrated **CKEditor** for writing beautiful legal articles.
*   **Search Functionality:** Global search to find acts, articles, and exam tips.
*   **Category Management:** Organized content (Indian Penal Code, Constitution, Career Guidance).

---

## 📸 Screenshots

| **Home Page** |
|:---:|
![Law2Rights Homepage](media/posts/Screenshot%202026-02-10%20153145.png)

---

## 🛠️ Tech Stack
*   **Backend:** Python, Django Framework
*   **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
*   **Database:** SQLite (Development) / PostgreSQL (Production ready)
*   **Utilities:** Pillow (Image handling), Django Crispy Forms

---

## 🚀 Quick Start Guide (Windows)

Follow these steps to set up the project locally on your machine.

### 1. Clone the Repository
```powershell
git clone https://github.com/PYTHONrohit7/law2right.git
cd law2right


### 2. Create & Activate Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
code
Powershell
# Create the environment
python -m venv .venv

# Activate it (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
### 3. Install Dependencies
code
Powershell
pip install -r requirements.txt
### 4. Database Setup
Apply migrations to create the database schema and create an admin user.
code
Powershell
python manage.py migrate

# Create the Superuser (Admin)
python manage.py createsuperuser
### 5. (Optional) Seed Initial Data
If you have a custom script to populate categories:
code
Powershell
python manage.py seed_categories
### 6. Run the Server
code
Powershell
python manage.py runserver
Visit http://127.0.0.1:8000/ to view the site.
Visit http://127.0.0.1:8000/admin/ to access the backend.
### 📂 Project Structure
code
Text
Law2Rights/
├── core/                 # Core application logic
├── law2rights/           # Project settings and configuration
├── media/                # User uploaded images (posts, thumbnails)
├── static/               # CSS, JS, and static images
├── templates/            # HTML Templates
├── db.sqlite3            # Database file
├── manage.py             # Django command-line utility
└── requirements.txt      # Project dependencies
### 🤝 Contributing
Contributions are welcome!
Fork the project.
Create your Feature Branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the Branch (git push origin feature/AmazingFeature).
Open a Pull Request.
