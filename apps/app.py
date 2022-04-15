from flask import Flask


# create_app関数を作成する
def create_app():
    # Flaskインスタンスを生成
    app = Flask(__name__)

    # crudパッケージからviewsをimportする
    from apps.crud import views as crud_views

    # register_blueprintを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
