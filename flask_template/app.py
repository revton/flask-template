from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "chave_secreta_que_nao_esta_secreta"

    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)

    @app.route("/")
    def index():
        return "<html><body>Teste</body></html>"

    return app
