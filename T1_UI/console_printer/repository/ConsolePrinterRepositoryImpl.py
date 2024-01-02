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
                self.__processResponse(response)
                consoleUiService.printMenu()
                consoleUiService.processUserInput(transmitQueue)
            else:
                sleep(0.5)

    def __processResponse(self, response):

        className = response.__class__.__name__

        if className == "AccountRegisterResponse":
            if response.getIsSuccess():
                print('회원 가입이 완료되었습니다.')

            if not response.getIsSuccess():
                print('회원 가입에 실패했습니다. 아이디 중복')

        if className == "AccountLoginResponse":
            if response.getAccountSessionId() is not None:
                consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
                consoleUiRepository.setSessionIdByUserId(response.getAccountSessionId())
                print(f'로그인이 완료되었습니다. 사용자 아이디: {response.getAccountSessionId()}')
            if response.getAccountSessionId() is None:
                print('로그인에 실패했습니다. 다시 입력하세요!')

        if className == "AccountLogoutResponse":
            if response.getIsSuccess():
                print('로그아웃이 완료되었습니다.')

            if not response.getIsSuccess():
                print('이런 상황이 있을까?')

        if className == "AccountDeleteResponse":
            if response.getIsSuccess():
                print('계정 삭제가 완료되었습니다.')

            if not response.getIsSuccess():
                print('이런 상황이 있을까?')

        if className == "ProductRegisterResponse":
            if response.getIsSuccess():
                print('상품 수정이 완료되었습니다.')

            if not response.getIsSuccess():
                print('이런 상황이 있을까?')

        if className == "ProductModifyResponse":
            if response.getIsSuccess():
                print('상품 수정이 완료되었습니다.')

            if not response.getIsSuccess():
                print('이런 상황이 있을까?')

        if className == "ProductPurchaseResponse":
            if response.getIsSuccess():
                print('상품 구매가 완료되었습니다.')

            if not response.getIsSuccess():
                print('이런 상황이 있을까?')

        if className == "ProductDeleteResponse":
            if response.getIsSuccess():
                print('상품 수정이 완료되었습니다.')

            if not response.getIsSuccess():
                print('이런 상황이 있을까?')
