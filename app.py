from flask import Flask
from flask_cors import CORS
from views import main_page
from extensions import db

db_conf = {
    'user': 'docker',
    'password': 'docker',
    'db': 'gis',
    'host': 'db',
    'port': '5432'
}


def create_app():
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    CORS(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{db_conf["user"]}:{db_conf["password"]}@' \
                                            f'{db_conf["host"]}:{db_conf["port"]}/{db_conf["db"]}'
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    with app.app_context():
        db.init_app(app)
        db.create_all()
        return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(main_page)
    return None


def fill_data():
    if not model_exists(Lines):
        db.create_all()


if __name__ == "__main__":
    # status = fill_data()
    app = create_app()
    app.run(host="0.0.0.0", debug=True)