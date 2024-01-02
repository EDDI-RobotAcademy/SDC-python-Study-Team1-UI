import unittest
from account.service.response.AccountLoginResponse import AccountLoginResponse
from account.service.response.AccountRegisterResponse import AccountRegisterResponse
from console_ui.repository.ConsoleUiRepository import ConsoleUiRepository
from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl


class TestReceiver(unittest.TestCase):
    def testReceiver(self):
        receivedMapDataStr = {"protocol": 1, "data": "AccountRegisterResponse(_AccountRegisterResponse"
                                                     "__isSuccess=True)"}

        receivedData = receivedMapDataStr["data"]

        print(f'{type(receivedData)}')
        evalThis = eval(receivedData)
        # print(evalThis.getIsSuccess())

        className = evalThis.__class__.__name__

        if className == "AccountRegisterResponse":
            if evalThis.getIsSuccess() == True:
                print('회원 가입이 완료되었습니다.')

            if evalThis.getIsSuccess() == False:
                print('회원 가입에 실패했습니다. 아이디 중복')

        # if className == "AccountLoginResponse":
        #     if evalThis.getAccountSessionId is not None:
        #         consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
        #         consoleUiRepository.setSessionIdByUserId(evalThis.getAccountSessionId)
        #         print(f'로그인이 완료되었습니다. 사용자 아이디: {evalThis.getAccountSessionId}')
        #     if evalThis.getAccountSessionId is None:
        #         print('로그인에 실패했습니다. 다시 입력하세요!')
        #         return

    def testEvalClassGeneration(self):
        class TestAccountRegisterResponse:
            def __init__(self, __isSuccess):
                self.__isSuccess = __isSuccess

            def getIsSuccess(self):
                return self.__isSuccess

        # protocol number 받지 않는게 좋겠다.
        data = "TestAccountRegisterResponse(_TestAccountRegisterResponse__isSuccess=True)"
        responseBbject = eval(data)

        isSuccessValue = responseBbject.getIsSuccess()

        print(f'Extracted __isSuccess value: {isSuccessValue}')


if __name__ == '__main__':
    unittest.main()