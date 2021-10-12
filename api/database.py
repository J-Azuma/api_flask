# データベース接続設定をする

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# SQLALchemyインスタンス宣言
db = SQLAlchemy()
# マシュマロインスタンス宣言
marshmallow = Marshmallow()

# db初期化
def init_db(app):
  db.init_app(app)