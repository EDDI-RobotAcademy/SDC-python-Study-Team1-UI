import unittest
from unittest import mock

from client_socket.repository.ClientSocketRepositoryImpl import ClientSocketRepositoryImpl
from client_socket.service.ClientSocketServiceImpl import ClientSocketServiceImpl


class TestClientSocket(unittest.TestCase):
    def testClientSocketGetInstance(self):
        print(f'Client Socket Instance 가져오고싶어')

        # clientSocketRepository = ClientSocketRepositoryImpl()
        # 위에꺼가 있다고 가정하고 작성하면 아래와 같음
        # mock 은 혁명이다
        clientSocketService = ClientSocketServiceImpl(mock)


if __name__ == '__main__':
    unittest.main()