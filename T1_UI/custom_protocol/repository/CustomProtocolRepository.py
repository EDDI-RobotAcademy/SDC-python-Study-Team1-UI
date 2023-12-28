import abc


class CustomProtocolRepository(abc.ABC):
    @abc.abstractmethod
    def register(self, protocolNumber, poiterOfFuction):
        pass

    @abc.abstractmethod
    def execute(self, protocolNumber, *arguments, **mapArguments):
        pass
