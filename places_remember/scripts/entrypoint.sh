#!/bin/sh
python manage.py shell < scripts/connect.py
python manage.py migrate
gunicorn --bind :8000 places_remember.wsgi:application
exec "$@"