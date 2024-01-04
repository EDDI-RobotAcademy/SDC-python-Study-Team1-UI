import os


class KeyboardInput:
    @classmethod
    def getKeyboardIntegerInputWithOutputMessage(cls, outputString):
        while True:
            try:
                print(f"{outputString} ", end="")
                userInput = os.read(0, 1024)
                return int(userInput)

            except ValueError:
                print("숫자값을 입력해야 합니다!")

            except EOFError:
                pass

    @classmethod
    def getKeyboardStringInputWithOutputMessage(cls, outputString):
        while True:
            try:
                print(f"{outputString} ", end="")
                userInput = os.read(0, 1024)
                return userInput

            except ValueError as e:
                print(f"입력한 문자열 오류: {e}")

            except EOFError:
                pass

