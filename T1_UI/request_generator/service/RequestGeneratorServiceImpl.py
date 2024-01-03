import ast

from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from custom_protocol.entity.CustomProtocol import CustomProtocol
from request_generator.service.RequestGeneratorService import RequestGeneratorService


class RequestGeneratorServiceImpl(RequestGeneratorService):
    __instance = None
    __requestFormGenerationTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__requestFormGenerationTable[
                CustomProtocol.ACCOUNT_REGISTER.value] = cls.__instance.generateAccountRegisterRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ACCOUNT_LOGIN.value] = cls.__instance.generateAccountLoginRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ACCOUNT_LOGOUT.value] = cls.__instance.generateAccountLogoutRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ACCOUNT_REMOVE.value] = cls.__instance.generateAccountDeleteRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_LIST.value] = cls.__instance.generateProductListRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_REGISTER.value] = cls.__instance.generateProductRegisterRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_READ.value] = cls.__instance.generateProductReadRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_MODIFY.value] = cls.__instance.generateProductModifyRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_PURCHASE.value] = cls.__instance.generateProductPurchaseRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.PRODUCT_REMOVE.value] = cls.__instance.generateProductRemoveRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ORDER_LIST.value] = cls.__instance.generateMyOrderListRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ORDER_READ.value] = cls.__instance.generateMyOrderReadRequest
            cls.__requestFormGenerationTable[
                CustomProtocol.ORDER_REMOVE.value] = cls.__instance.generateMyOrderRemoveRequest

        return cls.__instance

    def __init__(self):
        print("RequestGeneratorServiceImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def findRequestGenerator(self, protocolNumber):
        if self.__requestFormGenerationTable[protocolNumber] is not None:
            return self.__requestFormGenerationTable[protocolNumber]

        else:
            print(f"이 프로토콜 번호({protocolNumber}) 를 처리 할 수 있는 함수가 없습니다.")

    def generateAccountRegisterRequest(self, arguments):
        print("RequestGeneratorService: 회원 가입 dict data 형성")

        if not isinstance(arguments, tuple) or len(arguments) != 2:
            raise ValueError("Invalid request format")

        accountRegisterRequestData = {
            '__accountId': arguments[0].decode().strip(),
            '__password': arguments[1].decode().strip(),
        }

        return accountRegisterRequestData

    def generateAccountLoginRequest(self, arguments):
        print("RequestGeneratorService: 로그인 dict data 형성")

        if not isinstance(arguments, tuple) or len(arguments) != 2:
            raise ValueError("Invalid request format")

        accountLoginRequestData = {
            '__accountId': arguments[0].decode().strip(),
            '__password': arguments[1].decode().strip(),
        }

        return accountLoginRequestData

    def generateAccountLogoutRequest(self, arguments):
        print("RequestGeneratorService: 로그아웃 dict data 형성")
        print(f"현재 가지고 있는 session ID : {arguments} 를 삭제합니다.")

        accountLogoutRequestData = {
            '__accountSessionId': arguments,
        }
        return accountLogoutRequestData

    def generateAccountDeleteRequest(self, arguments):
        print("RequestGeneratorService: 회원 탈퇴 dict data 형성")
        print(f"현재 가지고 있는 session ID : {arguments} 로 회원 정보를 삭제합니다.")

        accountDeleteRequestData = {
            '__accountSessionId': arguments,
        }
        return accountDeleteRequestData

    def generateProductListRequest(self, arguments):
        print("RequestGeneratorService: 상품 리스트 (데이터 전송 없음)")
        pass

    def generateProductRegisterRequest(self, arguments):
        print("RequestGeneratorService: 상품 등록 dict data 형성")

        if not isinstance(arguments, tuple) or len(arguments) != 3:
            raise ValueError("Invalid request format")

        productRegisterRequestData = {
            '__productTitle': arguments[0].decode().strip(),
            '__productDetails': arguments[1].decode().strip(),
            '__productPrice': arguments[2],
        }

        return productRegisterRequestData

    def generateProductReadRequest(self, arguments):
        print("RequestGeneratorService : 상품 조회 dict data 형성")

        if not isinstance(arguments, int):
            raise ValueError("Invalid request format")

        productReadRequestData = {
            '__productNumber': arguments
        }

        return productReadRequestData

    def generateProductModifyRequest(self, arguments):
        print("RequestGeneratorService : 상품 수정 dict data 형성")

        consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
        currentReadProductNumber = consoleUiRepository.getProductNumber()

        productModifyRequestData = {
            '__productNumber': currentReadProductNumber,
            '__productTitle': arguments[0].decode().strip(),
            '__productDetails': arguments[1].decode().strip(),
            '__productPrice': arguments[2],
        }

        return productModifyRequestData

    def generateProductPurchaseRequest(self, arguments):
        print("RequestGeneratorService : 상품 구매 dict data 형성")

        consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
        currentReadProductNumber = consoleUiRepository.getProductNumber()

        productPurchaseRequestData = {
            '__productNumber': currentReadProductNumber,
        }

        return productPurchaseRequestData

    def generateProductRemoveRequest(self, arguments):
        print("RequestGeneratorService : 상품 삭제 dict data 형성")

        consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
        currentReadProductNumber = consoleUiRepository.getProductNumber()

        productRemoveRequestData = {
            '__productNumber': currentReadProductNumber,
        }

        return productRemoveRequestData

    def generateMyOrderListRequest(self, arguments):
        print("RequestGeneratorService: 내 주문 리스트 (데이터 전송 없음)")
        pass

    def generateMyOrderReadRequest(self, arguments):
        print("RequestGeneratorService: 내 주문 상세 조회 dict data 형성")

        myOrderReadData = {
            '__productOrderNumber': arguments
        }

        return myOrderReadData

    def generateMyOrderRemoveRequest(self, arguments):
        print("RequestGeneratorService: 내 주문 삭제 dict data 형성")

        consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()
        currentReadProductNumber = consoleUiRepository.getProductNumber()

        myOrderRemoveData = {
            '__productOrderNumber': currentReadProductNumber
        }

        return myOrderRemoveData
