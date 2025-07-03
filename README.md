# Recipe Management System

`A Django web application for managing recipes with user authentication, image upload, search, update, and delete functionality.

## Features

- User registration and login (with password encryption)
- Add recipes with name, description, and image
- Search recipes by name
- Update and delete recipes
- Admin panel for managing recipes
- Image upload and storage
- Clean, responsive UI

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd recipe-management-system
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

6. **Create a superuser (optional, for admin panel):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application:**
   - Home: http://127.0.0.1:8000/
   - Recipes: http://127.0.0.1:8000/recipes/
   - Login: http://127.0.0.1:8000/login/
   - Register: http://127.0.0.1:8000/registration/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
recipe-management-system/
├── core/
│   ├── core/            # Project settings
│   ├── vege/            # Recipe app (views, models, templates)
│   ├── home/            # Home app
│   ├── manage.py
│   └── requirements.txt
├── venv/                # Virtual environment
└── README.md
```

## Usage

1. Register a new user at `/registration/` or log in at `/login/`
2. Go to `/recipes/` to add, search, update, or delete recipes
3. Use the admin panel at `/admin/` to manage all recipes and users
4. Images are stored in the `media/recipe/` directory

## Technologies Used

- Django 5.2.3
- Python 3.10+
- SQLite (development)
- HTML/CSS

## Notes
- Passwords are securely hashed using Django's authentication system.
- Error and success messages are displayed using Django's messages framework.
- For production, configure proper static/media file serving and use a production-ready database. 