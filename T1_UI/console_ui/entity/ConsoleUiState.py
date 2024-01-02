class ConsoleUiState:

    def __init__(self):
        self.__currentRoutingState = 0
        self.__currentReadNumber = None

    def setCurrentRoutingState(self, currentState):
        self.__currentRoutingState = currentState

    def getCurrentRoutingState(self):
        return self.__currentRoutingState

    def setCurrentReadNumber(self, responsedProductNumber):
        self.__currentReadNumber = responsedProductNumber

    def getCurrentReadNumber(self):
        return self.__currentReadNumber
