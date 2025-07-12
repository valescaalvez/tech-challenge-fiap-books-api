from flask_jwt_extended import JWTManager



def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    
    Swagger(app)
    JWTManager(app)

    from .routes import bp # Principal
    from .auth_routes import auth_bp #autenticação
    

    app.register_blueprint(bp) # Registra as rotas da API principal
    app.register_blueprint(auth_bp) # Registra as rotas de autenticação
    return app
