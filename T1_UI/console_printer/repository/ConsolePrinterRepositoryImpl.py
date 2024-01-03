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
                print('오류 발생: 회원 가입 실패 (중복된 아이디)')

        if className == "AccountLoginResponse":
            if response.getAccountSessionId() is not None:
                consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
                consoleUiRepository.setSessionIdByUserId(response.getAccountSessionId())
                print(f'로그인이 완료되었습니다. 사용자 아이디: {consoleUiRepository.getSessionId()}')
            if response.getAccountSessionId() is None:
                print('오류 발생: 로그인 실패 (잘못된 입력)')

        if className == "AccountLogoutResponse":
            if response.getIsSuccess():
                print('로그아웃이 완료되었습니다.')
                consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
                consoleUiRepository.resetSessionId()

            if not response.getIsSuccess():
                print('오류 발생: 로그아웃 실패')

        if className == "AccountDeleteResponse":
            if response.getIsSuccess():
                print('계정 삭제가 완료되었습니다.')
                consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
                consoleUiRepository.resetSessionId()

            if not response.getIsSuccess():
                print('오류 발생: 계정 삭제 실패')

        if className == "ProductListResponse":
            if response.getProductList() is not None:
                productList = response.getProductList()
                productListLength = len(productList)
                print("번호", "       ", "상품명", "       ", "가격(원)")
                print("============================================")
                for i in range(productListLength):
                    print(productList[i]["__productId"], "       ",
                          productList[i]["__productName"], "       ",
                          productList[i]["__productPrice"])

            else:
                print('오류 발생: 상품 목록 불러오기 실패')

        if className == "ProductReadResponse":
            if response.getId() is not None:
                consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
                consoleUiRepository.setProductNumber(response.getId())
                print('요청하신 상품 정보는 아래와 같습니다.')
                print(f'상품 번호 : {response.getId()}')
                print(f'상품 제목 : {response.getName()}')
                print(f'상품 가격 : {response.getPrice()}')
                print(f'상품 세부 정보 : {response.getDetails()}')
                print(f'상품 판매자 : {response.getAccountId()}')

            if response.getId() is None:
                print('오류 발생: 상품 조회 실패')

        if className == "ProductRegisterResponse":
            if response.getIsSuccess():
                print('상품 수정이 완료되었습니다.')

            if not response.getIsSuccess():
                print('오류 발생: 상품 등록 실패')

        if className == "ProductModifyResponse":
            if response.getIsSuccess():
                print('상품 수정이 완료되었습니다.')

            if not response.getIsSuccess():
                print('오류 발생: 상품 수정 실패')

        if className == "ProductPurchaseResponse":
            if response.getIsSuccess():
                print('상품 구매가 완료되었습니다.')

            if not response.getIsSuccess():
                print('오류 발생: 상품 구매 실패')

        if className == "ProductDeleteResponse":
            if response.getIsSuccess():
                print('상품 삭제가 완료되었습니다.')
                consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
                consoleUiRepository.resetProductNumber()

            if not response.getIsSuccess():
                print('오류 발생: 상품 삭제 실패')

        if className == "MyOrderListResponse":
            if response.getMyOrderList() is not None:
                myOrderList = response.getMyOrderList()
                myOrderListLength = len(myOrderList)
                print("번호", "       ", "상품명")
                print("=======================")
                for i in range(myOrderListLength):
                    print(myOrderList[i]["__productId"], "       ",
                          myOrderList[i]["__productName"])

            if not response.getIsSuccess():
                print('오류 발생: 주문 내역 불러오기 실패')

        if className == "MyOrderReadResponse":
            if response.getId() is not None:
                consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
                consoleUiRepository.setProductNumber(response.getId())
                print('주문된 상품 정보는 아래와 같습니다.')
                print(f'상품 번호 : {response.getId()}')
                print(f'상품 제목 : {response.getName()}')
                print(f'상품 가격 : {response.getPrice()}')
                print(f'상품 세부 정보 : {response.getDetails()}')

        if className == "MyOrderRemoveResponse":
            if response.getIsSuccess():
                print('주문 삭제가 완료되었습니다.')

            if not response.getIsSuccess():
                print('오류 발생: 주문 취소 실패 (잘못된 입력)')
