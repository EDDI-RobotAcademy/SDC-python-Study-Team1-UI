import unittest

from utility.keyboard.KeyboardInput import KeyboardInput


class TestProductForm(unittest.TestCase):
    def testcreateProductListForm(self):
        print("상품리스트를 띄워줍니다")
        # 서버 db에 저장된 게시물에서 제목 정보 갖고 와서 띄우는건가?

    def testcreateProductWriteForm(self):
        print("상품게시글작성")
        userInputProductTitle = KeyboardInput.getKeyboardInputWithOutputMessage("상품게시글 제목 작성 :")
        userInputProductContent = KeyboardInput.getKeyboardInputWithOutputMessage("상품게시글 내용 작성 :")
        userInputProductPrice = KeyboardInput.getKeyboardInputWithOutputMessage("상품가격 작성 :")
        userInputProductUploader = KeyboardInput.getKeyboardInputWithOutputMessage("상품등록자 작성 :")

    def testcreateProductReadForm(self):
        self.testcreateProductListForm()
        print("원하는 상품게시글 선택하면 그 상품정보 보여줍니다")

if __name__ == '__main__':
        unittest.main()