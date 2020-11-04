#!/bin/bash
set -e

exec uwsgi -b 32768 \
     --http 0.0.0.0:5000 \
     --wsgi-file /app/dictionary.py \
     --callable app
