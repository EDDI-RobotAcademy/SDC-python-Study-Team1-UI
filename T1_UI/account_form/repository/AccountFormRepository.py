import abc

class AccountFormRepository(abc.ABC):
    @abc.abstractmethod
    def createAccountSigninForm(self):
        pass

    @abc.abstractmethod
    def createAccountRegisterForm(self):
        pass
