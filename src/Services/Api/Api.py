from src.app import session_app, verify_jwt, generate_jwt
from src.Entities.Usuario import Usuario
from flask import request, jsonify, Blueprint
import datetime
from flask_restx import Api, Resource, fields, Namespace
from src.Services.ColetarDados import Session, coletarDados, getDadosClimaticos

api_bp = Blueprint('api', __name__)
api = Api(api_bp, version='1.0', title='Api Dados Climaticos',
          description='Api para coleta de dados climaticos')


ns_coletar_dados = Namespace('coletar_dados', description='Operações para coletar dados climáticos')
ns_users = Namespace('users', description='Operações para manipulação de usuários')
api.add_namespace(ns_coletar_dados)
api.add_namespace(ns_users)

user_model = ns_users.model('Usuario', {
    'username': fields.String(required=True, description='The user name'),
    'password': fields.String(required=True, description='The user password'),
    'email': fields.String(required=False, description='The user email')
})

login_model = ns_users.model('Login', {
    'username': fields.String(required=True, description='The user name'),
    'password': fields.String(required=True, description='The user password')
})

coletar_dado_model = ns_coletar_dados.model('DadoInput', {
    'lat': fields.Float(required=True, description='Latitude'),
    'lon': fields.Float(required=True, description='Longitude')
})

@ns_users.route('/register')
class Register(Resource):
    @ns_users.expect(user_model)
    def post(self):
        data = request.get_json()
        new_user = Usuario(username=data['username'], password=data['password'], email=data['email'])
        session_app.add(new_user)
        session_app.commit()
        return "Usuario created successfully", 201

@ns_users.route('/get_user/<int:user_id>')
class GetUser(Resource):
    def get(self, user_id):
        user = session_app.query(Usuario).get(user_id)
        if not user:
            return jsonify({'message': 'Usuario not found'}), 404
        return jsonify({'username': user.username, 'email': user.email})

@ns_users.route("/user/<int:user_id>")
class DeleteUser(Resource):
    def delete(self, user_id):
        user = session_app.query(Usuario).get(user_id)
        if not user:
            return jsonify({"message": "Usuário não encontrado"}), 404
        session_app.delete(user)
        session_app.commit()
        return jsonify({"message": "Usuário deletado com sucesso"})

@ns_users.route("/users")
class ListUsers(Resource):
    def get(self):
        users = session_app.query(Usuario).all()
        if not users:
            return jsonify({"message": "Não há usuários cadastrados"}), 404
        return jsonify([user.to_dict() for user in users])

@ns_coletar_dados.route("/coletar_dado")
class ColetarDado(Resource):
    @ns_coletar_dados.expect(coletar_dado_model)
    def post(self):
        data = request.get_json()
        latitude = data['lat']
        longitude = data['lon']
        dado = coletarDados(latitude, longitude)
        return jsonify(dado.to_dict())

@ns_coletar_dados.route('/get_dados', defaults={'lim': None, 'pag': 1})
@ns_coletar_dados.route('/get_dados/<int:lim>', defaults={'pag': 1})
@ns_coletar_dados.route('/get_dados/<int:lim>/<int:pag>')
class GetDados(Resource):
    def get(self, lim, pag):
        dados = getDadosClimaticos()
        if not dados:
            return jsonify({'message':'Não há dados cadastrados'}), 404
        if lim and pag:
            dados = dados[(lim * (pag-1)): (lim * pag) + pag-1]
        return jsonify([dado.to_dict() for dado in dados])
