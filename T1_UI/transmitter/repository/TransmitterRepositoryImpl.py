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
                    inMemoryInfo = transmitQueue.get(block=True)

                    sendProtocol = inMemoryInfo['protocolNumber']
                    print(f"Transmitter: sendProtocol = {sendProtocol}")

                    sessionId = inMemoryInfo['sessionId']
                    print(f"Transmitter: sessionId = {sessionId}")

                    productNumber = inMemoryInfo['productNumber']
                    print(f"Transmitter: productNumber = {productNumber}")

                    request = customProtocolRepository.execute(sendProtocol)
                    print(f"Transmitter: Request: {request}")

                    requestGenerator = requestGeneratorService.findRequestGenerator(sendProtocol)
                    print(f"Transmitter: Request Generator: {requestGenerator}")

                    combinedRequestData = self.__combinedRequestProcessor(sendProtocol, sessionId,
                                                                          productNumber, request, requestGenerator)
                    print(f"Transmitter: Combined Request Data: {combinedRequestData}")

                    combinedRequestDataString = json.dumps(combinedRequestData)
                    print(f"transmitter: will be send this string - {combinedRequestDataString}")

                    clientSocket.sendall(combinedRequestDataString.encode())

                    print('{} command 전송 [{}]'.format(datetime.now(), sendProtocol))

                    if sendProtocol == 14:
                        break

                except (socket.error, BrokenPipeError) as exception:
                    print(f"사용자 연결 종료")
                    return None

                except socket.error as exception:
                    print(f"전송 중 에러 발생: str{exception}")

                except Exception as exception:
                    print(f"transmitter: 원인을 알 수 없는 에러가 발생하였습니다: {str(exception)}")

                finally:
                    sleep(0.5)

        print('Transmitter Off')

    def __combinedRequestProcessor(self, protocolNumber, sessionId,
                                   productNumber, requestData, requestGenerator):

        sendingRequest = None

        if (protocolNumber == 1 or protocolNumber == 2 or protocolNumber == 5
                or protocolNumber == 6 or protocolNumber == 7 or protocolNumber == 14):
            sendingRequest = requestGenerator(requestData)

        elif protocolNumber == 3 or protocolNumber == 4 or protocolNumber == 11:
            sendingRequest = requestGenerator(sessionId)

        elif protocolNumber == 8:
            sendingRequest = requestGenerator(productNumber, requestData)

        elif protocolNumber == 9 or protocolNumber == 13:
            sendingRequest = requestGenerator(sessionId, productNumber)

        elif protocolNumber == 10:
            sendingRequest = requestGenerator(productNumber)

        elif protocolNumber == 12:
            sendingRequest = requestGenerator(sessionId, requestData)

        print(f"__combinedRequestGenerator finish to generate request: {sendingRequest}")

        if protocolNumber == 5 or protocolNumber == 14:
            combinedRequestData = {
                'protocol': protocolNumber
            }
        else:
            combinedRequestData = {
                'protocol': protocolNumber,
                'data': sendingRequest
            }

        return combinedRequestData
