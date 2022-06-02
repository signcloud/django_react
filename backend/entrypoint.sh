#!/bin/sh
python manage.py makemigrations
python manage.py migrate
gunicorn todo_drf.wsgi:application --bind 0.0.0.0:8000 --timeout 300000
