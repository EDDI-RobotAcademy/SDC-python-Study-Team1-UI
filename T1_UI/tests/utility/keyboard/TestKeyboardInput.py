import unittest

from utility.keyboard.KeyboardInput import KeyboardInput


class TestKeyboardInput(unittest.TestCase):
    def testKeyboardIntegerInput(self):
        input = KeyboardInput.getKeyboardIntegerInputWithOutputMessage("숫자: ")
        print(input)

    def testKeyboardStringInput(self):
        input = KeyboardInput.getKeyboardStringInputWithOutputMessage("문자열:", 16)
        print(input)


if __name__ == '__main__':
    unittest.main()
