import abc


class ConsoleUiService(abc.ABC):
    @abc.abstractmethod
    def printMenu(self):
        pass

    @abc.abstractmethod
    def processUserInput(self, transmitQueue):
        pass
