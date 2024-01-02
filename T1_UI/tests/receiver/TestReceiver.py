import unittest
from account.service.response.AccountLoginResponse import AccountLoginResponse
from account.service.response.AccountRegisterResponse import AccountRegisterResponse
from console_ui.repository.ConsoleUiRepository import ConsoleUiRepository
from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl


class TestReceiver(unittest.TestCase):
    def testReceiver(self):
        receivedMapDataStr = {"protocol": 2, "data": {AccountLoginResponse: 15}}
        receivedMapDataStr2 = {"protocol": 2, "data": {AccountRegisterResponse: True}}
        proNum = receivedMapDataStr["protocol"]
        print(proNum)
        receivedData = receivedMapDataStr["data"]
        receivedData2 = receivedMapDataStr2["data"]
        print(f'{type(receivedData)}')
        this = receivedData.get(AccountLoginResponse)
        print(this)
        print(f'{type(this)}')
        this2 = receivedData2.get(AccountRegisterResponse)
        print(this2)
        print(f'{type(this2)}')

        consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
        consoleUiRepository.setSessionIdByUserId(this)
        sessionId = consoleUiRepository.getSessionId()


if __name__ == '__main__':
    unittest.main()