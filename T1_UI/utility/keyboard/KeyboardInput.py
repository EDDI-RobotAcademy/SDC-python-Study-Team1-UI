import os


class KeyboardInput:
    @staticmethod
    def getKeyboardIntegerInput():
        while True:
            try:
                print("원하는 선택지를 입력하세요: ", end="")
                userInput = os.read(0, 1024)
                return int(userInput)

            except ValueError:
                print("숫자값을 입력해야 합니다!")

            except EOFError:
                pass

    @staticmethod
    def getKeyboardIntegerInputToReadProduct():
        while True:
            try:
                print("조회할 상품 번호를 입력하세요: ", end="")
                userInput = os.read(0, 1024)
                return int(userInput)

            except ValueError:
                print("숫자값을 입력해야 합니다!")

            except EOFError:
                pass

    @classmethod
    def getKeyboardInputWithOutputMessage(cls, outputString):
        while True:
            try:
                print(f"{outputString} ", end="")
                userInput = os.read(0, 1024)
                return userInput

            except ValueError:
                print("숫자값을 입력해야 합니다!")

            except EOFError:
                pass

