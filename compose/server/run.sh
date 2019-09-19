#!/bin/bash

exec gunicorn -b 0.0.0.0:5000 -w 1 --threads 2 --log-level info wsgi:app