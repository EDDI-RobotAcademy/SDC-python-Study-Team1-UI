from time import sleep

from console_printer.repository.ConsolePrinterRepository import ConsolePrinterRepository
from console_ui.entity.ConsoleUiRoutingState import ConsoleUiRoutingState
from console_ui.repository.ConsoleUiRepositoryImpl import ConsoleUiRepositoryImpl
from console_ui.service.ConsoleUiServiceImpl import ConsoleUiServiceImpl


class ConsolePrinterRepositoryImpl(ConsolePrinterRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print("ConsolePrinterRepositoryImpl 생성자 호출")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def printConsoleUi(self, transmitQueue, receiveQueue):

        consoleUiService = ConsoleUiServiceImpl.getInstance()
        consoleUiService.printMenu()
        consoleUiService.processUserInput(transmitQueue)

        while True:
            if not receiveQueue.empty():
                response = receiveQueue.get()
                print(f"Received response: {response}")
                self.__processResponse(response)
                className = response.__class__.__name__
                if className == "ProgramExitResponse":
                    print('Console Printer Off')
                    break
                consoleUiService.printMenu()
                consoleUiService.processUserInput(transmitQueue)
            else:
                sleep(0.5)

    def __processResponse(self, response):

        consoleUiRepository = ConsoleUiRepositoryImpl.getInstance()

        className = response.__class__.__name__

        if className == "AccountRegisterResponse":
            if response.getIsSuccess():
                print('\033[92m회원 가입이 완료되었습니다.\033[0m')

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 회원 가입 실패 (중복된 아이디)\033[0m')

        if className == "AccountLoginResponse":
            if response.getAccountSessionId() is not None:
                consoleUiRepository.setSessionIdByUserId(response.getAccountSessionId())
                print(f'\033[94m로그인이 완료되었습니다. 사용자 아이디:\033[0m {consoleUiRepository.getSessionId()}')
            if response.getAccountSessionId() is None:
                print('\033[91m오류 발생: 로그인 실패 (잘못된 입력)\033[0m')

        if className == "AccountLogoutResponse":
            if response.getIsSuccess():
                print('\033[92m로그아웃이 완료되었습니다.\033[0m')
                consoleUiRepository.resetSessionId()

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 로그아웃 실패\033[0m')

        if className == "AccountDeleteResponse":
            if response.getIsSuccess():
                print('\033[94m계정 삭제가 완료되었습니다.\033[0m')
                consoleUiRepository.resetSessionId()

            if not response.getIsSuccess():
                print('\033[91m오류 발생: 계정 삭제 실패\033[0m')

        if className == "ProductListResponse":
            productList = response.getProductList()
            productListLength = len(productList)
            if productListLength == 0:
                print('등록된 상품이 없습니다.')
                return
            longestProductTitle = len(productList[0]["__productTitle"])
            for i in range(productListLength):

                if longestProductTitle < len(productList[i]["__productTitle"]):
                    longestProductTitle = len(productList[i]["__productTitle"])

            longestProductPrice = int(len(str((productList[0]["__productPrice"]))))
            for i in range(productListLength):

                if longestProductPrice < int(len(str((productList[i]["__productPrice"])))):
                    longestProductPrice = int(len(str((productList[i]["__productPrice"]))))
            print("\033[91m번호", "   ", end="")
            productTitleText = "상품명"
            productPriceText = "가격(원)"
            productTitleWidth = longestProductTitle
            productPriceWidth = longestProductPrice
            centered_productTitleText = productTitleText.center(productTitleWidth, ' ')
            centered_productPriceText = productPriceText.center(productPriceWidth, ' ')
            print(centered_productTitleText, centered_productPriceText)
            for i in range(longestProductPrice + longestProductTitle + 12):
                print("\033[95m=\033[0m", end="")

            print('')

            for i in range(productListLength):
                print(productList[i]["__productNumber"], "     ", end="")
                centerprintname = productList[i]["__productTitle"].center(productTitleWidth, ' ')
                print(centerprintname, "  ", end="")
                centerprintprice = str(productList[i]["__productPrice"]).center(productPriceWidth, ' ')
                print(centerprintprice)

        if className == "ProductReadResponse":
            if response.getId() is not None:
                consoleUiRepository.setProductNumber(response.getId())
                print(f"현재 조회하고 있는 상품 번호 저장 : {consoleUiRepository.getProductNumber()}번")
                print('\033[92m요청하신 상품 정보는 아래와 같습니다.\033[0m')
                print(f'\033[94m상품 번호 :\033[0m {response.getId()}')
                print(f'\033[94m상품 제목 :\033[0m {response.getName()}')
                print(f'\033[92m상품 가격 :\033[0m {response.getPrice()}')
                print(f'\033[94m상품 세부 정보 :\033[0m {response.getDetails()}')
                print(f'\033[92m상품 등록자 :\033[0m {response.getAccountId()}')
            else:
                print('\033[91m오류 발생: 상품 조회 실패 - 존재하지 않는 상품입니다.\033[0m')
                consoleUiRepository.saveCurrentRoutingState(ConsoleUiRoutingState.PRODUCT_LIST.value)

        if className == "ProductRegisterResponse":
            productList = response.getUpdatedProductList()
            productListLength = len(productList)
            longestProductTitle = len(productList[0]["__productTitle"])
            for i in range(productListLength):

                if longestProductTitle < len(productList[i]["__productTitle"]):
                    longestProductTitle = len(productList[i]["__productTitle"])

            longestProductPrice = int(len(str((productList[0]["__productPrice"]))))
            for i in range(productListLength):

                if longestProductPrice < int(len(str((productList[i]["__productPrice"])))):
                    longestProductPrice = int(len(str((productList[i]["__productPrice"]))))
            print("\033[91m번호", "   ", end="")
            productTitleText = "상품명"
            productPriceText = "가격(원)"
            productTitleWidth = longestProductTitle
            productPriceWidth = longestProductPrice
            centered_productTitleText = productTitleText.center(productTitleWidth, ' ')
            centered_productPriceText = productPriceText.center(productPriceWidth, ' ')
            print(centered_productTitleText, centered_productPriceText)
            for i in range(longestProductPrice + longestProductTitle + 12):
                print("\033[95m=\033[0m", end="")

            print('')

            for i in range(productListLength):
                print(productList[i]["__productNumber"], "     ", end="")
                centerprintname = productList[i]["__productTitle"].center(productTitleWidth, ' ')
                print(centerprintname, "  ", end="")
                centerprintprice = str(productList[i]["__productPrice"]).center(productPriceWidth, ' ')
                print(centerprintprice)

        if className == "ProductModifyResponse":
            if response.getId() is not None:
                consoleUiRepository.setProductNumber(response.getId())
                print(f"{consoleUiRepository.getProductNumber()}번 상품 수정이 완료되었습니다.")
                print('\033[92m수정된 상품 정보는 아래와 같습니다.\033[0m')
                print(f'\033[94m상품 번호 :\033[0m {response.getId()}')
                print(f'\033[94m상품 제목 :\033[0m {response.getName()}')
                print(f'\033[92m상품 가격 :\033[0m {response.getPrice()}')
                print(f'\033[94m상품 세부 정보 :\033[0m {response.getDetails()}')
                print(f'\033[92m상품 등록자 :\033[0m {response.getAccountId()}')

            else:
                print('\033[91m오류 발생: 상품 수정 실패 - 권한이 없습니다.\033[0m')

        if className == "ProductPurchaseResponse":
            if response.getId() is not None:
                consoleUiRepository.setProductNumber(response.getId())
                print(f'{response.getId()}번 상품 구매가 완료되었습니다.')
                print(f'\033[94m상품 번호 :\033[0m {response.getId()}')
                print(f'\033[94m상품 제목 :\033[0m {response.getName()}')
                print(f'\033[92m상품 가격 :\033[0m {response.getPrice()}')
                print(f'\033[94m상품 세부 정보 :\033[0m {response.getDetails()}')
                print(f'\033[92m상품 등록자 :\033[0m {response.getAccountId()}')

            else:
                print('\033[91m오류 발생: 상품 구매 실패\033[0m')

        if className == "ProductDeleteResponse":
            if response.getUpdatedProductList() is not None:
                print(f"{consoleUiRepository.getProductNumber()}번 삭제가 완료되었습니다.")
                consoleUiRepository.resetProductNumber()
                productList = response.getUpdatedProductList()
                productListLength = len(productList)
                print(productListLength, "---")
                longestProductTitle = len(productList[0]["__productTitle"])
                for i in range(productListLength):

                    if longestProductTitle < len(productList[i]["__productTitle"]):
                        longestProductTitle = len(productList[i]["__productTitle"])

                longestProductPrice = int(len(str((productList[0]["__productPrice"]))))
                for i in range(productListLength):

                    if longestProductPrice < int(len(str((productList[i]["__productPrice"])))):
                        longestProductPrice = int(len(str((productList[i]["__productPrice"]))))
                print("\033[91m번호", "   ", end="")
                productTitleText = "상품명"
                productPriceText = "가격(원)"
                productTitleWidth = longestProductTitle
                productPriceWidth = longestProductPrice
                centered_productTitleText = productTitleText.center(productTitleWidth, ' ')
                centered_productPriceText = productPriceText.center(productPriceWidth, ' ')
                print(centered_productTitleText, centered_productPriceText)
                for i in range(longestProductPrice + longestProductTitle + 12):
                    print("\033[95m=\033[0m", end="")

                print('')

                for i in range(productListLength):
                    print(productList[i]["__productNumber"], "     ", end="")
                    centerprintname = productList[i]["__productTitle"].center(productTitleWidth, ' ')
                    print(centerprintname, "  ", end="")
                    centerprintprice = str(productList[i]["__productPrice"]).center(productPriceWidth, ' ')
                    print(centerprintprice)

            if response.getUpdatedProductList() is None:
                print('\033[91m오류 발생: 상품 삭제 실패 - 직접 등록하시지 않은 상품입니다.\033[0m')

        if className == "MyOrderListResponse":
            myOrderList = response.getMyOrderList()
            myOrderListLength = len(myOrderList)
            if myOrderListLength == 0:
                print("주문 내역이 없습니다.")
                return
            sum = 0

            longestProductName = len(myOrderList[0]["__productTitle"])

            for i in range(myOrderListLength):

                if longestProductName < len(myOrderList[i]["__productTitle"]):
                    longestProductName = len(myOrderList[i]["__productTitle"])


            longestProductPrice = int(len(str((myOrderList[0]["__productPrice"]))))
            for i in range(myOrderListLength):

                if longestProductPrice < int(len(str((myOrderList[i]["__productPrice"])))):
                    longestProductPrice = int(len(str((myOrderList[i]["__productPrice"]))))

            print("\033[91m번호", "   ", end="")
            myOrderProductName="상품명"
            myOrderProductPrice="가격(원)"
            myOrderProductNameWidth = longestProductName
            myOrderProductPriceWidth = longestProductPrice
            centered_myOrderProductNameText = myOrderProductName.center(myOrderProductNameWidth, ' ')
            centered_myOrderProductPriceText = myOrderProductPrice.center(myOrderProductPriceWidth, ' ')
            print(centered_myOrderProductNameText, centered_myOrderProductPriceText)
            for i in range(longestProductPrice + longestProductName + 12):
                print("\033[95m=\033[0m", end="")

            print('')

            for i in range(myOrderListLength):
                print(myOrderList[i]["__productNumber"], "     ", end="")
                centerprintname = myOrderList[i]["__productTitle"].center(myOrderProductNameWidth, ' ')
                print(centerprintname, "  ", end="")
                centerprintprice = str(myOrderList[i]["__productPrice"]).center(myOrderProductPriceWidth, ' ')
                print(centerprintprice)
                sum += int(myOrderList[i]["__productPrice"])

                for i in range(longestProductPrice + longestProductName + 12):
                    print("\033[95m=\033[0m", end="")

                print('')
                print(f"\033[94m주문 총액 : {sum}원\033[0m")

        if className == "MyOrderReadResponse":
            if response.getId() is not None:
                consoleUiRepository.setProductNumber(response.getId())
                print('\033[94m주문된 상품 정보는 아래와 같습니다.\033[0m')
                print(f'\033[92m상품 번호 :\033[0m {response.getId()}')
                print(f'\033[94m상품 제목 :\033[0m {response.getName()}')
                print(f'\033[92m상품 가격 :\033[0m {response.getPrice()}')
                print(f'\033[94m상품 세부 정보 :\033[0m {response.getDetails()}')
                print(f'\033[92m상품 판매자 :\033[0m {response.getSeller()}')
            else:
                print('\033[91m오류 발생: 주문 상세 조회 실패 - 존재하지 않는 상품입니다.\033[0m')
                consoleUiRepository.saveCurrentRoutingState(ConsoleUiRoutingState.ORDER_LIST.value)

        if className == "MyOrderRemoveResponse":
            myOrderList = response.getMyOrderUpdatedList()
            myOrderListLength = len(myOrderList)
            if myOrderListLength == 0:
                print('주문 내역이 없습니다.')
                return
            sum = 0

            longestProductName = len(myOrderList[0]["__productTitle"])

            for i in range(myOrderListLength):

                if longestProductName < len(myOrderList[i]["__productTitle"]):
                    longestProductName = len(myOrderList[i]["__productTitle"])

            longestProductPrice = int(len(str((myOrderList[0]["__productPrice"]))))
            for i in range(myOrderListLength):

                if longestProductPrice < int(len(str((myOrderList[i]["__productPrice"])))):
                    longestProductPrice = int(len(str((myOrderList[i]["__productPrice"]))))

            print("\033[91m번호", "   ", end="")
            myOrderProductName = "상품명"
            myOrderProductPrice = "가격(원)"
            myOrderProductNameWidth = longestProductName
            myOrderProductPriceWidth = longestProductPrice
            centered_myOrderProductNameText = myOrderProductName.center(myOrderProductNameWidth, ' ')
            centered_myOrderProductPriceText = myOrderProductPrice.center(myOrderProductPriceWidth, ' ')
            print(centered_myOrderProductNameText, centered_myOrderProductPriceText)
            for i in range(longestProductPrice + longestProductName + 12):
                print("\033[95m=\033[0m", end="")

            print('')

            for i in range(myOrderListLength):
                print(myOrderList[i]["__productNumber"], "     ", end="")
                centerprintname = myOrderList[i]["__productTitle"].center(myOrderProductNameWidth, ' ')
                print(centerprintname, "  ", end="")
                centerprintprice = str(myOrderList[i]["__productPrice"]).center(myOrderProductPriceWidth, ' ')
                print(centerprintprice)
                sum += int(myOrderList[i]["__productPrice"])

            for i in range(longestProductPrice + longestProductName + 12):
                print("\033[95m=\033[0m", end="")

            print('')
            print(f"\033[94m주문 총액 : {sum}원\033[0m")

        if className == "ProgramExitResponse":
            if response.getIsSuccess():
                print('''\033[92m           
                                                                                        gBRviirLrrP2Y1v775Lv7L2srrii::::....i:.        ..        .: ..SBBY       
                                                                                       RBbJi:77iv5vi25jJYjYJvrvrviri:ir......   .   ..  .     .    .r: 7BBB.     
                                                                                      gBri::PJ:iv2rq5JUUUIUS1uvYr7r:::::.... .  ...       .   :r    r.  rBBB:    
                                                                                     uBj :7:jYsuqYZqEY1K22suUvLv7r7r:i:.:.... .        ..  .      .    : .BBB    
                                                                                    .BP:iru:.Lu7iIP1UjJPvXXYIJ7Lr7rJri::.:::.  ... . .     ..           i: BBi   
                                                                                    .Bvuri1vrIYr7PK7JSqPJPdSS2Y7Y7Yrur:.... .     ..:i.     ..       ..... .BB   
                                              .    .rDQBBBQBBQKdi                    Q:7::LdqXiKXbYJXgZYrXP1vPjIr:7::i:.iX7. r..           1. :r i:  ..   : :BB5 
                                              5BPBBBBBBBBBBQBBBBBBL                  SK7U1SIILUKbJIqUX1rvIIrv777irvr.:::vi    .:   .i:.  . ......:    .    i.vBB 
                                          iIQBDj7.             .SBBBdi              iX:7vYSXX2J1LIPvJJqSSZ12:7iYYjYY:i::ir.ii:r:.   :.. i: .            .i  .vBB.
                                       .BQBUi                     .RBBI             YLviu51IP1IvUXU1us51gJ55UbIqqSrYJii:: :YLiQ5X :7rU.i2: ..  i :: .  ...   2BB 
                                     rBBJ             1EKu          rBB            iYvi7i2vJqPU2DXYX7:IBuvrsYPss:LuPruiir7vr7viirv:L:r7IS..    r:::.r.       :BB 
                                 .:uBB:             .Bg..LB.         .BB           Bqrr7iJvJP1r7J7sUYPBJ7iirr:7:.:..sjrrrii       . .  .B..:..     .:.  .  .i:BB 
                                QBBB.               jB    gQ           Bj          BrvLrrsbu71Yv:U2PJRP:::v:...7i::..iri:: .         ..:S: .. :. :. ...    i: gB 
                              .BBQ.            .q.       2Q            iB.         BXii:sXbKsIbbiiP577Pr:::.::7r7::.:........         .  57   ::    . .   . . EQi
                             7BBu             dgQj      .BP             BB        .BEY7LU1juIgsiK7Pv:EBr.:..i.:......:::.. ..            iIi.r  :..:  .     : BB.
                            2QBi            iBJ 1M        7BZ           YQ.       UB7.::KI1UvKqvbgL.LBP.:....     . ...:.     YJjSUXPdEv. r::.  .. .  .  . :  BB 
                           ZBB.             ..  rBJKPg.     .LQ.        :BB        iiiirrP5UdvJ1vPIJqq7.. .r2PMgRQQP.  i:  7rE2r     ..:  :L.::  .  .    . :.iBB 
                          PBB          MJ       PQ   :       :P.        LBB7       uBJ:iv7s21UsJ5vdEBg:..YBBP7r:..::.  .: rS: .:1Ir..   ...Yv::  .... :.  .  PBq 
                         iBBJ     :    .BB      Du Jr:B: .7             BBB        rBsr7rsuvis5PSvuKBZ:.:j: .vSKBBuL7.   ... vIiQBB7:. ... .Ir.i :.  ..i..:  BBv 
                         BBB      Bu     7Bv       .BX EBBv            vBBB        :BjsY57KSv1XUrKugX7Y.   JPYugBqi7i.   .:..   .   .   ... :v:i: .  ..ii  r EBr 
                        rBBs      IM   :   Bg        iBBB             rBBBR        .BU:rjYvjS11qrLUKgPi  ...    .:vi     .::.. ....:::.  .  . 7.. .: .....:v.BBi 
                        5BB       YBIPEX :u UBr r    iB:             7BBBQi         :ruIrY7772Xbb7sEQBi  .....:::i.   .  .r:..               5Y:j1UiL :  .. vQB: 
                        BBQ       7B    rB:  .: XB   .              XBQBP            .rur7rviv7j2PuPQd:     ....     .    .i..::          .. rKg..v:   .... BBB  
                        .BB.      5B  iQB       qMB:              .QBBBi             :Bs:YU7vr7L1rSPQg.     ..    r..     .::.. ..         :  5. :i  ..:.i iBBB  
                         :BB      ...BQ rB .i iB:iB:             JBBBB.               BBZuLu11XI755dPR.  .    ..ig.              P:.          ::i. .:. .   BQB:  
                          MB:       Sr   Iv BBB PD             :BBB2                 .BUi5viuisYvQKIjI:      .:sB5i. .      :uLrSi :I:       ..   :...  . jQB2   
                          5BQ                rgBi            2BBBBB                  rB  iUL7Y7J7PX..i:      :UQ:  ..iUqr7LRIi..    .Ib.   . i:.  ..... :ZBBP    
                          iBB:                               .BQBBBBJ                iB :iEs::v7IJURK5X     .PQ. i:.U77JRSv.  ...   : IZ   . i    .    .PBBB     
                           1QBi                         rQBB.  :PBBBBB.               Di:::Q777:LU:rIQB ..  gB::2:.iL7j7i..i..:. JDD5  .  u ..   .     gQBQ      
                             rBP.                    7QBBBBBBQBs2BBQBBB2.             7B Yr:I5 riis7rjur v  Z2 JKgB1...:  . . ..iR2. .   v1 7   :  .i.LBBZ       
                               iSqr.            .sgBQBBBBBBBBBBBBUii..::              vB.:i.igU7vv:ii2r2r:Y  :vv :1Yjv.r::i.vYji     .r: 7 r.  d7:uBBBQB:        
                                  :KBIrr7vJ7sZBQBBBQBBBQBBK7.                         RBi ii.7SqS7i:7:r:77sY:iUUr    iu1X21Lr.  :i  i ..Y  . ..u. RBBBB          
                                    i:.:iuRBBBBBQBR7   :                              BBY .i::i2LJ2PLivr:ruU7iLsi...::       .YR7 .ri      . iE    JBBB          
                                                                                     :BMgi:5vqsiYv15ds1K7.rr:.. :7i .sX1IbPDMgX. i:     .  rrI.     SBBS         
                                                                                     QQRv2L5rSZgZPj5YPPKjiiqY::rr:i:i......i.. ..       .:iPi        dQB.        
                                                                                    7BBB .::v 77J2MsjvI2DJrSJr:7r ..:.  ...:.    . .i ...2q.   ...   iXBBB7      
                                                                                   KBBQE.. ir.7:.ijPuYu1PQv5:..rir.:.....: . ..  r .. .:PI.   ...   :X  rBBBi    
                                                                                 YBQBB2  i1:i:Yivv rDrP7SXvsu7I:.1Jr.ir.:7.:..7  .:   vM1          :b.    .IBBBr 
                                                                              iKBBBBBM7.ir.LMY:u7:PZY.qu2q7:qiPUi:riiLs7vYs::.1:i :.iYBi          :D .       iBBB
                                                                            jBBQBBs7Ss::r:s7YYss.7KL::v:Iu7:Y:7i2r:i.vUJJ7Yi7:.:. ::BE            R..          .B
                                                                          rBBBBQi ::.:.7Ur5X75XSrr.iKir7L5PY2v   uSbuur1rii7::..:7rgY        .   Mr.             

                        \033[0m''')
