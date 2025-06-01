# Clothify
It is just my first web-site made from Django.


# Clothify

Clothify is a modern and minimalistic online clothing store built with Django. It supports product browsing, categories, reviews, cart management, and admin functionality.

## 🔧 Tech Stack

- **Backend**: Django 4+
- **Frontend**: HTML, CSS, Bootstrap (customized)
- **Database**: SQLite (development)
- **Authentication**: Django’s built-in user system
- **Hosting-ready**: Supports deployment on platforms like Heroku or Vercel (via Render)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/GlitchMage1/Clothify.git
cd Clothify


# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate


pip install -r requirements.txt


SECRET_KEY='your_secret_key'
DEBUG=True
SQL_ENGINE=django.db.backends.sqlite3
SQL_DATABASE=db.sqlite3


python manage.py makemigrations
python manage.py migrate


python manage.py createsuperuser


python manage.py runserver

Visit http://127.0.0.1:8000 in your browser.
