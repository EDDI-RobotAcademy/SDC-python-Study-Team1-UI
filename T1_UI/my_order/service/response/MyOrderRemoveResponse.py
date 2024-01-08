class MyOrderRemoveResponse:
    __myOrderList = []

    def __init__(self, __myOrderUpdatedList):
        self.__myOrderList = __myOrderUpdatedList

    def getMyOrderUpdatedList(self):
        return self.__myOrderList
