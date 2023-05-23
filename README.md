# Docker Compose Django Restframework

## Setup

#### Open the Command prompt and type the following commands

    $ docker-compose build 

### To Create Django Project

    $ docker-compose run qr_faas_management /usr/local/bin/django-admin.py startproject qr_faas_management .

### To Create Django App

    $ docker-compose run qr_faas_management /usr/local/bin/django-admin.py startapp first_app

### Add Your App in project settings Intalled App

## Running project in development and Setup Admin Account

    $ docker-compose run qr_faas_management bash -c "python manage.py makemigrations  && python manage.py migrate && python manage.py createsuperuser --email admin@example.com --username admin"

### Run the Project

    $ docker-compose up