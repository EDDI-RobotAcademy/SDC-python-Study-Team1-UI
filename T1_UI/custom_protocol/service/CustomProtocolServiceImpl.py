from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from custom_protocol.service.CustomProtocolService import CustomProtocolService


class CustomProtocolServiceImpl(CustomProtocolService):
    __instance = None

    def __new__(cls, repository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.repository = repository
        return cls.__instance

    def __init__(self, repository):
        print("CustomProtocolServiceImpl 생성자 호출")
        self.__customProtocolRepository = CustomProtocolRepositoryImpl()

    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def registerCustomProtocol(self, protocolNumber, poiterOfFuction):
        self.__customProtocolRepository.register(protocolNumber, poiterOfFuction)
