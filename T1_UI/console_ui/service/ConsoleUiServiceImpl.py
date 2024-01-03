from console_ui.service.ConsoleUiService import ConsoleUiService
from utility.keyboard.KeyboardInput import KeyboardInput


class ConsoleUiServiceImpl(ConsoleUiService):
    __instance = None

    def __new__(cls, repository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__repository = repository
        return cls.__instance

    def __init__(self, repository):
        print("ConsoleUiServiceImpl 생성자 호출")


    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def printMenu(self):
        print("ConsoleUiServiceImpl: printMenu")
        self.__repository.menuPrinter()

    def processUserInput(self, transmitQueue):
        print("ConsoleUiServiceImpl: processUserInput")
        sessionId = self.__repository.getSessionId()
        userCommandNumber = KeyboardInput.getKeyboardIntegerInput()
        convertedUserCommandNumber = self.__repository.commandConverter(userCommandNumber)
        transmitData = {'protocolNumber': convertedUserCommandNumber,
                        'sessionId': int(sessionId.get("__accountSessionId"))}
        self.__repository.routingStateConverter(convertedUserCommandNumber)

        transmitQueue.put(transmitData)
