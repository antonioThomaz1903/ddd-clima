import sqlite3
from sqlite3 import Error


class Database:
    __instance = None
    connection = None

    @staticmethod
    def getConnection():
        if Database.__instance is None:
            Database()
        return Database.__instance.connection

    def __init__(self):
        if Database.__instance is not None:
            raise Exception("Erro")
        else:
            try:
                self.connection = sqlite3.connect("database.db")
                print(sqlite3.version)
                Database.__instance = self
            except Error as e:
                print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

createLocalizacaoGeograficaSql = """ CREATE TABLE IF NOT EXISTS localizacaoGeografica (
                                        ID INT PRIMARY KEY AUTOINCREMENT,
                                        latitude REAL,
                                        longitude REAL
                                    );"""

createDadosClimaticosSql = """CREATE TABLE IF NOT EXISTS dadosClimaticos (
                                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    temperatura REAL,
                                    umidade REAL,
                                    velocidadeVento REAL,
                                    pressaoAtmosferica REAL,
                                    tempo DATETIME,
                                    localizacaoGeografica_ID INTEGER,
                                    FOREIGN KEY (localizacaoGeografica_ID) REFERENCES localizacaoGeografica(ID)
                                );"""

if __name__ == '__main__':
    conn = Database.getConnection()
    create_table(conn, createLocalizacaoGeograficaSql)
    create_table(conn, createDadosClimaticosSql)
