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
            # cls.__requestFormGenerationTable[
            #     CustomProtocol.PRODUCT_LIST.value] = cls.__instance.generateProductListRequest
            # cls.__requestFormGenerationTable[
            #     CustomProtocol.PRODUCT_REGISTER.value] = cls.__instance.generateProductRegisterRequest
            # cls.__requestFormGenerationTable[
            #     CustomProtocol.PRODUCT_READ.value] = cls.__instance.generateProductReadRequest
            # cls.__requestFormGenerationTable[
            #     CustomProtocol.PRODUCT_MODIFY.value] = cls.__instance.generateProductModifyRequest
            # cls.__requestFormGenerationTable[
            #     CustomProtocol.PRODUCT_PURCHASE.value] = cls.__instance.generateProductPurchaseRequest
            # cls.__requestFormGenerationTable[
            #     CustomProtocol.PRODUCT_REMOVE.value] = cls.__instance.generateProductRemoveRequest
            # cls.__requestFormGenerationTable[
            #     CustomProtocol.ORDER_LIST.value] = cls.__instance.generateOrderListRequest
            # cls.__requestFormGenerationTable[
            #     CustomProtocol.ORDER_REMOVE.value] = cls.__instance.generateOrderRemoveRequest

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

        accountRequestData = {
            '__accountId': arguments[0].decode().strip(),
            '__password': arguments[1].decode().strip(),
        }

        return accountRequestData

    def generateAccountLoginRequest(self, arguments):
        print("RequestGeneratorService: 로그인 dict data 형성")

        if not isinstance(arguments, tuple) or len(arguments) != 2:
            raise ValueError("Invalid request format")

        accountRequestData = {
            '__accountId': arguments[0].decode().strip(),
            '__password': arguments[1].decode().strip(),
        }

        return accountRequestData

    def generateAccountLogoutRequest(self, arguments):
        print("RequestGeneratorService: 로그아웃 dict data 형성")
        print(f"현재 가지고 있는 session ID : {arguments} 를 삭제합니다.")

        accountRequestData = {
            '__accountSessionId': arguments,
        }

        return accountRequestData

    def generateAccountDeleteRequest(self, arguments):
        print("RequestGeneratorService: 회원 탈퇴 dict data 형성")
        print(f"현재 가지고 있는 session ID : {arguments} 로 회원 정보를 삭제합니다.")

        accountRequestData = {
            '__accountSessionId': arguments,
        }

        return accountRequestData

    def generateProductListRequest(self, arguments):
        return None

    def generateProductRegisterRequest(self, arguments):
        print("RequestGeneratorService : Register ")
        productRequestData = {
            '__productTitle': arguments[0].decode().strip(),
            '__productContent': arguments[1].decode().strip(),
            '__productPrice': arguments[2],
        }
        return productRequestData

    def generateProductReadRequest(self, arguments):
        print("RequestGeneratorService : Read")
        productRequestData = {
            '__productNumber': arguments,

        }
        return productRequestData

    def generateProductModifyRequest(self, arguments):
        print("RequestGeneratorService Modify")
        productRequestData = {
            '__productNumber': arguments[0],
            '__productTitle': arguments[1].decode().strip(),
            '__productContent': arguments[2].decode().strip(),
            '__productPrice': arguments[3],
        }
        return productRequestData

    def generateProductPurchaseRequest(self, arguments):
        print("RequestGeneratorService Purchase")
        productRequestData = {
            '__productNumber': arguments,
        }
        return productRequestData

    def generateProductRemoveRequest(self, arguments):
        print("RequestGeneratorService Remove")
        productRequestData = {
            '__productNumber': arguments,
        }
        return productRequestData

    def generateProductOrderListRequest(self, arguments):
        print("RequestGeneratorService OrderList")
        productRequestData = {
            '__productOrderNumber': arguments,
        }
        return productRequestData

    def generateProductOrderRemoveRequest(self, arguments):
        print("RequestGeneratorService - OrderRemove")
        productRequestData = {
            '__productOrderNumber': arguments,
        }
        return productRequestData


