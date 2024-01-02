import unittest
from account.service.response.AccountLoginResponse import AccountLoginResponse
from account.service.response.AccountRegisterResponse import AccountRegisterResponse
from console_ui.repository.ConsoleUiRepository import ConsoleUiRepository
from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from response_generator.service.ResponseGeneratorServiceImpl import ResponseGeneratorServiceImpl


class TestReceiver(unittest.TestCase):
    def testReceiver(self):
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()
        # 1. 회원가입 응답 형태
        # receivedMapDataStr = {"protocol": 1, "data": "AccountRegisterResponse(_AccountRegisterResponse"
        #                                              "__isSuccess=True)"}
        # 2. 로그인 응답 형태
        # receivedMapDataStr = {"protocol": 2, "data": "AccountLoginResponse(_AccountLoginResponse"
        #                                              "__accountSessionId=3)"}

        # protonum = receivedMapDataStr["protocol"]
        # responseData = receivedMapDataStr["data"]
        # response = responseGenerator.findgeneratorbyprotocol(protonum) # login 객체 형성
        # response(responseData) # id 값 넣어서 객체 완성
        receivedMapDataStr = {"protocol": 3, "data": True}
        responseGenerator = responseGeneratorService.findResponseGenerator(receivedMapDataStr["protocol"])
        responseObj = responseGenerator(receivedMapDataStr["data"])

        # receivedData = receivedMapDataStr["data"]

        # print(f'{type(responseObj)}')
        #
        # evalThis = eval(responseObj)
        # print(evalThis)

        className = responseObj.__class__.__name__

        if className == "AccountRegisterResponse":
            if responseObj.getIsSuccess():
                print('회원 가입이 완료되었습니다.')

            if not responseObj.getIsSuccess():
                print('회원 가입에 실패했습니다. 아이디 중복')

        if className == "AccountLoginResponse":
            if responseObj.getAccountSessionId() is not None:
                consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
                consoleUiRepository.setSessionIdByUserId(responseObj.getAccountSessionId())
                print(f'로그인이 완료되었습니다. 사용자 아이디: {responseObj.getAccountSessionId()}')
            if responseObj.getAccountSessionId() is None:
                print('로그인에 실패했습니다. 다시 입력하세요!')
                return

        if className == "AccountLogoutResponse":
            if responseObj.getIsSuccess():
                print('로그아웃이 완료되었습니다.')

            if not responseObj.getIsSuccess():
                print('이런 상황이 있을까?')

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