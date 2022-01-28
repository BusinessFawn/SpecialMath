import os
from datetime import datetime
from uuid import uuid4

from flask import Flask
MAX_SPECIAL_NUMBER_ENTRY = int(os.getenv('MAX_SPECIAL_NUMBER_ENTRY', '1000'))

# TODO: TechDebt: Place in constants package
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


# TODO: TechDebt: Move this func and utils package to stand alone to avoid duplication
def get_request_context() -> dict:
    request_time = datetime.utcnow()
    return {
        "request-id": uuid4(),
        "request-time": request_time.strftime(DATETIME_FORMAT)
    }


def internal_server_error(e):
    return {'context': get_request_context(), 'error': {'message': e.description,
                                                        'name': e.name.replace(' ', '')}}, e.code


def not_found_error(e):
    return {'context': get_request_context(), 'error': {'message': e.description,
                                                        'name': e.name.replace(' ', '')}}, e.code


def bad_request_error(e):
    return {'context': get_request_context(), 'error': {'message': e.description,
                                                        'name': e.name.replace(' ', '')}}, e.code


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(404, not_found_error)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import specialmath
    app.register_blueprint(specialmath.bp)

    return app
