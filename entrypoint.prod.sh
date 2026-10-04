#!/usr/bin/env bash

uv run python manage.py migrate --noinput &&
#uv run python manage.py collectstatic --noinput &

# Inicia o servidor com gunicorn via uv
exec uv run gunicorn kernel.wsgi:application --bind 0.0.0.0:8000

#gunicorn kernel.wsgi