#!/bin/bash

service mysql start
mysql -u root -e "drop database if exists api_unit;"
mysql -u root -e "create database api_unit;"
mysql -u root api_unit < /usr/local/api_flask/api/utils/schema.sql
