import abc

class ConsoleUiRepository(abc.ABC):
    @abc.abstractmethod
    def saveCurrentRoutingState(self, currentState):
        pass

    @abc.abstractmethod
    def acquireCurrentRoutingState(self):
        pass

    @abc.abstractmethod
    def saveAccountState(self, userId):
        pass

    @abc.abstractmethod
    def acquireAccountState(self):
        pass