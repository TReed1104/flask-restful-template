#!/bin/sh
exec gunicorn --bind 0.0.0.0:5000 --chdir /usr/src/app template:app