from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.webscraping import EmbrapaConsulta


consulta_bp = Blueprint('consulta', __name__)


@consulta_bp.route('/consulta', methods=['GET'])
@jwt_required()
def get_items():
    """
    Consulta dados da Embrapa
    ---
    tags:
      - Consulta
    security:
      - BearerAuth: []
    parameters:
      - name: ano
        in: query
        type: integer
        required: true
        description: Ano da consulta
      - name: opcao
        in: query
        type: integer
        required: true
        description: Opção do menu principal
      - name: subopcao
        in: query
        type: integer
        required: true
        description: Subopção selecionada
    responses:
      200:
        description: Consulta realizada com sucesso
        schema:
          type: object
          example: {"resultado": "dados aqui"}
      401:
        description: Requisição não autorizada (token ausente ou inválido)
      400:
        description: Parâmetros inválidos
    """
    current_user_id = get_jwt_identity()

    ano = int(request.args.get('ano'))
    opcao = int(request.args.get('opcao'))
    subopcao = int(request.args.get('subopcao'))

    embrapa_consulta = EmbrapaConsulta(ano, opcao, subopcao)
    resultado_json = embrapa_consulta.consultar_api()
    return jsonify(resultado_json)