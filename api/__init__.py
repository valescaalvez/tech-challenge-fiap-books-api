from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] 
    
    Swagger(app)
    JWTManager(app)

    from .routes import bp
    app.register_blueprint(bp)
    return app
