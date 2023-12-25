import abc

class CustomProtocolService(abc.ABC):
    @abc.abstractmethod
    def registerCustomProtocol(self, protocolNumber, poiterOfFuction):
        pass