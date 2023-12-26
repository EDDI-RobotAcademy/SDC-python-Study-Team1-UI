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

    def processUserInput(self):
        print(f'최초 구동 화면')
        print(f'0. 로그인')
        print(f'1. 회원가입')
        print(f'2. 상품 리스트 조회')
        print(f'3. 종료')

        userInput = KeyboardInput.getKeyboardIntegerInput()
        self.__repository.saveCurrentRoutingState(userInput)

        return userInput
