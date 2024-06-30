from dynaconf import FlaskDynaconf
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from src.Entities import BaseUsuario
from sqlalchemy.orm import sessionmaker
from flask_restx import Api, Resource, fields, Namespace
from src.Entities.DadosClimaticos import BaseClimatico

from src.Services.ColetarDados import getDadosClimaticos, coletarDados

app = Flask(__name__)

api = Api(app, version='1.0', title='Api Dados Climaticos',
          description='Api para coleta de dados climaticos')

API_KEY = '1cb7b2c2d9c6feb1e037ecfd4a42a887'
engine = create_engine('sqlite:///climate_data.db')
BaseUsuario.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

coletar_dado_model = api.model('DadoInput', {
    'lat': fields.Float(required=True, description='Latitude'),
    'lon': fields.Float(required=True, description='Longitude')
})

@api.route("/coletar_dado")
class ColetarDado(Resource):
    @api.expect(coletar_dado_model)
    def post(self):
        data = request.get_json()
        latitude = data['lat']
        longitude = data['lon']
        dado = coletarDados(latitude, longitude)
        return jsonify(dado.to_dict())

@api.route('/get_dados', defaults={'lim': None, 'pag': 1})
@api.route('/get_dados/<int:lim>', defaults={'pag': 1})
@api.route('/get_dados/<int:lim>/<int:pag>')
class GetDados(Resource):
    def get(self, lim, pag):
        dados = getDadosClimaticos()
        if not dados:
            return jsonify({'message':'Não há dados cadastrados'}), 404
        if lim and pag:
            dados = dados[(lim * (pag-1)): (lim * pag) + pag-1]
        return jsonify([dado.to_dict() for dado in dados])

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5001)