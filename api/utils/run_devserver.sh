#!/bin/bash

service mysql start
export FLASK_APP=api
export FLASK_ENV=dev
export APP_CONFIG=/usr/local/api_flask/instance/config/development.py
flask run
