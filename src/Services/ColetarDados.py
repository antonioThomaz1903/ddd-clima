import requests
import json
from src.Entities.LocalizacaoGeografica import LocalizacaoGeografica
from src.Entities.DadosClimaticos import DadosClimaticos
import datetime
from src.Persistence.DAO.DadosClimaticosDao import DadosClimaticosDao
from src.app import settings

API_KEY = settings.API_KEY

def coletarDados(localizacao):
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={localizacao.getLatitude()}&lon={localizacao.getLongitude()}&appid={API_KEY}")
    conteudo = json.loads(req.content)
    temp = conteudo['main']['temp']
    humidity = conteudo['main']['humidity']
    pressure = conteudo['main']['pressure']
    windSpeed = conteudo['wind']['speed']
    data = datetime.datetime.now()
    dadosClimaticos = DadosClimaticos(temp, humidity, windSpeed, pressure, data, localizacao)
    dadosClimaticosDao = DadosClimaticosDao()
    dadosClimaticosDao.insertDadosClimaticos(dadosClimaticos)
    return dadosClimaticos

if __name__ == "__main__":
    localizacao = LocalizacaoGeografica(4.23, 1.98)
    coletarDados(localizacao)