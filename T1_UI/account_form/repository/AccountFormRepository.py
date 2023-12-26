import abc

class AccountFormRepository(abc.ABC):
    @abc.abstractmethod
    def createAccountSigninForm(self):
        pass

    @abc.abstractmethod
    def createAccountRegistrationForm(self):
        pass