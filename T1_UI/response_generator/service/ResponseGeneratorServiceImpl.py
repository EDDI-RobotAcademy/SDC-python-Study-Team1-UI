
from account.service.response.AccountRegisterResponse import AccountRegisterResponse
from account.service.response.AccountLoginResponse import AccountLoginResponse
from account.service.response.AccountLogoutResponse import AccountLogoutResponse
from account.service.response.AccountDeleteResponse import AccountDeleteResponse
from product.service.response.ProductListResponse import ProductListResponse
from product.service.response.ProductRegisterResponse import ProductRegisterResponse
from product.service.response.ProductReadResponse import ProductReadResponse
from product.service.response.ProductModifyResponse import ProductModifyResponse
from product.service.response.ProductPurchaseResponse import ProductPurchaseResponse
from product.service.response.ProductDeleteResponse import ProductDeleteResponse
from my_order.service.response.MyOrderListResponse import MyOrderListResponse
from my_order.service.response.MyOrderReadResponse import MyOrderReadResponse
from my_order.service.response.MyOrderRemoveResponse import MyOrderRemoveResponse

from custom_protocol.entity.CustomProtocol import CustomProtocol
from response_generator.service.ResponseGeneratorService import ResponseGeneratorService


class ResponseGeneratorServiceImpl(ResponseGeneratorService):
    __instance = None
    __responseFormGenerationTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__responseFormGenerationTable[
                CustomProtocol.ACCOUNT_REGISTER.value] = cls.__instance.generateAccountRegisterResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ACCOUNT_LOGIN.value] = cls.__instance.generateAccountLoginResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ACCOUNT_LOGOUT.value] = cls.__instance.generateAccountLogoutResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ACCOUNT_REMOVE.value] = cls.__instance.generateAccountRemoveResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_LIST.value] = cls.__instance.generateProductListResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_REGISTER.value] = cls.__instance.generateProductRegisterResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_READ.value] = cls.__instance.generateProductReadResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_MODIFY.value] = cls.__instance.generateProductModifyResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_PURCHASE.value] = cls.__instance.generateProductPurchaseResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.PRODUCT_REMOVE.value] = cls.__instance.generateProductRemoveResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ORDER_LIST.value] = cls.__instance.generateMyOrderListResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ORDER_READ.value] = cls.__instance.generateMyOrderReadResponse
            cls.__responseFormGenerationTable[
                CustomProtocol.ORDER_REMOVE.value] = cls.__instance.generateMyOrderRemoveResponse

        return cls.__instance

    def __init__(self):
        print("ResponseGeneratorServiceImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def findResponseGenerator(self, protocolNumber):
        if self.__responseFormGenerationTable[protocolNumber] is not None:
            return self.__responseFormGenerationTable[protocolNumber]

        else:
            print(f"이 프로토콜 번호({protocolNumber}) 를 처리 할 수 있는 함수가 없습니다.")

    def generateAccountRegisterResponse(self, arguments):
        return AccountRegisterResponse(arguments)

    def generateAccountLoginResponse(self, arguments):
        return AccountLoginResponse(arguments)

    def generateAccountLogoutResponse(self, arguments):
        return AccountLogoutResponse(arguments)

    def generateAccountRemoveResponse(self, arguments):
        return AccountDeleteResponse(arguments)

    def generateProductListResponse(self, arguments):
        return ProductListResponse(arguments)

    def generateProductRegisterResponse(self, arguments):
        return ProductRegisterResponse(arguments)

    def generateProductReadResponse(self, arguments):
        return ProductReadResponse(**arguments)

    def generateProductModifyResponse(self, arguments):
        return ProductModifyResponse(arguments)

    def generateProductPurchaseResponse(self, arguments):
        return ProductPurchaseResponse(arguments)

    def generateProductRemoveResponse(self, arguments):
        return ProductDeleteResponse(arguments)

    def generateMyOrderListResponse(self, arguments):
        return MyOrderListResponse(arguments)

    def generateMyOrderReadResponse(self, arguments):
        return MyOrderReadResponse(**arguments)

    def generateMyOrderRemoveResponse(self, arguments):
        return MyOrderRemoveResponse(arguments)



