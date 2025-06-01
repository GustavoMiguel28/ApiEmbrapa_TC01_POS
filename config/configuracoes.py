class Config:
    SECRET_KEY = 'sua_chave_secreta'
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'API Embrapa',
        'uiversion': 3
    }
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'sua_chave_jwt_secreta'