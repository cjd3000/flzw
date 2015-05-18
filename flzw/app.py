from flask import Flask

from .views import ctl


def get_app():
    app = Flask(__name__)
    app.register_blueprint(ctl.mod)

    @app.route('/')
    def hi():
        return "hello"

    return app
