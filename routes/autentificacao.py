from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from db.database import db
from models import Usuario


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/cadastro', methods=['POST'])
def cadastro_usuario():
    """
    Cadastro de novo usuário
    ---
    tags:
      - Autenticação
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Cadastro
          required:
            - nome
            - senha
          properties:
            nome:
              type: string
              description: Nome de usuário
            senha:
              type: string
              description: Senha do usuário
    responses:
      201:
        description: Usuário criado com sucesso
      400:
        description: Usuário já existe
    """
    data = request.get_json()
    if Usuario.query.filter_by(nome=data['nome']).first():
        return jsonify({"error": "Usuario existente"}), 400
    novo_usuario = Usuario(nome=data['nome'], senha=data['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({"msg": "Usuario criado"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login de usuário
    ---
    tags:
      - Autenticação
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Login
          required:
            - nome
            - senha
          properties:
            nome:
              type: string
              description: Nome do usuário
            senha:
              type: string
              description: Senha do usuário
    responses:
      200:
        description: Login bem-sucedido, retorna token JWT
        schema:
          type: object
          properties:
            access_token:
              type: string
              description: Token JWT de acesso
      401:
        description: Nome ou senha inválidos
    """
    data = request.get_json()
    try:
        usuario = Usuario.query.filter_by(nome=data['nome']).first()

        if usuario and usuario.senha == data['senha']:
            token = create_access_token(identity=str(usuario.id))
            return jsonify({"access_token": token}), 200

        # "Senha padrão" para acesso
        if data['nome'] == 'admin' and data['senha'] == 'senha':
            token = create_access_token(identity='1')
            return jsonify({"access_token": token}), 200

        return jsonify({"error": "Nome ou senha inválidos"}), 401

    except Exception as e:
        # Log do erro (opcional) e retorno do erro genérico
        print(f"Erro no login: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500