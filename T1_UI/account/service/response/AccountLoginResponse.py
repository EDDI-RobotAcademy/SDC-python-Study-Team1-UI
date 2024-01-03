class AccountLoginResponse:
    def __init__(self, **kwargs):
        self.__accountSessionId = kwargs['__accountSessionId']

    def getAccountSessionId(self):
        return self.__accountSessionId
