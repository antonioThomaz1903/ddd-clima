class LocalizacaoGeografica:
    id = None
    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    def getLatitude(self):
        return self.__latitude

    def setLatitude(self, latitude):
        self.__latitude = latitude

    def getLongitude(self):
        return self.__longitude

    def setLongitude(self, longitude):
        self.__longitude = longitude