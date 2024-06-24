from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float

BaseUsuario = declarative_base()
class Usuario(BaseUsuario):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

    def __repr__(self):
            return '<Usuario %r>' % self.username

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }