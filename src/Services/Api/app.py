from src.Entities.Usuario import Usuario
from flask import request, jsonify, Blueprint, Flask
import datetime
from flask_restx import Api, Resource, fields, Namespace
from src.Services.ColetarDados import coletarDados, getDadosClimaticos
from src.Services.Newsletter import enviar_newsletter
import requests
from src.Services.ColetarDados import getDadosClimaticos, coletarDados

app = Flask(__name__)
api = Api(app, version='1.0', title='Api Gateway',
          description='Api Gateway')

def forward_request(service_url, path):
    url = f'{service_url}/{path}'
    response = requests.request(
        method=request.method,
        url=url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    return (response.content, response.status_code, response.headers.items())

@api.route('/coletarDados/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def service_a(path):
    return forward_request('http://localhost:5001', path)

@api.route('/newsletter/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def service_b(path):
    return forward_request('http://localhost:5002', path)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)