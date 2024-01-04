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
    def generateAccountLogoutRequest(self, arguments):
        pass

    @abc.abstractmethod
    def generateAccountDeleteRequest(self, arguments):
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
    def generateProductModifyRequest(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductPurchaseRequest(self, arguments1, arguments2):
        pass

    @abc.abstractmethod
    def generateProductRemoveRequest(self, arguments):
        pass

    @abc.abstractmethod
    def generateMyOrderListRequest(self, arguments):
        pass

    @abc.abstractmethod
    def generateMyOrderRemoveRequest(self, arguments):
        pass
