import abc


class ResponseGeneratorService(abc.ABC):
    @abc.abstractmethod
    def findResponseGenerator(self, protocolNumber):
        pass

    @abc.abstractmethod
    def generateAccountRegisterResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateAccountLogoutResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateAccountLoginResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateAccountLogoutResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateAccountRemoveResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductListResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductRegisterResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductReadResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductModifyResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductPurchaseResponse(self, arguments):
        pass

    @abc.abstractmethod
    def generateProductRemoveResponse(self, arguments):
        pass

    # @abc.abstractmethod
    # def generateOrderListResponse(self, arguments):
    #     pass
    # @abc.abstractmethod
    # def generateOrderRemoveResponse(self, arguments):
    #     pass


