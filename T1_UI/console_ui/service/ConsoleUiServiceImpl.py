from console_ui.service.ConsoleUiService import ConsoleUiService
from custom_protocol.entity.CustomProtocol import CustomProtocol
from custom_protocol.repository.CustomProtocolRepository import CustomProtocolRepository
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
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

    def processUserInput(self, transmitQueue):
        # 지금은 sessionId = None 인 상태임
        # -1 로 만들어줘야 함
        sessionId = self.__repository.acquireAccountState()
        userCommandNumber = KeyboardInput.getKeyboardIntegerInput()
        convertedCommandNumber = self.determineUserCommand(sessionId, userCommandNumber)
        transmitQueue.put(convertedCommandNumber)
        # customProtocolRepository = CustomProtocolRepositoryImpl.getInstance()
        # request = customProtocolRepository.execute(convertedCommandNumber)

        # self.__repository.saveCurrentRoutingState(convertedCommandNumber)

        # transmitQueue.put(sessionId, convertedCommandNumber)
        # print(f'transmitQueue 에 담길 정보 = {sessionId}, {convertedCommandNumber}, {request}')
        # return sessionId, convertedCommandNumber

    def determineUserCommand(self, sessionId, userCommandNumber):
        # if sessionId == -1:
        #     print('최초 구동 화면')
        #     print('0. 로그인')
        #     print('1. 회원가입')
        #     print('2. 상품 리스트 조회')
        #     print('3. 종료')
        # else:
        #     print('로그인 후 구동 화면')
        #     print('0. 로그아웃')
        #     print('1. 상품 리스트 조회')
        #     print('2. 내 주문 내역 확인')
        #     print('3. 회원탈퇴')
        #     print('4. 종료')
        if userCommandNumber == 0:
            if sessionId == -1:
                return CustomProtocol.ACCOUNT_LOGIN.value
            return CustomProtocol.ACCOUNT_LOGOUT.value
        if userCommandNumber == 1:
            if sessionId == -1:
                return CustomProtocol.ACCOUNT_REGISTER.value
        if userCommandNumber == 2:
            if sessionId == -1:
                return CustomProtocol.PRODUCT_LIST.value
            return CustomProtocol.ORDER_LIST.value
        if userCommandNumber == 3:
            if sessionId == -1:
                return CustomProtocol.EXIT.value
            return CustomProtocol.ACCOUNT_REMOVE.value
        if userCommandNumber == 4:
            return CustomProtocol.EXIT.value
        else:
            print('잘못 입력하셨습니다. 다시 입력하세요!')
