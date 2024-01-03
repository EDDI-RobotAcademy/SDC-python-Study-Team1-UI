class MyOrderListResponse:
    __myorderlist = []

    def __init__(self, myorderlist):
        self.__myorderlist = myorderlist

    def getmyorderlist(self):
        return self.__myorderlist
