import unittest
from unittest import mock

from account_form.repository.AccountFormRepositoryImpl import AccountFormRepositoryImpl
from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from console_ui.service.ConsoleUiServiceImpl import ConsoleUiServiceImpl
from custom_protocol.entity.CustomProtocol import CustomProtocol
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl


class TestConsoleUi(unittest.TestCase):
    def testConsoleUiGetInstance(self):
        print("ConsoleUi Instance 생성 하고싶어")

        consoleUiRepository = ConsoleUiRepositoryImpl()
        consoleUiService = ConsoleUiServiceImpl(consoleUiRepository)
        self.assertIsNotNone(consoleUiService)

    def testProcessingUserInput(self):
        print("Processing 잘 되니?")

        consoleUiRepository = ConsoleUiRepositoryImpl()
        consoleUiService = ConsoleUiServiceImpl(consoleUiRepository)
        consoleUiService.processUserInput()

    def testSettingAccountState(self):
        print("SessionId 를 AccountUid 로 대체하기")
        receivedUid = 1
        consoleUiRepository = ConsoleUiRepositoryImpl()
        consoleUiRepository.saveAccountState(receivedUid)
        self.assertIs(consoleUiRepository.acquireAccountState(), receivedUid)

    def testAccountStateBasedProcessing(self):
        print("Account State 가 -1 이 아니면 로그인 된 UI 출력")
        initialState = -1
        receivedUid = 1

        customProtocolRepostiory = CustomProtocolRepositoryImpl.getInstance()
        accountFormRepository = AccountFormRepositoryImpl.getInstance()
        customProtocolRepostiory.register(CustomProtocol.ACCOUNT_LOGIN.value,
                                          accountFormRepository.createAccountSigninForm)

        consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
        consoleUiRepository.saveAccountState(initialState)
        consoleUiService = ConsoleUiServiceImpl(consoleUiRepository)

        transmitQueue = mock

        if consoleUiRepository.acquireAccountState() == initialState:
            customProtocolRepostiory.execute(consoleUiService.processUserInput(transmitQueue))
            consoleUiRepository.saveAccountState(receivedUid)

        # if consoleUiRepository.acquireAccountState() == receivedUid:
        #     print("로그인이 됐으면 다음과 같은 UI 가 나와야 해")
        #     print('0. 로그아웃')
        #     print('1. 상품 리스트 조회')
        #     print('2. 내 주문 내역 확인')
        #     print('3. 회원탈퇴')
        #     print('4. 종료')


if __name__ == '__main__':
    unittest.main()