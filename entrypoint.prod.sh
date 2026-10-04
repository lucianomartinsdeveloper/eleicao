#!/usr/bin/env bash

uv run python manage.py migrate --noinput &&
uv run python manage.py collectstatic --noinput &

uv run python manage.py qcluster &

gunicorn core.wsgi