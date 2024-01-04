import abc


class RequestGeneratorService(abc.ABC):

    @abc.abstractmethod
    def findRequestGenerator(self, protocolNumber):
        pass

    @abc.abstractmethod
    def generateAccountRegisterRequest(self, arguments):
        pass

    @abc.abstractmethod
    def generateAccountLoginRequest(self, arguments):
        pass

    @abc.abstractmethod
    def generateAccountLogoutRequest(self, accountSessionId):
        pass

    @abc.abstractmethod
    def generateAccountDeleteRequest(self, accountSessionId):
        pass

    @abc.abstractmethod
    def generateProductListRequest(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductRegisterRequest(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductReadRequest(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductModifyRequest(self, currentReadProductNumber, arguments):
        pass

    @abc.abstractmethod
    def generateProductPurchaseRequest(self, accountSessionId, currentReadProductNumber):
        pass

    @abc.abstractmethod
    def generateProductRemoveRequest(self, currentReadProductNumber):
        pass

    @abc.abstractmethod
    def generateMyOrderListRequest(self, accountSessionId):
        pass

    @abc.abstractmethod
    def generateMyOrderReadRequest(self, accountSessionId, arguments):
        pass

    @abc.abstractmethod
    def generateMyOrderRemoveRequest(self, accountSessionId, currentReadProductNumber):
        pass
