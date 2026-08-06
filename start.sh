#!/usr/bin/env bash
# start.sh — orquestra o startup do viegas-lima-site no Render
#
# 1) Cria database 'vl_site' dentro do gag-bot-db (compartilhado, Render free)
# 2) Roda migrations
# 3) Sobe gunicorn

set -e

echo "[start.sh] === Viegas & Lima site startup ==="
echo "[start.sh] PG_HOST=$PG_HOST PG_PORT=$PG_PORT PG_USER=$PG_USER"
echo "[start.sh] $(date -u +%Y-%m-%dT%H:%M:%SZ)"

# 1. Setup database (idempotente)
echo "[start.sh] STEP 1/3: setup_db.py"
TARGET_DB=vl_site python setup_db.py

# 2. Migrations
echo "[start.sh] STEP 2/3: manage.py migrate"
export DATABASE_URL="postgresql://${PG_USER}:${PG_PASSWORD}@${PG_HOST}:${PG_PORT}/vl_site"
python manage.py migrate --noinput

# 3. Gunicorn (exec pra preservar PID)
echo "[start.sh] STEP 3/3: gunicorn"
exec gunicorn vl_website.wsgi:application \
    --workers=1 \
    --threads=4 \
    --timeout=120 \
    --graceful-timeout=60 \
    --access-logfile - \
    --error-logfile -
