#!/bin/bash
###
# テスト用のデータベースとテーブルを作成します
###
service mysql start
mysql --defaults-extra-file=/etc/mysql/my.cnf -u root  < /usr/local/api_flask/api/utils/create_database.sql
mysql --defaults-extra-file=/etc/mysql/my.cnf -u root  api < /usr/local/api_flask/api/utils/schema.sql