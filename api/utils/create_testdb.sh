#!/bin/bash

service mysql start
mysql --defaults-extra-file=/etc/mysql/my.cnf -u root  -e "drop database if exists api_unit;"
mysql --defaults-extra-file=/etc/mysql/my.cnf -u root  -e "create database api_unit;"
mysql --defaults-extra-file=/etc/mysql/my.cnf -u root  api_unit < /usr/local/api_flask/api/utils/schema.sql
