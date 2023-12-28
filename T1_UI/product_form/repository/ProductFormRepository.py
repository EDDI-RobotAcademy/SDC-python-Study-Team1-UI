import abc

class ProductFormRepository(abc.ABC):

    @abc.abstractmethod
    def createProductWriteForm(self):
        pass

    @abc.abstractmethod
    def createProductModifyForm(self):
        pass

