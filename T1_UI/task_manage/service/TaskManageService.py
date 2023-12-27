import abc

class TaskManageService(abc.ABC):
    @abc.abstractmethod
    def createTransmitTask(self, lock, transmitQueue):
        pass

    @abc.abstractmethod
    def createReceiveTask(self, lock, receiveQueue):
        pass