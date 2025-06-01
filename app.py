from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from config.configuracoes import Config
from db.database import db
from models import Usuario
from routes import auth_bp, consulta_bp


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)
swagger = Swagger(app)

app.register_blueprint(auth_bp)
app.register_blueprint(consulta_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)