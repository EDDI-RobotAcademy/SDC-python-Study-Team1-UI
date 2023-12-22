from client_socket.repository.ClientSocketRepository import ClientSocketRepository


class ClientSocketRepositoryImpl(ClientSocketRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("ClientSocketRepositoryImpl 생성자 호출")
        self.__clientSocket = None

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance