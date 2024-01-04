import abc


class MyOrderFormRepository(abc.ABC):

    @abc.abstractmethod
    def createMyOrderReadForm(self):
        pass

    @abc.abstractmethod
    def myOrderNothing(self):
        pass
