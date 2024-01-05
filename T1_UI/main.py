import multiprocessing
import socket
from time import sleep

from decouple import config

from account_form.repository.AccountFormRepositoryImpl import AccountFormRepositoryImpl
from client_socket.repository.ClientSocketRepositoryImpl import ClientSocketRepositoryImpl
from client_socket.service.ClientSocketServiceImpl import ClientSocketServiceImpl
from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from console_ui.service.ConsoleUiServiceImpl import ConsoleUiServiceImpl
from custom_protocol.entity.CustomProtocol import CustomProtocol
from custom_protocol.service.CustomProtocolServiceImpl import CustomProtocolServiceImpl
from my_order_form.repository.MyOrderFormRepositoryImpl import MyOrderFormRepositoryImpl
from product_form.repository.ProductFormRepositoryImpl import ProductFormRepositoryImpl
from program_form.repository.ProgramFormRepositoryImpl import ProgramFormRepositoryImpl

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


def registerProtocol():
    customProtocolService = CustomProtocolServiceImpl.getInstance()
    accountFormRepository = AccountFormRepositoryImpl.getInstance()
    productFormRepository = ProductFormRepositoryImpl.getInstance()
    myOrderFormRepository = MyOrderFormRepositoryImpl.getInstance()
    programFormRepository = ProgramFormRepositoryImpl.getInstance()

    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_LOGIN.value,
        accountFormRepository.createAccountSigninForm
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_REGISTER.value,
        accountFormRepository.createAccountRegisterForm
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_LOGOUT.value,
        accountFormRepository.accountNothing
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ACCOUNT_REMOVE.value,
        accountFormRepository.accountNothing
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_LIST.value,
        productFormRepository.productNothing
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_REGISTER.value,
        productFormRepository.createProductRegisterForm
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_READ.value,
        productFormRepository.createProductReadForm
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_MODIFY.value,
        productFormRepository.createProductModifyForm
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_PURCHASE.value,
        productFormRepository.productNothing
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.PRODUCT_REMOVE.value,
        productFormRepository.productNothing
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ORDER_LIST.value,
        myOrderFormRepository.myOrderNothing
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ORDER_READ.value,
        myOrderFormRepository.createMyOrderReadForm
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.ORDER_REMOVE.value,
        myOrderFormRepository.myOrderNothing
    )
    customProtocolService.registerCustomProtocol(
        CustomProtocol.EXIT.value,
        programFormRepository.programExit
    )


def initConnection():
    clientSocketService = ClientSocketServiceImpl.getInstance()
    clientSocketService.createClientSocket(config('TARGET_HOST'), int(config('PORT')))
    clientSocketService.connectToTargetHost()


def createAllTasks():
    taskManageService = TaskManageServiceImpl.getInstance()

    lock = multiprocessing.Lock()
    transmitQueue = multiprocessing.Queue()
    receiveQueue = multiprocessing.Queue()

    taskManageService.createTransmitTask(lock, transmitQueue)
    taskManageService.createReceiveTask(lock, receiveQueue)
    taskManageService.createPrinterTask(transmitQueue, receiveQueue)


if __name__ == '__main__':
    initEachDomain()
    registerProtocol()
    initConnection()
    createAllTasks()

    while True:
        try:
            sleep(5.0)

        except socket.error:
            sleep(0.5)
