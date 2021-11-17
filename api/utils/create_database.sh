#!/bin/bash
###
# データベースとテーブルを作成します
###
service mysql start
mysql -u root < /usr/local/api_flask/api/utils/create_database.sql
mysql -u root api < /usr/local/api_flask/api/utils/schema.sql