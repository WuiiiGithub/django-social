# django-social
## Introduction
This is a repository which while trying to develop a webpage using a python framework called Django. I tried to make a simple webpage which is like blog page. And didn't focus much on UI as its not for commercial purpose. I like something to contribute to the open source community. I like keeping few codes for free. So, I just thought let me post it so that anybody will find it helpfull and continue from here. Let's continue how to use this.
## Setup
You need these python3 packages wtih pip on your device to work with this.
- django
- django_crispy_forms
- crispy_bootstrap4
- django-bootstrap4
- whitenoise
- Pillow

These were the packages which I had to download while working on it. If you are a unix user and had already downloaded python and pip in your device then copy and paste this in terminal:
```
pip install django
django_crispy_forms
pip install crispy_bootstrap4
pip install django-bootstrap4
pip install whitenoise
pip install Pillow
```
## Essential Django Commands:

### Project Management:

- `django-admin startproject <project_name>`: Creates a new Django project structure.
- `python manage.py runserver`: Starts the development server locally for testing and debugging.
- `python manage.py createsuperuser`: Creates a superuser account for administration.
- `python manage.py collectstatic`: Collects static files from various app directories into a single location.
- `python manage.py startapp <app_name>`: Creates a new Django app within your project.
- `python manage.py check`: Runs various checks for potential errors or warnings in your project.
- `python manage.py help [command]`: Gets help on a specific command's usage.

### Database Management:

- `python manage.py makemigrations`: Creates migration files to reflect model changes in your database.
- `python manage.py migrate`: Applies pending migrations to your database.
- `python manage.py sqlmigrate <app_name> [migration_id]`: Generates raw SQL for a specific migration.
- `python manage.py shell`: Opens an interactive Python shell within your project environment.
- `python manage.py loaddata <fixture_file>`: Loads initial data from fixture files into your database.
- `python manage.py flush`: It deletes all the entries (data) from your tables, leaving the table structure (columns and names) intact.

### Data Management:

- `python manage.py dumpdata <app_name> [model_name] > <fixture_file>`: Creates fixture files from existing data.
- `python manage.py customcommand [args]`: Creates and runs custom management commands for specific tasks.
- `python manage.py clearsessions`: Removes all session data from the database.

### Development Tools:

- `python manage.py test [app_name] [test_pattern]`: Runs unit tests for your project or app.
- `python manage.py coverage`: Measures code coverage using Django's test runner.

### Deployment:

- `python manage.py gunicorn`: Starts your project using the Gunicorn web server (more suitable for production).
- `python manage.py collectstatic [--no-postprocess]`: Collects static files for deployment.
- `python manage.py compress`: Compresses static files for better performance.
- `python manage.py freeze > requirements.txt`: Creates a requirements.txt file listing project dependencies.
- `python manage.py startapp myapp --template=project_template`: Uses a custom project template for rapid development.

### Miscellaneous:

- `python manage.py startproject <project_name>`: Creates a new Django project in the current directory.
- `python manage.py startapp <app_name>`: Creates a new Django app in the current directory.
- `python manage.py runserver [port number]`: Starts the development server with a different address and port.
- `python manage.py runserver --settings=myproject.settings.dev`: Uses a specific settings file.
- `python manage.py shell --basic`: Starts a shell without loading models or apps.

# Conclusion
If you have a basic understanding of django then this might be very helpfull to you. If you are at the start and love making a site then you might need a tutorial to understand django and get some handson experience and then look at this repository.

Thank you for reading this
