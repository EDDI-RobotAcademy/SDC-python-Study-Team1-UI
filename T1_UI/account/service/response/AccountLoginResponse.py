class AccountLoginResponse:
    def __init__(self, __accountId):
        self.__accountId = __accountId

    def getAccountSessionId(self):
        return self.__accountId
