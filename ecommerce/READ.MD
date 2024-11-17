# E-Commerce Project

## Setup Instructions
1. Clone the repository.
2. Navigate to the project directory:
   ```bash
   cd ecommerce_project
python -m venv venv

venv\Scripts\activate     # For Windows
pip install django
python manage.py makemigrations
python manage.py migrate
## runnig the project
python manage.py runserver

Access the admin panel at http://127.0.0.1:8000/admin.