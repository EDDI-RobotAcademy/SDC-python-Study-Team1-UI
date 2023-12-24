import abc

class AccountFormRepository(abc.ABC):
    @abc.abstractmethod
    def createAccountSigninForm(self):
        pass

    def createAccountRegistrationForm(self):
        pass