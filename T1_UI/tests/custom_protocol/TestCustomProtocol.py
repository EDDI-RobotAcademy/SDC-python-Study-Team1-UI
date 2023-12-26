import unittest

from account_form.repository.AccountFormRepository import AccountFormRepository
from account_form.repository.AccountFormRepositoryImpl import AccountFormRepositoryImpl
from custom_protocol.entity.CustomProtocol import CustomProtocol
from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl


class TestCustomProtocol(unittest.TestCase):

    def accountLoginFormGeneration(self):
        print(f'로그인')


    def accountRegisterFormGeneration(self):
        print(f'회원가입')


    def testCustomProtocolOperation(self):
        firstInstance = CustomProtocolRepositoryImpl.getInstance()
        secondInstance = CustomProtocolRepositoryImpl.getInstance()
        accountFormRepository = AccountFormRepositoryImpl.getInstance()

        # firstInstance.register(1, self.accountLoginFormGeneration)
        # firstInstance.execute(1)
        # firstInstance.register(2, self.accountRegisterFormGeneration)
        # firstInstance.execute(2)

        firstInstance.register(CustomProtocol.ACCOUNT_LOGIN.value, accountFormRepository.createAccountSigninForm)
        firstInstance.execute(0)
        secondInstance.register(CustomProtocol.ACCOUNT_REGISTER.value,
                               accountFormRepository.createAccountRegistrationForm)
        secondInstance.execute(1)


if __name__ == '__main__':
    unittest.main()