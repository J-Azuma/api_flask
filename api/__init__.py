## アプリケーションファクトリを定義
from flask import (Flask)
import sys
sys.path.append('..')
from api.database import db, marshmallow
from api.views import hello

def create_app(test_config=None):
    app = Flask(__name__ , instance_relative_config=True)

    # 標準設定ファイルを読み込み(標準設定とは？)
    app.config.from_object("setting")

    # 非公開設定ファイルを読み込み(サーバ起動用スクリプトで環境変数を設定)
    app.config.from_envvar("APP_CONFIG")

    if test_config is not None:
        # テスト用設定を上書き
        app.config.from_mapping(test_config)

    # ルーティング設定読み込み
    app.register_blueprint(hello.bp)
    return app

    

# アプリケーションインスタンスを定義
app = create_app()




