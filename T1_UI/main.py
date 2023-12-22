from client_socket.repository.ClientSocketRepositoryImpl import ClientSocketRepositoryImpl
from client_socket.service.ClientSocketServiceImpl import ClientSocketServiceImpl


def initClientSocketDomain():
    clientSocketRepository = ClientSocketRepositoryImpl()
    clientSocketService = ClientSocketServiceImpl(clientSocketRepository)


def initEachDomain():
    initClientSocketDomain()


if __name__ == '__main__':
    print(f"Hello World!")
    initEachDomain()