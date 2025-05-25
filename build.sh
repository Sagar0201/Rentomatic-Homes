#!/bin/bash

# Script exit होईल error आले तर
set -o errexit

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Making migrations..."
python manage.py makemigrations

echo "Applying migrations to database..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"
