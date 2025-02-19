#!/bin/sh

# Start cron
cron

# Start Gunicorn
exec gunicorn "app:create_app()" --bind 0.0.0.0:10000 --workers 2
