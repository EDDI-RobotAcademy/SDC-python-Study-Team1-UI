class ConsoleUiState():

    def __init__(self):
        self.__sessionId = None
        self.__currentRoutingState = None
        self.__currentReadNumber = None

    def setCurrentRoutingState(self, currentState):
        self.__currentRoutingState = currentState

    def getCurrentRoutingState(self):
        return self.__currentRoutingState

    def setSessionId(self, userId):
        self.__sessionId = userId

    def getSessionId(self):
        return self.__sessionId

    def setCurrentReadNumber(self, responsedProductNumber):
        self.__currentReadNumber = responsedProductNumber

    def getCurrentReadNumber(self):
        return self.__currentReadNumber