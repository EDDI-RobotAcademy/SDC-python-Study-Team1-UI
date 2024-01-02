class Session:
    def __init__(self):
        self.__sessionId = None

    def setSessionId(self, userId):
        self.__sessionId = userId

    def getSessionId(self):
        return self.__sessionId
