import ast

from account.service.response.AccountLoginResponse import AccountLoginResponse
from account.service.response.AccountRegisterResponse import AccountRegisterResponse
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
                CustomProtocol.ACCOUNT_LOGIN.value] = cls.__instance.generateAccountRegisterResponse

        return cls.__instance

    def __init__(self):
        print("ResponseGeneratorServiceImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def findResponseGenerator(self, protocolNumber):
        print("Response generator를 찾아옵니다")
        if self.__responseFormGenerationTable[protocolNumber] is not None:
            return self.__responseFormGenerationTable[protocolNumber]

        else:
            print(f"이 프로토콜 번호({protocolNumber}) 를 처리 할 수 있는 함수가 없습니다.")

    def generateAccountRegisterResponse(self, arguments):
        print("AccountRegisterResponse 생성")
        return AccountRegisterResponse(arguments)

    def generateAccountLoginResponse(self, arguments):
        return AccountLoginResponse(arguments)

