import unittest

from response_generator.service.ResponseGeneratorServiceImpl import ResponseGeneratorServiceImpl


class TestResponseGenerator(unittest.TestCase):

    def test_generate(self):
        sampleListOfDictionaries = [{"name": "상근", "age": 29}, {"name": "장훈", "age": 27}]
        # sampleArgs = 1
        # responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()
        # responseGenerator = responseGeneratorService.findResponseGenerator(protocolNumber=3)
        # response = responseGenerator(sampleArgs)
        # print(response.getIsSuccess())
        # 이렇게 하면 개문제인듯?
        receivedData1 = str({"protocolNumber": 3, "data": sampleListOfDictionaries})
        print(f'{type(receivedData1)}')
        evalData1 = eval(receivedData1)
        print(f'{type(evalData1)}')
        print(evalData1)
        protoNum = evalData1['protocolNumber']
        data = evalData1['data']
        print(protoNum)
        print(data)
        # key 값을 맞추면 저희가 response 객체 내 private 변수에다 argument[0] 요런식으로

    def testBoolTypeResponse(self):
        # Booltype은 다 처리 가능 확인
        # 1, 3, 4, 6, 8, 9, 10, 13
        sampleResponse = {"protocolNumber": 4, "data": True}
        receivedProtocolNumber = sampleResponse['protocolNumber']
        receivedData = sampleResponse['data']
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()
        responseGenerator = responseGeneratorService.findResponseGenerator(receivedProtocolNumber)
        response = responseGenerator(receivedData)
        print(response.getIsSuccess())

    def testDictionaryResponse(self):
        # 2 : account login 같은 경우는 아래와 같이 처리했습니다.
        sessionId = {'__accountSessionId': 3}  # 현재 저장하고 있는 스타일이 왼쪽과 같은 dict 형태입니다.
        # 따라서 아래와 같이 처리합니다.
        print(int(sessionId.get('__accountSessionId')))

        # 7, 12
        sampleResponse = {"protocolNumber": 7, "data": {'__productId': 1, '__productName': "Sibal",
                                                        "__productPrice": 20000, "__productDetails": "Dog Sibal",
                                                        '__seller': "me"}}
        receivedProtocolNumber = sampleResponse['protocolNumber']
        receivedData = sampleResponse['data']
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()
        responseGenerator = responseGeneratorService.findResponseGenerator(receivedProtocolNumber)
        response = responseGenerator(receivedData)
        print(response.getId())
        print(response.getName())
        print(response.getPrice())
        print(response.getDetails())
        print(response.getAccountId())

    def testListResponse(self):
        # 5, 11
        sampleResponse = {"protocolNumber": 5, "data": [{'__productId': 1, '__productName': "Sibal",
                                                         "__productPrice": 20000},
                                                        {'__productId': 2, '__productName': "Sibal",
                                                         "__productPrice": 30000},
                                                        {'__productId': 3, '__productName': "Sibal",
                                                         "__productPrice": 1818}]}
        receivedProtocolNumber = sampleResponse['protocolNumber']
        receivedData = sampleResponse['data']
        responseGeneratorService = ResponseGeneratorServiceImpl.getInstance()
        responseGenerator = responseGeneratorService.findResponseGenerator(receivedProtocolNumber)
        response = responseGenerator(receivedData)
        # myOrderList = response.getMyOrderList()
        # myOrderListLength = len(myOrderList)
        # print(myOrderListLength)
        # for i in range(myOrderListLength):
        #     print(myOrderList[i])

        productList = response.getProductList()
        productListLength = len(productList)
        print(productListLength)
        for i in range(productListLength):
            print(productList[i])


if __name__ == '__main__':
    unittest.main()
