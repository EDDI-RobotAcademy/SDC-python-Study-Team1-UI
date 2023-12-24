from account_form.repository.AccountFormRepositoryImpl import AccountFormRepositoryImpl
from client_socket.repository.ClientSocketRepositoryImpl import ClientSocketRepositoryImpl
from client_socket.service.ClientSocketServiceImpl import ClientSocketServiceImpl
from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from console_ui.service.ConsoleUiServiceImpl import ConsoleUiServiceImpl

from task_manage.repository.TaskManageRepositoryImpl import TaskManageRepositoryImpl
from task_manage.service.TaskManageServiceImpl import TaskManageServiceImpl


def initClientSocketDomain():
    clientSocketRepository = ClientSocketRepositoryImpl()
    clientSocketService = ClientSocketServiceImpl(clientSocketRepository)


def initTaskManageDomain():
    taskManageRepository = TaskManageRepositoryImpl()
    taskManageService = TaskManageServiceImpl(taskManageRepository)


def initConsoleUiDomain():
    consoleUiRepository = ConsoleUiRepositoryImpl()
    consoleUiService = ConsoleUiServiceImpl(consoleUiRepository)


def initEachDomain():
    initClientSocketDomain()
    initTaskManageDomain()
    initConsoleUiDomain()


if __name__ == '__main__':
    print(f"Hello World!")
    initEachDomain()

    # 당연히 동작하는 것이라 Test 큰 의미 없음
    # accountFormRepository = AccountFormRepositoryImpl()
    # accountFormRepository.createAccountSigninForm()
    # accountFormRepository.createAccountRegisterForm()