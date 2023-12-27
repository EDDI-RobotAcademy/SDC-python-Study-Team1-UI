from client_socket.repository.ClientSocketRepositoryImpl import ClientSocketRepositoryImpl
from console_printer.repository.ConsolePrinterRepositoryImpl import ConsolePrinterRepositoryImpl
from receiver.repository.ReceiverRepositoryImpl import ReceiverRepositoryImpl
from task_manage.repository.TaskManageRepositoryImpl import TaskManageRepositoryImpl
from task_manage.service.TaskManageService import TaskManageService
from transmitter.repository.TransmitterRepositoryImpl import TransmitterRepositoryImpl


class TaskManageServiceImpl(TaskManageService):
    __instance = None

    def __new__(cls, repository):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__repository = repository
        return cls.__instance

    def __init__(self, repository):
        print("TaskManageServiceImpl 생성자 호출")
        self.__taskManageRepository = TaskManageRepositoryImpl()

    @classmethod
    def getInstance(cls, repository=None):
        if cls.__instance is None:
            cls.__instance = cls(repository)
        return cls.__instance

    def createTransmitTask(self, lock, transmitQueue):
        transmitterRepository = TransmitterRepositoryImpl.getInstance()
        clientSocketRepository = ClientSocketRepositoryImpl.getInstance()

        # transmitter 있는 transmitCommand를 하는 Task(ps -ef) 생성
        # 신입 사원 뽑았다 생각하면 됨
        self.__taskManageRepository.createTask(
            target=transmitterRepository.transmitCommand,
            args=(clientSocketRepository.getClientSocket(), lock, transmitQueue)
        )

    def createReceiveTask(self, lock, receiveQueue):
        receiverRepository = ReceiverRepositoryImpl.getInstance()
        clientSocketRepository = ClientSocketRepositoryImpl.getInstance()

        self.__taskManageRepository.createTask(
            target=receiverRepository.receiveCommand,
            args=(clientSocketRepository.getClientSocket(), lock, receiveQueue)
        )

    def createPrinterTask(self, transmitQueue, receiveQueue):
        consolePrinterRepository = ConsolePrinterRepositoryImpl.getInstance()

        self.__taskManageRepository.createTask(
            target=consolePrinterRepository.printConsoleUi,
            args=(transmitQueue, receiveQueue, )
        )
