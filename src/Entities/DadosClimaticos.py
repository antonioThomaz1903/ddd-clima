from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float

Base = declarative_base()
class DadosClimaticos(Base):
    __tablename__ = 'dados_climaticos'
    id = Column(Integer, primary_key=True)
    temperatura = Column(Float, nullable=False)
    umidade = Column(Float, nullable=False)
    velocidade_do_vento = Column(Float, nullable=False)
    pressao_atmosferica = Column(Float, nullable=False)
    tempo = Column(String(100), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    def __init__(self, temperatura, umidade, velocidade_do_vento, pressao_atmosferica, tempo, latitude, longitude):
        self.temperatura = temperatura
        self.umidade = umidade
        self.velocidade_do_vento = velocidade_do_vento
        self.pressao_atmosferica = pressao_atmosferica
        self.tempo = tempo
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"<DadosClimaticos(id={self.id}, temperatura={self.temperatura}, umidade={self.umidade}, " \
               f"velocidade_do_vento={self.velocidade_do_vento}, pressao_atmosferica={self.pressao_atmosferica}, " \
               f"tempo='{self.tempo}', lat={self.latitude}, lon={self.longitude})>"

    def to_dict(self):
        return {
            'id': self.id,
            'temperatura': self.temperatura,
            'umidade': self.umidade,
            'velocidade_do_vento': self.velocidade_do_vento,
            'pressao_atmosferica': self.pressao_atmosferica,
            'tempo': self.tempo,
            'latitude': self.latitude,
            'longitude': self.longitude
        }