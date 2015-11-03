import sqlite3
from flask import Flask, g


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from .views.api import api as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api')

    @app.before_request
    def before_request():
        g.db = sqlite3.connect(app.config['DATABASE_URI'])

    @app.teardown_request
    def teardown_request(exception):
        db = getattr(g, 'db', None)
        if db is not None:
            db.close()

    @app.errorhandler(404)
    def page_not_found(e):
        """Return a custom 404 error."""
        return 'Sorry, Nothing at this URL.', 404

    @app.errorhandler(500)
    def page_not_found(e):
        """Return a custom 500 error."""
        return 'Sorry, unexpected error: {}'.format(e), 500

    return app

