import requests
import json
from src.Entities.DadosClimaticos import DadosClimaticos, Base
import datetime
from src.app import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


API_KEY = settings.API_KEY

engine = create_engine(settings.DADOS_CLIMATICOS_DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

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
