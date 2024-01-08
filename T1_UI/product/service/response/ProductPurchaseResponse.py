class ProductPurchaseResponse:
    def __init__(self, **kwargs):
        self.__productId = kwargs["__productNumber"]
        self.__name = kwargs["__productTitle"]
        self.__price = kwargs["__productPrice"]
        self.__details = kwargs["__productDetails"]
        self.__accountId = kwargs["__seller"]

    def getId(self):
        return self.__productId

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getDetails(self):
        return self.__details

    def getAccountId(self):
        return self.__accountId
