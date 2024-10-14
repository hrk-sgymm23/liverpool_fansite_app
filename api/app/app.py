# MEMO: ex. __init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    with app.app_context():
        # ルートの登録
        from routes import register_routes
        register_routes(app)

    return app
