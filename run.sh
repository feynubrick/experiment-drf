#!/bin/bash

#gunicorn experiment.wsgi
python manage.py runserver $DJANGO_HOST:$DJANGO_PORT