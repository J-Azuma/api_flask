## アプリケーションファクトリを定義
from flask import (Flask)
from api.database import db, marshmallow
from api.views import hello

def create_app():
    app = Flask(__name__ , instance_relative_config=True)

    # 標準設定ファイルを読み込み(標準設定とは？)
    app.config.from_object("setting")

    # 非公開設定ファイルを読み込み(サーバ起動用スクリプトで環境変数を設定)
    app.config.from_envvar("APP_CONFIG")

    # ルーティング設定読み込み
    app.register_blueprint(hello.bp)
    return app

    

# アプリケーションインスタンスを定義
app = create_app()




