import sys
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

        consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()

        className = response.__class__.__name__

        if className == "AccountRegisterResponse":
            if response.getIsSuccess():
                print('\033[92m회원 가입이 완료되었습니다.\033[0m')

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 회원 가입 실패 (중복된 아이디)\033[0m')

        if className == "AccountLoginResponse":
            if response.getAccountSessionId() is not None:
                consoleUiRepository.setSessionIdByUserId(response.getAccountSessionId())
                print(f'\033[94m로그인이 완료되었습니다. 사용자 아이디:\033[0m {consoleUiRepository.getSessionId()}')
            if response.getAccountSessionId() is None:
                print('\033[91m오류 발생: 로그인 실패 (잘못된 입력)\033[0m')

        if className == "AccountLogoutResponse":
            if response.getIsSuccess():
                print('\033[92m로그아웃이 완료되었습니다.\033[0m')
                consoleUiRepository.resetSessionId()

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 로그아웃 실패\033[0m')

        if className == "AccountDeleteResponse":
            if response.getIsSuccess():
                print('\033[94m계정 삭제가 완료되었습니다.\033[0m')
                consoleUiRepository.resetSessionId()

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 계정 삭제 실패\033[0m')

        if className == "ProductListResponse":
            if response.getProductList() is not None:
                consoleUiRepository.resetProductNumber()
                productList = response.getProductList()
                productListLength = len(productList)
                print("\033[91m번호\033[0m", "       ", "\033[91m상품명\033[0m", "       ", "\033[91m가격(원)\033[0m")
                print("\033[95m============================================\033[0m")
                for i in range(productListLength):
                    print(productList[i]["__productNumber"], "       ",
                          productList[i]["__productTitle"], "       ",
                          productList[i]["__productPrice"])
            else:
                print('\033[91m오류 발생: 상품 목록 불러오기 실패\033[0m')

        if className == "ProductReadResponse":
            if response.getId() is not None:
                consoleUiRepository.setProductNumber(response.getId())
                print(f"현재 조회하고 있는 상품 번호 저장 : {consoleUiRepository.getProductNumber()}번")
                print('\033[92m요청하신 상품 정보는 아래와 같습니다.\033[0m')
                print(f'\033[94m상품 번호 :\033[0m {response.getId()}')
                print(f'\033[94m상품 제목 :\033[0m {response.getName()}')
                print(f'\033[92m상품 가격 :\033[0m {response.getPrice()}')
                print(f'\033[94m상품 세부 정보 :\033[0m {response.getDetails()}')
                print(f'\033[92m상품 등록자 :\033[0m {response.getAccountId()}')
            else:
                print('\033[91m오류 발생: 상품 조회 실패 - 존재하지 않는 상품입니다.\033[0m')
                consoleUiRepository.saveCurrentRoutingState(1)

        if className == "ProductRegisterResponse":
            if response.getIsSuccess():
                print('\033[94m상품 등록이 완료되었습니다.\033[0m')

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 상품 등록 실패\033[0m')

        if className == "ProductModifyResponse":
            if response.getIsSuccess():
                print('\033[92m상품 수정이 완료되었습니다.\033[0m')

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 상품 수정 실패\033[0m')

        if className == "ProductPurchaseResponse":
            if response.getIsSuccess():
                print('\033[94m상품 구매가 완료되었습니다.\033[0m')

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 상품 구매 실패\033[0m')

        if className == "ProductDeleteResponse":
            if response.getIsSuccess():
                consoleUiRepository.resetProductNumber()
                print('\033[92m상품 삭제가 완료되었습니다.\033[0m')

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 상품 삭제 실패\033[0m')

        if className == "MyOrderListResponse":
            if response.getMyOrderList() is not None:
                consoleUiRepository.resetProductNumber()
                myOrderList = response.getMyOrderList()
                myOrderListLength = len(myOrderList)
                sum = 0
                print("\033[91m번호\033[0m", "       ", "\033[91m상품명\033[0m", "       ", "\033[91m가격(원)\033[0m")
                print("\033[95m=============================\033[0m")
                for i in range(myOrderListLength):
                    print(myOrderList[i]["__productNumber"], "       ",
                          myOrderList[i]["__productTitle"], "       ",
                          myOrderList[i]["__productPrice"])
                    sum += int(myOrderList[i]["__productPrice"])
                print("\033[95m=============================\033[0m")
                print(f"\033[95m주문 총액 : {sum}원\033[0m")

        if className == "MyOrderReadResponse":
            if response.getId() is not None:
                consoleUiRepository.setProductNumber(response.getId())
                print('\033[94m주문된 상품 정보는 아래와 같습니다.\033[0m')
                print(f'\033[92m상품 번호 :\033[0m {response.getId()}')
                print(f'\033[94m상품 제목 :\033[0m {response.getName()}')
                print(f'\033[92m상품 가격 :\033[0m {response.getPrice()}')
                print(f'\033[94m상품 세부 정보 :\033[0m {response.getDetails()}')
                print(f'\033[92m상품 판매자 :\033[0m {response.getSeller()}')
            else:
                print('\033[91m오류 발생: 주문 상세 조회 실패 - 존재하지 않는 상품입니다.\033[0m')
                consoleUiRepository.saveCurrentRoutingState(3)

        if className == "MyOrderRemoveResponse":
            if response.getIsSuccess():
                consoleUiRepository.resetProductNumber()
                print('\033[92m주문 삭제가 완료되었습니다.\033[0m')

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 주문 취소 실패 (잘못된 입력)\033[0m')

        if className == "ProgramExitResponse":
            while response.getIsSuccess():
                try:
                    print('밥 아저씨 그림 여기입니다.')
                    sys.exit()
                except SystemExit:
                    return
