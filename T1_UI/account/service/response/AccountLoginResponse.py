class AccountLoginResponse:
    def __init__(self, __accountSessionId):
        self.__accountSessionId = __accountSessionId

    def getAccountSessionId(self):
        return self.__accountSessionId
