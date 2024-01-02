import abc


class ProductFormRepository(abc.ABC):

    @abc.abstractmethod
    def createProductRegisterForm(self):
        pass

    @abc.abstractmethod
    def createProductReadForm(self):
        pass

    @abc.abstractmethod
    def createProductModifyForm(self):
        pass

