import abc


class ClientSocketService:
    @abc.abstractmethod
    def createClientSocket(self, host, port):
        pass

    @abc.abstractmethod
    def connectToTargetHost(self):
        pass

    @abc.abstractmethod
    def setBlockingOperation(self):
        pass