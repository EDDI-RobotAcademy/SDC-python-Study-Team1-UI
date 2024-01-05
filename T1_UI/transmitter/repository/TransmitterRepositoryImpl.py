import json
import socket
from datetime import datetime
from time import sleep

from custom_protocol.repository.CustomProtocolRepositoryImpl import CustomProtocolRepositoryImpl
from request_generator.service.RequestGeneratorServiceImpl import RequestGeneratorServiceImpl
from transmitter.repository.TransmitterRepository import TransmitterRepository


class TransmitterRepositoryImpl(TransmitterRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("TransmitterRepositoryImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def transmitCommand(self, clientSocketObject, lock, transmitQueue):
        clientSocket = clientSocketObject.getSocket()
        customProtocolRepository = CustomProtocolRepositoryImpl.getInstance()
        requestGeneratorService = RequestGeneratorServiceImpl.getInstance()

        while True:
            with (lock):
                try:
                    protocolAndSessionIdAndProductNumber = transmitQueue.get(block=True)
                    sendProtocol = protocolAndSessionIdAndProductNumber['protocolNumber']
                    sessionId = protocolAndSessionIdAndProductNumber['sessionId']
                    productNumber = protocolAndSessionIdAndProductNumber['productNumber']
                    print(f"Transmitter typeof(sendProtocol) = {type(sendProtocol)}")
                    print(f"Transmitter sendProtocol = {sendProtocol}")
                    print(f"Transmitter sessionId = {sessionId}")
                    print(f"Transmitter productNumber = {productNumber}")

                    request = customProtocolRepository.execute(sendProtocol)
                    print(f"Transmitter Request from repository: {request}")

                    requestGenerator = requestGeneratorService.findRequestGenerator(sendProtocol)
                    print(f"Transmitter Request Generator: {requestGenerator}")

                    #     ACCOUNT_REGISTER = 1
                    #     ACCOUNT_LOGIN = 2
                    #     ACCOUNT_LOGOUT = 3
                    #     ACCOUNT_REMOVE = 4
                    #     PRODUCT_LIST = 5
                    #     PRODUCT_REGISTER = 6
                    #     PRODUCT_READ = 7
                    #     PRODUCT_MODIFY = 8
                    #     PRODUCT_PURCHASE = 9
                    #     PRODUCT_REMOVE = 10
                    #     ORDER_LIST = 11
                    #     ORDER_READ = 12
                    #     ORDER_REMOVE = 13
                    #     EXIT = 14
                    # 아래의 코드를 개선할 필요가 있음
                    # combinedSendingRequest = combinedRequestProcessor(sendProtocol, requestGenerator, request)
                    if sendProtocol == 1 or sendProtocol == 2 or sendProtocol == 5 or \
                        sendProtocol == 6 or sendProtocol == 7:
                        sendingRequest = requestGenerator(request)
                    elif sendProtocol == 3 or sendProtocol == 4 or sendProtocol == 11:
                        sendingRequest = requestGenerator(sessionId)
                    elif sendProtocol == 10:
                        sendingRequest = requestGenerator(productNumber)
                    elif sendProtocol == 8 or sendProtocol == 12:
                        sendingRequest = requestGenerator(productNumber, request)
                    elif sendProtocol == 9 or sendProtocol == 13:
                        sendingRequest = requestGenerator(sessionId, productNumber)

                    print(f"Transmitter finish to generate request: {sendingRequest}")

                    if sendProtocol == 5:
                        combinedRequestData = {
                            'protocol': sendProtocol
                        }
                    else:
                        combinedRequestData = {
                            'protocol': sendProtocol,
                            'data': sendingRequest
                        }

                    combinedRequestDataString = json.dumps(combinedRequestData)

                    print(f"transmitter: will be send - {combinedRequestDataString}")

                    clientSocket.sendall(combinedRequestDataString.encode())

                    print('{} command 전송 [{}]'.format(datetime.now(), sendProtocol))

                except (socket.error, BrokenPipeError) as exception:
                    print(f"사용자 연결 종료")
                    return None

                except socket.error as exception:
                    print(f"전송 중 에러 발생: str{exception}")

                except Exception as exception:
                    print(f"transmitter: 원인을 알 수 없는 에러가 발생하였습니다: {str(exception)}")

                finally:
                    sleep(0.5)


