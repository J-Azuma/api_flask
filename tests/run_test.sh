#!/bin/bash
export APP_CONFIG=/usr/local/api_flask/instance/config/test.py 
export SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:Azuma_516@localhost/api_unit?charset=utf8
pytest