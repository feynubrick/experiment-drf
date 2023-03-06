#!/bin/bash

#python manage.py runserver $DJANGO_HOST:$DJANGO_PORT
gunicorn --bind $DJANGO_HOST:$DJANGO_PORT experiment.wsgi:application
