#!/bin/sh
set -eo pipefail

WORKERS=${WORKERS:-1}
ACCESS_LOG=${ACCESS_LOG:--}
ERROR_LOG=${ERROR_LOG:--}

# Initialize database
python app.py

# Start SQLi1
echo "Starting SQLi1"
exec gunicorn 'app:app' \
    --bind '0.0.0.0:8000' \
    --workers $WORKERS \
    --access-logfile "$ACCESS_LOG" \
    --error-logfile "$ERROR_LOG"
