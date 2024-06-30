from dynaconf import FlaskDynaconf
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from src.Entities import BaseUsuario
from sqlalchemy.orm import sessionmaker
from flask_restx import Api, Resource, fields, Namespace
from src.Entities.Usuario import Usuario
from src.Services.ColetarDados import getDadosClimaticos
from src.Services.Newsletter import enviar_newsletter

app = Flask(__name__)

api = Api(app, version='1.0', title='Api Newsletter',
          description='Api para envio de Newsletter')

engine = create_engine('sqlite:///user_data.db')
BaseUsuario.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

user_model = api.model('Usuario', {
    'username': fields.String(required=True, description='The user name'),
    'password': fields.String(required=True, description='The user password'),
    'email': fields.String(required=False, description='The user email')
})

login_model = api.model('Login', {
    'username': fields.String(required=True, description='The user name'),
    'password': fields.String(required=True, description='The user password')
})

@api.route('/enviar_newsletter')
class EnviarNewsletter(Resource):
    def post(self):
        response = enviar_newsletter()
        print(response)
        return response

@api.route('/register')
class Register(Resource):
    @api.expect(user_model)
    def post(self):
        data = request.get_json()
        new_user = Usuario(username=data['username'], password=data['password'], email=data['email'])
        session.add(new_user)
        session.commit()
        return "Usuario created successfully", 201

@api.route('/get_user/<int:user_id>')
class GetUser(Resource):
    def get(self, user_id):
        user = session.query(Usuario).get(user_id)
        if not user:
            return jsonify({'message': 'Usuario not found'}), 404
        return jsonify({'username': user.username, 'email': user.email})

@api.route("/user/<int:user_id>")
class DeleteUser(Resource):
    def delete(self, user_id):
        user = session.query(Usuario).get(user_id)
        if not user:
            return jsonify({"message": "Usuário não encontrado"}), 404
        session.delete(user)
        session.commit()
        return jsonify({"message": "Usuário deletado com sucesso"})

@api.route("/users")
class ListUsers(Resource):
    def get(self):
        users = session.query(Usuario).all()
        if not users:
            return jsonify({"message": "Não há usuários cadastrados"}), 404
        return jsonify([user.to_dict() for user in users])

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5002)