#!/bin/sh
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn todo_drf.wsgi:application --bind 0.0.0.0:8000 --timeout 300000
