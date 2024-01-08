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
        currentReadNumber = self.__repository.getProductNumber()
        userCommandNumber = KeyboardInput.getKeyboardIntegerInputWithOutputMessage("원하는 선택지를 입력하세요:")
        convertedUserCommandNumber = self.__repository.commandConverter(userCommandNumber)
        self.__repository.routingStateConverter(convertedUserCommandNumber)

        while (convertedUserCommandNumber == -1 or convertedUserCommandNumber == 0 or
               convertedUserCommandNumber == 4 or convertedUserCommandNumber == 14):

            userCertifiedInput = self.__getUserInputCertificationMessage(convertedUserCommandNumber)

            if userCertifiedInput == "y" or "Y":
                break
            elif userCertifiedInput == "n" or "N" or userCertifiedInput is None:
                self.printMenu()
                userCommandNumber = KeyboardInput.getKeyboardIntegerInputWithOutputMessage("원하는 선택지를 입력하세요:")
                convertedUserCommandNumber = self.__repository.commandConverter(userCommandNumber)
                self.__repository.routingStateConverter(convertedUserCommandNumber)
            else:
                print('유효하지 않은 입력입니다. y(Y) 혹은 n(N) 을 입력하세요!')

        transmitData = {'protocolNumber': convertedUserCommandNumber, 'sessionId': sessionId,
                        'productNumber': currentReadNumber}

        transmitQueue.put(transmitData)

    def __getUserInputCertificationMessage(self, convertedUserCommandNumber):

        if convertedUserCommandNumber == 4:
            userCertifiedInput = (
                KeyboardInput.getKeyboardStringInputWithOutputMessage("\033[91m회원 탈퇴를 계속하시겠습니까?(y/n):\033[0m", 4))
            return userCertifiedInput.decode().strip()

        elif convertedUserCommandNumber == 14:
            userCertifiedInput = (
                KeyboardInput.getKeyboardStringInputWithOutputMessage("\033[91m정말 종료하시겠습니까?(y/n):\033[0m", 4))
            return userCertifiedInput.decode().strip()
        else:
            return None
