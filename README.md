# Django PythonAnywhere Demo

A simple Django web application demonstrating deployment on PythonAnywhere hosting platform.

## Description

This is a minimal Django project that displays a "Hello, Django on PythonAnywhere!" message. It serves as a basic template for deploying Django applications to PythonAnywhere.

## Features

- Django 5.2 web framework
- SQLite database (default)
- Single page application with basic view
- PythonAnywhere deployment configuration

## Setup

### Prerequisites

- Python 3.x
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd django-pythonanywhere-demo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Open your browser and navigate to `http://127.0.0.1:8000/`

## Deployment

### PythonAnywhere Setup

1. **Upload your code:**
   - Upload this project to your PythonAnywhere account via the Files tab
   - Or clone directly using Git in a Bash console

2. **Create a virtual environment:**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 mysite-virtualenv
   pip install -r requirements.txt
   ```

3. **Configure the Web App:**
   - Go to the Web tab in your PythonAnywhere dashboard
   - Click "Add a new web app"
   - Choose "Manual configuration" and select Python 3.10
   - Set the source code directory to `/home/yourusername/django-pythonanywhere-demo`
   - Set the virtual environment to `/home/yourusername/.virtualenvs/mysite-virtualenv`

4. **Update WSGI configuration:**
   - Edit the WSGI configuration file (link in Web tab)
   - Point it to your Django project's WSGI file:
     ```python
     import sys
     path = '/home/yourusername/django-pythonanywhere-demo'
     if path not in sys.path:
         sys.path.insert(0, path)

     from mysite.wsgi import application
     ```

5. **Configure settings:**
   - Update `ALLOWED_HOSTS` in `settings.py` with your PythonAnywhere domain
   - Set `DEBUG = False` for production
   - Configure static files path

6. **Collect static files and migrate:**
   ```bash
   python manage.py collectstatic
   python manage.py migrate
   ```

7. **Reload the web app** from the Web tab

### Deployment Configuration

This project includes PythonAnywhere-ready settings:

- `ALLOWED_HOSTS` configured for PythonAnywhere domain
- Static files configuration included
- Production-ready settings available

## Project Structure

```
django-pythonanywhere-demo/
├── core/                 # Main application
│   ├── views.py         # View functions
│   ├── urls.py          # URL patterns
│   └── ...
├── mysite/              # Django project settings
│   ├── settings.py      # Configuration
│   └── ...
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## Requirements

- Django 5.2
- asgiref 3.8.1
- sqlparse 0.5.3