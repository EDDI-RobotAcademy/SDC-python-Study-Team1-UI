import abc


class ConsoleUiRepository(abc.ABC):
    @abc.abstractmethod
    def saveCurrentRoutingState(self, currentState):
        pass

    @abc.abstractmethod
    def acquireCurrentRoutingState(self):
        pass

    @abc.abstractmethod
    def menuPrinter(self):
        pass

    @abc.abstractmethod
    def commandConverter(self, userCommand):
        pass

    @abc.abstractmethod
    def routingStateConverter(self, convertedUserChoice):
        pass
