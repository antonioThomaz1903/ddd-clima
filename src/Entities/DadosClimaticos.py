class DadosClimaticos:
    id = None
    def __init__(self, temperatura, umidade, velocidadeDoVento, pressaoAtmosferica, tempo, localizacao):
        self.__temperatura = temperatura
        self.__umidade = umidade
        self.__velocidadeDoVento = velocidadeDoVento
        self.__pressaoAtmosferica = pressaoAtmosferica
        self.__tempo = tempo
        self.__localizacao = localizacao

    def getTempo(self):
        return self.__tempo

    def setTempo(self, tempo):
        self.__tempo = tempo

    def getUmidade(self):
        return self.__umidade

    def setUmidade(self, umidade):
        self.__umidade = umidade

    def getVelocidadeDoVento(self):
        return self.__velocidadeDoVento

    def setVelocidadeDoVento(self, velocidade):
        self.__velocidadeDoVento = velocidade

    def getPressaoAtmosferica(self):
        return self.__pressaoAtmosferica

    def setPressaoAtmosferica(self, pressaoAtmosferica):
        self.__pressaoAtmosferica = pressaoAtmosferica

    def getLocalizacao(self):
        return self.__localizacao

    def setLocalizacao(self, localizacao):
        self.__localizacao = localizacao

    def getTemperatura(self):
        return self.__temperatura

    def setTemperatura(self, temperatura):
        self.__temperatura = temperatura