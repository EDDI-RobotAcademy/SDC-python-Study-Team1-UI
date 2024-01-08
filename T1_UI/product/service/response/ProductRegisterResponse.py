class ProductRegisterResponse:
    __productList = []

    def __init__(self, productUpdatedList):
        self.__productList = productUpdatedList

    def getUpdatedProductList(self):
        return self.__productList
