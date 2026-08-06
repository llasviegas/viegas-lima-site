#!/usr/bin/env bash
set -euxo pipefail

echo "=== start.sh BEGIN ==="
echo "PG_HOST=$PG_HOST PG_PORT=$PG_PORT PG_USER=$PG_USER"

# Step 1: setup database
echo "--- Step 1: setup_db.py ---"
TARGET_DB=vl_site python setup_db.py

# Step 2: migrations
echo "--- Step 2: migrate ---"
export DATABASE_URL="postgresql://${PG_USER}:${PG_PASSWORD}@${PG_HOST}:${PG_PORT}/vl_site"
python manage.py migrate --noinput

# Step 3: gunicorn
echo "--- Step 3: gunicorn ---"
exec gunicorn vl_website.wsgi:application --workers=1 --threads=4 --timeout=120 --graceful-timeout=60
