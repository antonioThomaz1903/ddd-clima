from src.Entities.LocalizacaoGeografica import LocalizacaoGeografica
from src.Persistence.Database import Database


class LocalizacaoGeograficaDao:
    def __init__(self):
        self.__cursor = Database.getConnection().cursor()
        self.__banco = Database.getConnection()

    def getLocalizacaoGeograficaById(self, id):
        self.__cursor.execute(f"SELECT * FROM localizacaoGeografica WHERE ID = ?;", id)
        return self.__cursor.fetchall()


    def insertLocalizacaoGeografica(self, localizacao):
        lat = localizacao.getLatitude()
        lon = localizacao.getLongitude()
        params = (lat, lon)
        self.__cursor.execute(f"INSERT INTO localizacaoGeografica (latitude, longitude) VALUES (?, ?);", params)
        self.__banco.commit()

    def getLocalizacaoGeograficaByLatLon(self, lat, lon):
        params = (lat, lon)
        self.__cursor.execute(f"SELECT * FROM localizacaoGeografica WHERE latitude = ? AND longitude = ?;", params)
        return self.__cursor.fetchall()