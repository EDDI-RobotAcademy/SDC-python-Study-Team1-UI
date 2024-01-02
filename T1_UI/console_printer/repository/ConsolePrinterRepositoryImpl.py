from time import sleep

from console_printer.repository.ConsolePrinterRepository import ConsolePrinterRepository
from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from console_ui.service.ConsoleUiServiceImpl import ConsoleUiServiceImpl


class ConsolePrinterRepositoryImpl(ConsolePrinterRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("ConsolePrinterRepositoryImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def printConsoleUi(self, transmitQueue, receiveQueue):

        consoleUiService = ConsoleUiServiceImpl.getInstance()
        consoleUiService.printMenu()
        consoleUiService.processUserInput(transmitQueue)

        while True:
            if not receiveQueue.empty():
                response = receiveQueue.get()
                print(f"Received response: {response}")
                # 뭔가 있어야 되는데 없는 상태
                # responseGenerator(response) -> session 갱신
                self.__processResponse(response)
                consoleUiService.printMenu()
                consoleUiService.processUserInput(transmitQueue)
            else:
                sleep(0.5)

    def __processResponse(self, response):

        className = response.__class__.__name__

        if className == "AccountRegisterResponse":
            if response.getIsSuccess == True:
                print('회원 가입이 완료되었습니다.')
                return
            if response.getIsSuccess == False:
                print('회원 가입에 실패했습니다. 아이디 중복')
                return

        if className == "AccountLoginResponse":
            if response.getAccountSessionId is not None:
                consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
                consoleUiRepository.setSessionIdByUserId(response.getAccountSessionId)
                print(f'로그인이 완료되었습니다. 사용자 아이디: {response.getAccountSessionId}')
            if response.getAccountSessionId is None:
                print('로그인에 실패했습니다. 다시 입력하세요!')
                return