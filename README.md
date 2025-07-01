# Recipe Management System

A Django web application for managing recipes with image upload functionality.

## Features

- Add recipes with name, description, and image
- Admin panel for managing recipes
- Image upload and storage
- Clean, responsive UI

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd recipe
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   cd core
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application:**
   - Main app: http://127.0.0.1:8000/
   - Recipes: http://127.0.0.1:8000/recipes/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
recipe/
├── core/                 # Django project root
│   ├── core/            # Project settings
│   ├── vege/            # Recipe app
│   ├── home/            # Home app
│   ├── manage.py
│   └── requirements.txt
├── venv/                # Virtual environment
└── README.md
```

## Usage

1. Go to `/recipes/` to add new recipes
2. Use the admin panel at `/admin/` to manage all recipes
3. Images are stored in the `media/recipe/` directory

## Technologies Used

- Django 5.2.3
- Python 3.10
- SQLite (development)
- HTML/CSS 