import unittest


from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from console_ui.service.ConsoleUiServiceImpl import ConsoleUiServiceImpl


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


if __name__ == '__main__':
    unittest.main()