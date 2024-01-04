from my_order_form.repository.MyOrderFormRepository import MyOrderFormRepository
from utility.keyboard.KeyboardInput import KeyboardInput


class MyOrderFormRepositoryImpl(MyOrderFormRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("MyOrderFormRepositoryImpl 초기화 동작")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createMyOrderReadForm(self):
        userInputMyOrderProductNumber = KeyboardInput.getKeyboardIntegerInputToReadProduct()

        return userInputMyOrderProductNumber

    def myOrderNothing(self):
        print("myOrderNothing: 암것도 없음")
        pass
