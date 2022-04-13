# Flaskクラスをimportする
from flask import Flask, current_app, g, render_template, request, url_for, redirect

# Flaskクラスをインスタンス化する
app = Flask(__name__)


# URLと実行する関数をマッピングする
@app.route("/")
def index():
    return "Hello, Flaskbook!"


@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    # Python 3.6から導入されたf-stringで文字列を定義
    return f"Hello, {name}!"


@app.route("/name/<name>")
def show_name(name):
    # 変数をテンプレートエンジンに渡す
    return render_template("index.html", name=name)


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=1
    print(url_for("show_name", name="ichiro", page="1"))

# ここで呼び出すとエラーになる
# print(current_app)

# アプリケーションコンテキストを取得してスタックへpushする
ctx = app.app_context()
ctx.push()

# current_appにアクセスが可能になる
print(current_app.name)
# >> apps.minimalapp.app

# グローバルなテンポラリ領域に値を設定する
g.connection = "connection"
print(g.connection)
# >> connection

with app.test_request_context("/users?updated=true"):
    # trueが出力される
    print(request.args.get("updated"))


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # form属性を使ってフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # メールを送る(最後に実装)

        # contactエンドポイントへリダイレクトする
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")
