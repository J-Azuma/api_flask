## アプリケーションファクトリを定義
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, NOT_FOUND
from flask import (Flask, jsonify)
from api.database import db, init_db
from api.mail import init_mail
from api.presentationlayer.movie.movieview import MovieView
from api.presentationlayer.user.userview import UserView
from api.presentationlayer.shared.exception.exceptionhandler import BadRequestException, InternalServerException, NotFoundException

# from api.views.userView import UserView
from flask_jwt import JWT
# from api.views.auth import authenticate, identity

def create_app():
    app = Flask(__name__ , instance_relative_config=True)

    # 標準設定ファイルを読み込み(標準設定とは？)
    app.config.from_object("setting")

    # 非公開設定ファイルを読み込み(サーバ起動用スクリプトで環境変数を設定)
    app.config.from_envvar("APP_CONFIG")

    # 各種オブジェクトを初期化
    init_db(app)
    init_mail(app)
    # jwt = JWT(app, authenticate, identity)
    
    # ルーティング設定読み込み
    app.register_blueprint(UserView.user_route, url_prefix='/api/v1/users/')
    app.register_blueprint(MovieView.movie_route, url_prefix="/api/v1/movies/")
    
    # ExceptionHanlder
    app.register_error_handler(BAD_REQUEST, BadRequestException.error_response)
    app.register_error_handler(NOT_FOUND, NotFoundException.error_response)
    app.register_error_handler(INTERNAL_SERVER_ERROR, InternalServerException.error_response)
    
    return app

    

# アプリケーションインスタンスを定義
app = create_app()




