import unittest


from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from console_ui.service.ConsoleUiServiceImpl import ConsoleUiServiceImpl


class TestConsoleUi(unittest.TestCase):
    def testConsoleUiGetInstance(self):
        print("ConsoleUi Instance 생성 하고싶어")

        consoleUiRepository = ConsoleUiRepositoryImpl()
        consoleUiService = ConsoleUiServiceImpl(consoleUiRepository)
        self.assertIsNotNone(consoleUiRepository)


if __name__ == '__main__':
    unittest.main()