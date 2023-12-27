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
        # while True:
        #     if not receiveQueue.empty():
        #         responsedUserId = receiveQueue.get()

        consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
        consoleUiService = ConsoleUiServiceImpl.getInstance()

        if receiveQueue.empty():
            self.consoleUiIntroduce(-1)
            consoleUiService.processUserInput(transmitQueue)

        while True:
            if not receiveQueue.empty():
                response = receiveQueue.get()
                print(f"Received response: {response}")
                sessionId = consoleUiRepository.saveAccountState(response)
                self.consoleUiIntroduce(sessionId)
                consoleUiService.processUserInput(transmitQueue)
            else:
                sleep(0.5)

    def consoleUiIntroduce(self, sessionId):
        if sessionId == -1:
            print('최초 구동 화면')
            print('0. 로그인')
            print('1. 회원가입')
            print('2. 상품 리스트 조회')
            print('3. 종료')
        else:
            print('로그인 후 구동 화면')
            print('0. 로그아웃')
            print('1. 상품 리스트 조회')
            print('2. 내 주문 내역 확인')
            print('3. 회원탈퇴')
            print('4. 종료')
