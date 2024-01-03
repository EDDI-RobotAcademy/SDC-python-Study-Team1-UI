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


if __name__ == '__main__':
    unittest.main()
