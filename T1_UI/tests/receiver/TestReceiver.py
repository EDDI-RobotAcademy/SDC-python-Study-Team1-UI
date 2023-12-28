import unittest
from account.service.response.AccountLoginResponse import AccountLoginResponse


class TestReceiver(unittest.TestCase):
    def testReceiver(self):
        receivedMapDataStr = {"protocol": 2, "data": {"__accountSessionId": 15}}

        wannaBeInQueue = eval(receivedMapDataStr)


if __name__ == '__main__':
    unittest.main()