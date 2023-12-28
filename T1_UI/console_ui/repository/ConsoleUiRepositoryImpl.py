from console_ui.entity.ConsoleUiRoutingState import ConsoleUiRoutingState
from console_ui.entity.ConsoleUiState import ConsoleUiState
from console_ui.entity.Session import Session
from console_ui.repository.ConsoleUiRepository import ConsoleUiRepository
from custom_protocol.entity.CustomProtocol import CustomProtocol


class ConsoleUiRepositoryImpl(ConsoleUiRepository):
    __instance = None
    __menuTable = {}
    __convertCommandTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__menuTable[ConsoleUiRoutingState.INITIALIZED.value] = cls.__instance.__initialMenu

            cls.__instance.__convertCommandTable[
                ConsoleUiRoutingState.INITIALIZED.value] = cls.__instance.__initialStateCommandConverter

        return cls.__instance

    def __init__(self):
        print("ConsoleUiRepositoryImpl 생성자 호출")
        self.__consoleUiState = ConsoleUiState()
        self.__session = Session()

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __initialMenu(self):

        if self.getSessionId() is None:
            print('최초 구동 화면')
            print('1. 회원가입')
            print('2. 로그인')
            print('2. 상품 리스트 조회')
            print('3. 종료')
            return

        print('로그인 후 구동 화면')
        print('1. 로그아웃')
        print('2. 상품 리스트 조회')
        print('3. 내 주문 내역 확인')
        print('4. 회원탈퇴')
        print('5. 종료')

    def __initialStateCommandConverter(self, userCommand):
        if self.getSessionId() is None:
            if userCommand == 1:
                return CustomProtocol.ACCOUNT_REGISTER.value
            if userCommand == 2:
                return CustomProtocol.ACCOUNT_LOGIN.value
            # if userCommand == 3:
            #     return CustomProtocol.PRODUCT_LIST.value
            if userCommand == 4:
                return CustomProtocol.EXIT.value
        if userCommand == 1:
            return CustomProtocol.ACCOUNT_LOGOUT.value
        # if userCommand == 2:
        #     return CustomProtocol.PRODUCT_LIST.value
        # if userCommand == 3:
        #     return CustomProtocol.ORDER_LIST.value
        if userCommand == 4:
            return CustomProtocol.ACCOUNT_REMOVE.value
        if userCommand == 5:
            return CustomProtocol.EXIT.value

    def menuPrinter(self):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()
        menu = self.__menuTable[currentRoutingState]
        # print(f'menu type: {type(menu)}')
        menu()

    def commandConverter(self, userCommand):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()
        converter = self.__convertCommandTable[currentRoutingState]
        return converter(userCommand)

    def routingStateConverter(self, convertedUserChoice):
        if convertedUserChoice == CustomProtocol.ACCOUNT_REGISTER.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.INITIALIZED)

        elif convertedUserChoice == CustomProtocol.ACCOUNT_LOGIN.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.INITIALIZED)

        elif convertedUserChoice == CustomProtocol.ACCOUNT_LOGOUT.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.INITIALIZED)

        elif convertedUserChoice == CustomProtocol.ACCOUNT_REMOVE.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.INITIALIZED)

    def saveCurrentRoutingState(self, currentState):
        self.__consoleUiState.setCurrentRoutingState(currentState)

    def acquireCurrentRoutingState(self):
        return self.__consoleUiState.getCurrentRoutingState()

    def setSessionIdByUserId(self, userId):
        self.__session.setSessionId(userId)

    def getSessionId(self):
        return self.__session.getSessionId()

    def resetSessionId(self):
        self.__session.setSessionId(None)
