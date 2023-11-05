#!/bin/bash

python manage.py migrate
gunicorn --bind :8080 --workers 3 vegetation.wsgi:application
