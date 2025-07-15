from flask import Flask
from flask_jwt_extended import JWTManager
import os
from flasgger import Swagger
import importlib
import sys

def create_app():
    app = Flask(__name__)

    if os.getenv('TESTING') == 'True':
        app.config['DATA_PATH'] = os.getenv('DATA_PATH', 'data/books.csv')
    else:
        app.config['DATA_PATH'] = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../data/books.csv'
        )

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'fallback_secret_key')

    Swagger(app)
    JWTManager(app)

    from .auth_routes import auth_bp
    from .stats_routes import stats_bp
    from .ml_routes import ml_bp
    from .book_routes import book_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(stats_bp)
    app.register_blueprint(ml_bp)
    app.register_blueprint(book_bp)

    importlib.reload(importlib.import_module(__name__ + '.data_loader'))

    from .data_loader import DataLoader, data_loader as _old_loader

    new_loader = DataLoader(data_path=app.config['DATA_PATH'])

    app.data_loader = new_loader
    sys.modules[__name__ + '.data_loader'].data_loader = new_loader

    return app
