import unittest

from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl


class TestCustomProtocol(unittest.TestCase):

    def accountLoginFormGeneration(self):
        print(f'로그인')


    def accountRegisterFormGeneration(self):
        print(f'회원가입')


    def testCustomProtocolOperation(self):
        firstInstance = CustomProtocolRepositoryImpl.getInstance()

        firstInstance.register(1, self.accountLoginFormGeneration)
        firstInstance.execute(1)
        firstInstance.register(2, self.accountRegisterFormGeneration)
        firstInstance.execute(2)


if __name__ == '__main__':
    unittest.main()