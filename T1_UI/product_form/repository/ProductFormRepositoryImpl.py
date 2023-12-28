from product_form.repository.ProductFormRepository import ProductFormRepository
from utility.keyboard.KeyboardInput import KeyboardInput


class ProductFormRepositoryImpl(ProductFormRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("AccountFormRepositoryImpl 초기화 동작")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance



    def createProductWriteForm(self):
        print("상품게시글작성")
        userInputProductTitle = KeyboardInput.getKeyboardInputWithOutputMessage("상품게시글 제목 작성 :")
        userInputProductContent = KeyboardInput.getKeyboardInputWithOutputMessage("상품게시글 내용 작성 :")
        userInputProductPrice = KeyboardInput.getKeyboardInputWithOutputMessage("상품가격 작성 :")

        return userInputProductTitle, userInputProductContent, userInputProductPrice

    def createProductModifyForm(self):
        print("상품게시글 수정")
        userInputProductTitle = KeyboardInput.getKeyboardInputWithOutputMessage("상품게시글 제목 작성 :")
        userInputProductContent = KeyboardInput.getKeyboardInputWithOutputMessage("상품게시글 내용 작성 :")
        userInputProductPrice = KeyboardInput.getKeyboardInputWithOutputMessage("상품가격 작성 :")

        return return userInputProductTitle, userInputProductContent, userInputProductPrice
