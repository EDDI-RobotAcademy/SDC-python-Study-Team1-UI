class MyOrderListResponse:
    __myOrderList = []

    def __init__(self, __myOrderList):
        self.__myOrderList = __myOrderList

    def getMyOrderList(self):
        return self.__myOrderList
