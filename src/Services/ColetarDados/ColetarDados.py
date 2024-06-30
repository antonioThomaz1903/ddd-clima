import requests
import json
from src.Entities.DadosClimaticos import DadosClimaticos
import datetime
from src.app import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float
from src.Services.ColetarDados.app import API_KEY, session

def coletarDados(lat, lon):
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
    conteudo = json.loads(req.content)
    temp = conteudo['main']['temp']
    humidity = conteudo['main']['humidity']
    pressure = conteudo['main']['pressure']
    windSpeed = conteudo['wind']['speed']
    data = datetime.datetime.now()
    dadosClimaticos = DadosClimaticos(temp, humidity, windSpeed, pressure, data, lat, lon)
    session.add(dadosClimaticos)
    session.commit()
    return dadosClimaticos

def getDadosClimaticos():
    dadosClimaticos = []
    for dado in session.query(DadosClimaticos).all():
        dadosClimaticos.append(dado)
    return dadosClimaticos
