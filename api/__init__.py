## アプリケーションファクトリを定義
from flask import (Flask)
from api.database import db, init_db, marshmallow
from api.mail import init_mail
from api.set_jwt import init_jwt
from api.views import user,hello
from flask_mail import Mail

def create_app():
    app = Flask(__name__ , instance_relative_config=True)

    # 標準設定ファイルを読み込み(標準設定とは？)
    app.config.from_object("setting")

    # 非公開設定ファイルを読み込み(サーバ起動用スクリプトで環境変数を設定)
    app.config.from_envvar("APP_CONFIG")

    init_db(app)
    init_mail(app)
    init_jwt(app)
    # ルーティング設定読み込み
    app.register_blueprint(hello.bp)
    app.register_blueprint(user.user_route, url_prefix='/api/v1/users/')
    return app

    

# アプリケーションインスタンスを定義
app = create_app()




