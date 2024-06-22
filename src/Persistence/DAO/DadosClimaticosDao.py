from src.Entities.DadosClimaticos import DadosClimaticos
from src.Persistence.Database import Database
from src.Persistence.DAO.LocalizacaoGeograficaDao import LocalizacaoGeograficaDao

class DadosClimaticosDao:
    def __init__(self):
        self.__cursor = Database.getConnection().cursor()
        self.__banco = Database.getConnection()

    def getDadosClimaticosById(self, id):
        self.__cursor.execute(f"SELECT * FROM dadosClimaticos WHERE ID = {id}")
        return self.__cursor.fetchall()

    def getDadosClimaticos(self):
        self.__cursor.execute(f"SELECT * FROM dadosClimaticos")
        dados = self.__cursor.fetchall()
        dados_response = []
        locDao = LocalizacaoGeograficaDao()
        for dado in dados:
            localizacao = locDao.getLocalizacaoGeograficaById(int(dado[6]))
            dadoClimatico = DadosClimaticos(dado[1], dado[2], dado[3], dado[4], dado[5], localizacao)
            dados_response.append(dadoClimatico)
        return dados_response

    def insertDadosClimaticos(self, dadosClimaticos):
        localizacaoGeograficaDao = LocalizacaoGeograficaDao()
        localizacaoGeograficaDao.insertLocalizacaoGeografica(dadosClimaticos.getLocalizacao())
        localizacao = localizacaoGeograficaDao.getLocalizacaoGeograficaByLatLon(dadosClimaticos.getLocalizacao().getLatitude(), dadosClimaticos.getLocalizacao().getLongitude())
        tempo = dadosClimaticos.getTempo()

        tempo_str = tempo.strftime('%Y-%m-%d %H:%M:%S')

        self.__cursor.execute("""INSERT INTO dadosClimaticos 
                                (temperatura, umidade, velocidadeVento, pressaoAtmosferica, tempo, localizacaoGeografica_ID)
                                VALUES (?, ?, ?, ?, ?)""",
                              (dadosClimaticos.getTemperatura(), dadosClimaticos.getUmidade(),
                               dadosClimaticos.getVelocidadeDoVento(), dadosClimaticos.getPressaoAtmosferica(),
                               tempo_str))
        self.__banco.commit()

