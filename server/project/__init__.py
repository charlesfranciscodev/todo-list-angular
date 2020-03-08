import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# instantiate the db
db = SQLAlchemy()

cors = CORS(expose_headers="Authorization")


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    cors.init_app(app)

    # import here to prevent circular import(s)
    from project.api.todo_routes import todo_blueprint
    from project.api.user_routes import user_blueprint
    from project.api.test_routes import test_blueprint

    # register blueprints
    app.register_blueprint(todo_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(test_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
