import multiprocessing
import unittest
from unittest import mock

from account_form.repository.AccountFormRepositoryImpl import AccountFormRepositoryImpl
from console_printer.repository.ConsolePrinterRepositoryImpl import ConsolePrinterRepositoryImpl
from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from console_ui.service.ConsoleUiServiceImpl import ConsoleUiServiceImpl
from custom_protocol.entity.CustomProtocol import CustomProtocol
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl


class TestConsolePrinter(unittest.TestCase):

    def fuck(self):
        print('fuck!')

    def testPrinterOperationWithConsoleUiDomain(self):
        print('session = -1 인 경우 0번 명령이 잘 convert가 되는가 ?')
        initialSessionState = -1
        consolePrinterRepo = ConsolePrinterRepositoryImpl.getInstance()

        customProtocolRepostiory = CustomProtocolRepositoryImpl.getInstance()
        accountFormRepository = AccountFormRepositoryImpl.getInstance()
        customProtocolRepostiory.register(CustomProtocol.ACCOUNT_LOGIN.value,
                                          accountFormRepository.createAccountSigninForm)
        customProtocolRepostiory.register(CustomProtocol.ACCOUNT_REGISTER.value,
                                          accountFormRepository.createAccountRegisterForm)
        customProtocolRepostiory.register(CustomProtocol.ACCOUNT_LOGOUT.value,
                                          self.fuck)

        consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
        consoleUiRepository.saveAccountState(initialSessionState)
        consoleUiService = ConsoleUiServiceImpl(consoleUiRepository)

        transmitQueue = mock
        receiveQueue = multiprocessing.Queue()
        receiveQueue.put(initialSessionState)

        consolePrinterRepo.printConsoleUi(transmitQueue, receiveQueue)

        # 이 다음 명령의 실행은 transmitter에서 하는거임


if __name__ == '__main__':
    unittest.main()