from custom_protocol.repository.CustomProtocolRepository import CustomProtocolRepository


class CustomProtocolRepositoryImpl(CustomProtocolRepository):
    __instance = None
    __customProtocolTable = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__customProtocolTable.append(cls.notImplemented)
        return cls.__instance

    def __init__(self):
        print("CustomProtocolRepositoryImpl 생성자 호출")
        # self.__clientSocket = None

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def notImplemented(self):
        print("아직 구현되지 않은 기능입니다")