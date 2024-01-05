import os


class KeyboardInput:
    @classmethod
    def getKeyboardIntegerInputWithOutputMessage(cls, outputString):
        while True:
            try:
                print(f"{outputString} ", end="")
                userInput = os.read(0, 1024)
                userInputNumber = int(userInput)
                if userInputNumber <= 0:
                    print("유효하지 않은 입력값(선택지 없음, 음수인 가격 입력 등)입니다. 다시 입력하세요!")
                else:
                    return userInputNumber

            except ValueError:
                print("숫자값을 입력해야 합니다!")

            except EOFError:
                pass

    @classmethod
    def getKeyboardStringInputWithOutputMessage(cls, outputString, limitLength):
        while True:
            try:
                print(f"{outputString} ", end="")
                userInput = os.read(0, 1024)
                if userInput.decode().strip() == "":
                    print('아무것도 입력하지 않으셨습니다. 다시 입력하세요!')
                elif len(userInput.decode().strip()) > limitLength:
                    print(f'제한된 byte = {limitLength} 보다 초과 입력하셨습니다. 다시 입력하세요!')
                else:
                    return userInput

            except ValueError as e:
                print(f"입력한 문자열 오류: {e}")

            except EOFError:
                pass

