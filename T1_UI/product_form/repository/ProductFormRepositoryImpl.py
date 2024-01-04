from product_form.repository.ProductFormRepository import ProductFormRepository
from utility.keyboard.KeyboardInput import KeyboardInput


class ProductFormRepositoryImpl(ProductFormRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("ProductFormRepositoryImpl 초기화 동작")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createProductRegisterForm(self):
        print("상품 등록을 위한 정보를 입력하세요.")
        userInputProductTitle = KeyboardInput.getKeyboardStringInputWithOutputMessage("신규 상품명:")
        userInputProductContent = KeyboardInput.getKeyboardStringInputWithOutputMessage("신규 상품 상세 정보:")
        userInputProductPrice = KeyboardInput.getKeyboardIntegerInputWithOutputMessage("상품 가격(원):")

        return userInputProductTitle, userInputProductContent, userInputProductPrice

    def createProductReadForm(self):
        userInputProductNumber = KeyboardInput.getKeyboardStringInputWithOutputMessage("조회하실 상품 번호를 입력하세요:")

        return userInputProductNumber

    def createProductModifyForm(self):
        print("상품 수정을 위한 정보를 입력하세요.")
        userInputProductTitle = KeyboardInput.getKeyboardStringInputWithOutputMessage("상품 제목:")
        userInputProductContent = KeyboardInput.getKeyboardStringInputWithOutputMessage("상품 내용 작성:")
        userInputProductPrice = KeyboardInput.getKeyboardIntegerInputWithOutputMessage("상품 가격(원):")

        return userInputProductTitle, userInputProductContent, userInputProductPrice

    def productNothing(self):
        print(f'productNothing: 암것도 없음')
        return None
