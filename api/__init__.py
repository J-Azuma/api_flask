## アプリケーションファクトリを定義
from flask import (Flask)

import sys
sys.path.append('..')


def create_app(test_config=None):
    app = Flask(__name__ , instance_relative_config=True)
    set_config(app, test_config=None)
    return app

# 設定を読み込み
def set_config(app, test_config=None ):

    # テストでない場合configファイルを読み込む
    if test_config is None:
        app.config.from_pyfile('..config.py', silent=True)
    else:
    # テストの場合、標準設定を読み込む
        app.config.from_mapping(test_config)

# アプリケーションインスタンスを定義
app = create_app()




