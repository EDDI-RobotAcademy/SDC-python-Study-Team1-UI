import unittest

from utility.keyboard.KeyboardInput import KeyboardInput


class TestKeyboardInput(unittest.TestCase):
    def testKeyboardIntegerInput(self):
        print("Testing keyboard integer input")

        result = KeyboardInput.getKeyboardIntegerInput()
        print(f'result: {result}')

    def testKeyboardStringInput(self):
        print("Testing keyboard string input")

        result = KeyboardInput.getKeyboardInputWithOutputMessage("수행할 명령은:")
        print(f'{result}')


if __name__ == '__main__':
    unittest.main()