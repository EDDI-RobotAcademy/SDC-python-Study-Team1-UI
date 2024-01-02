import abc
class ResponseGeneratorService(abc.ABC):
    @abc.abstractmethod
    def findresponseGenerator(self, protocolNumber):
        pass
    @abc.abstractmethod
    def generateAccountRegisterReponse(self, arguments):
        pass