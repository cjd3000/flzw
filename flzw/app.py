from flask import Flask, render_template

from .views import ctl


def get_app():
    app = Flask(__name__)
    app.register_blueprint(ctl.mod)

    @app.route('/')
    def root():
        return render_template('index.html')

    return app
