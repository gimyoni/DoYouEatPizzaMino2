import sys
import pandas as pd
import self as self
import matplotlib.pyplot as plt
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from pandas import ExcelWriter, DataFrame
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc, pyplot
import platform

if platform.system() == 'Windows':
    # 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    # Mac 인 경우
    rc('font', family='AppleGothic')

matplotlib.rcParams['axes.unicode_minus'] = False
# 그래프에서 마이너스 기호가 표시되도록 하는 설정입니다.
# pizza_result = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet1")
# pizza_tem = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet2")
from test_pandas import makePlot

self.df1 = pd.DataFrame.from_records([{'날짜': '2020-11-30', '메뉴': '피자', '개수': 1, '가격': 3500}])

self.df2 = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet3")


def addResultData(date):
    pizza_result = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet1")
    # new_row = {'날짜': date, '메뉴': name, '개수': amount, '가격': price}
    # self.df1 = self.df2.append(new_row, ignore_index=True)
    #
    # self.df1.to_excel("pizzaInfo.xlsx", sheet_name='Sheet1', index=False)
    print(self.df1)


def addTemData(name, amount, price):
    # pizza_tem = pizza_tem.append({'메뉴': name, '개수': amount, '가격': price}, ignore_index=True)
    # pizza_tem = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet2")

    new_row = {'메뉴': name, '개수': amount, '가격': price}
    self.df2 = self.df2.append(new_row, ignore_index=True)
    self.df2.to_excel("pizzaInfo.xlsx", sheet_name='Sheet3', index=False)
    print()
    print(self.df2)


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.date = QDate.currentDate()

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        start_widget = StartWidget(self)
        start_widget.adv.clicked.connect(self.clickAdv)
        self.central_widget.addWidget(start_widget)

        self.setWindowTitle('PizzaKiosk')
        self.setWindowIcon(QIcon('images/dominoLogo.png'))
        self.setFixedSize(800, 950)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clickAdv(self):
        order_widget = OrderWidget(self)
        order_widget.pizzaBtn.clicked.connect(self.clickFame)
        order_widget.subBtn.clicked.connect(self.clickSub)
        order_widget.buyBtn.clicked.connect(self.clickBuy)

        open('nowPizzaCart.txt', 'w').close()
        open('nowSubCart.txt', 'w').close()

        self.central_widget.addWidget(order_widget)
        self.central_widget.setCurrentWidget(order_widget)

    def clickFame(self):
        fame_widget = FameWidget(self)
        fame_widget.recommendBtn.clicked.connect(self.clickRec1)
        fame_widget.premiumBtn.clicked.connect(self.clickPre1)
        fame_widget.classicBtn.clicked.connect(self.clickCla1)
        fame_widget.orderBtn.clicked.connect(self.click_back)

        self.central_widget.addWidget(fame_widget)
        self.central_widget.setCurrentWidget(fame_widget)

    def clickSub(self):
        sub_widget = SubWidget(self)
        sub_widget.sidedishBtn.clicked.connect(self.clickSub_side)
        sub_widget.drinkBtn.clicked.connect(self.clickSub_drink)
        sub_widget.etcBtn.clicked.connect(self.clickSub_etc)

        sub_widget.rec1Btn.clicked.connect(
            lambda img_name="tomato_pasta", name="셰프’s 토마토 파스타", price=9800, menu="sidedish": self.click_menu2(img_name,
                                                                                                               name,
                                                                                                               price,
                                                                                                               menu))
        sub_widget.rec2Btn.clicked.connect(
            lambda img_name="basil_pasta", name="셰프’s 트러플 바질 파스타", price=9800, menu="sidedish": self.click_menu2(
                img_name, name, price, menu))
        sub_widget.rec3Btn.clicked.connect(
            lambda img_name="rose_pasta", name="스파이시 씨푸드 로제 파스타", price=8800, menu="sidedish": self.click_menu2(
                img_name,
                name,
                price, menu))

        self.central_widget.addWidget(sub_widget)
        self.central_widget.setCurrentWidget(sub_widget)

    def clickRec1(self):
        rec_widget = RecWidget_1(self)
        rec_widget.fameBtn.clicked.connect(self.clickFame)
        rec_widget.premiumBtn.clicked.connect(self.clickPre1)
        rec_widget.classicBtn.clicked.connect(self.clickCla1)
        rec_widget.orderBtn.clicked.connect(self.click_back)

        rec_widget.prevBtn.clicked.connect(self.clickRec3)
        rec_widget.nextBtn.clicked.connect(self.clickRec2)

        self.central_widget.addWidget(rec_widget)
        self.central_widget.setCurrentWidget(rec_widget)

    def clickRec2(self):
        rec_widget = RecWidget_2(self)
        rec_widget.fameBtn.clicked.connect(self.clickFame)
        rec_widget.premiumBtn.clicked.connect(self.clickPre1)
        rec_widget.classicBtn.clicked.connect(self.clickCla1)
        rec_widget.orderBtn.clicked.connect(self.click_back)

        rec_widget.prevBtn.clicked.connect(self.clickRec1)
        rec_widget.nextBtn.clicked.connect(self.clickRec3)

        self.central_widget.addWidget(rec_widget)
        self.central_widget.setCurrentWidget(rec_widget)

    def clickRec3(self):
        rec_widget = RecWidget_3(self)
        rec_widget.fameBtn.clicked.connect(self.clickFame)
        rec_widget.premiumBtn.clicked.connect(self.clickPre1)
        rec_widget.classicBtn.clicked.connect(self.clickCla1)
        rec_widget.orderBtn.clicked.connect(self.click_back)

        rec_widget.prevBtn.clicked.connect(self.clickRec2)
        rec_widget.nextBtn.clicked.connect(self.clickRec1)

        self.central_widget.addWidget(rec_widget)
        self.central_widget.setCurrentWidget(rec_widget)

    def clickPre1(self):
        pre1_widget = PreWidget_1(self)
        pre1_widget.fameBtn.clicked.connect(self.clickFame)
        pre1_widget.recommendBtn.clicked.connect(self.clickRec1)
        pre1_widget.classicBtn.clicked.connect(self.clickCla1)
        pre1_widget.orderBtn.clicked.connect(self.click_back)

        pre1_widget.pz1Btn.clicked.connect(
            lambda img_name="starChefSignature", name="스타 셰프 시그니처", size_l=36900, size_m=29900: self.click_menu(
                img_name, name, size_l, size_m))
        pre1_widget.pz2Btn.clicked.connect(
            lambda img_name="starChefTruffleBazil", name="스타 셰프 트러플 바질", size_l=36900, size_m=29900: self.click_menu(
                img_name, name, size_l, size_m))
        pre1_widget.pz3Btn.clicked.connect(
            lambda img_name="globalLegend4", name="글로벌 레전드4", size_l=35900, size_m=29000: self.click_menu(img_name,
                                                                                                          name, size_l,
                                                                                                          size_m))
        pre1_widget.pz4Btn.clicked.connect(
            lambda img_name="serialChilliCrab", name="시리얼 칠리크랩", size_l=34900, size_m=29000: self.click_menu(img_name,
                                                                                                             name,
                                                                                                             size_l,
                                                                                                             size_m))
        pre1_widget.pz5Btn.clicked.connect(
            lambda img_name="cheeseCakeBlackTiger", name="치즈케이크 블랙타이거", size_l=35900, size_m=29000: self.click_menu(
                img_name, name, size_l, size_m))
        pre1_widget.pz6Btn.clicked.connect(
            lambda img_name="30CheeseNewYorkStripStake", name="30 치즈&뉴욕 스트립 스테이크", size_l=34900,
                   size_m=29000: self.click_menu(img_name, name, size_l, size_m))

        pre1_widget.nextBtn.clicked.connect(self.clickPre2)

        self.central_widget.addWidget(pre1_widget)
        self.central_widget.setCurrentWidget(pre1_widget)

    def clickPre2(self):
        pre2_widget = PreWidget_2(self)
        pre2_widget.fameBtn.clicked.connect(self.clickFame)
        pre2_widget.recommendBtn.clicked.connect(self.clickRec1)
        pre2_widget.classicBtn.clicked.connect(self.clickCla1)
        pre2_widget.orderBtn.clicked.connect(self.click_back)

        pre2_widget.pz1Btn.clicked.connect(
            lambda img_name="blackAngersStake", name="블랙앵거스 스테이크", size_l=34900, size_m=29000, i=0: self.click_menu(
                img_name, name, size_l, size_m))
        pre2_widget.pz2Btn.clicked.connect(
            lambda img_name="bestQuattro", name="베스트 콰트로", size_l=34900, size_m=29000: self.click_menu(img_name, name,
                                                                                                       size_l, size_m))
        pre2_widget.pz3Btn.clicked.connect(
            lambda img_name="blackTigerShrimp", name="블랙타이거 슈림프", size_l=34900, size_m=29000: self.click_menu(img_name,
                                                                                                              name,
                                                                                                              size_l,
                                                                                                              size_m))
        pre2_widget.pz4Btn.clicked.connect(
            lambda img_name="zikhwaStake", name="직화 스테이크", size_l=33900, size_m=28000: self.click_menu(img_name, name,
                                                                                                       size_l, size_m))

        pre2_widget.prevBtn.clicked.connect(self.clickPre1)

        self.central_widget.addWidget(pre2_widget)
        self.central_widget.setCurrentWidget(pre2_widget)

    def click_menu(self, img_name, name, sizeL, sizeM):
        about_widget = AboutWidget(self)
        about_widget.setting(img_name, name, sizeL, sizeM)
        about_widget.backBtn.clicked.connect(self.click_back)

        self.central_widget.addWidget(about_widget)
        self.central_widget.setCurrentWidget(about_widget)

    def click_back(self):
        order_widget = OrderWidget(self)
        order_widget.pizzaBtn.clicked.connect(self.clickFame)
        order_widget.subBtn.clicked.connect(self.clickSub)
        order_widget.buyBtn.clicked.connect(self.clickBuy)

        self.central_widget.addWidget(order_widget)
        self.central_widget.setCurrentWidget(order_widget)

    def clickBuy(self):
        option = QMessageBox.question(self, "구매", "구매창으로 넘어갑니다",
                                      QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if option == QMessageBox.Yes:
            buy_widget = BuyWidget(self)

            buy_widget.turnBtn.clicked.connect(self.clickTurn)
            self.central_widget.addWidget(buy_widget)
            self.central_widget.setCurrentWidget(buy_widget)

    def clickTurn(self):
        buy_widget = StartWidget(self)

        buy_widget.adv.clicked.connect(self.clickAdv)
        self.central_widget.addWidget(buy_widget)
        self.central_widget.setCurrentWidget(buy_widget)

    def clickCla1(self):
        cla1_widget = ClaWidget_1(self)
        cla1_widget.fameBtn.clicked.connect(self.clickFame)
        cla1_widget.recommendBtn.clicked.connect(self.clickRec1)
        cla1_widget.premiumBtn.clicked.connect(self.clickPre1)
        cla1_widget.orderBtn.clicked.connect(self.click_back)

        cla1_widget.pz1Btn.clicked.connect(
            lambda img_name="realBulgogi", name="리얼 불고기", size_l=27900, size_m=21000: self.click_menu(
                img_name, name, size_l, size_m))
        cla1_widget.pz2Btn.clicked.connect(
            lambda img_name="cheeseGarden", name="치즈 가든", size_l=27900, size_m=21000: self.click_menu(
                img_name, name, size_l, size_m))
        cla1_widget.pz3Btn.clicked.connect(
            lambda img_name="ourGoguma", name="우리고구마", size_l=29900, size_m=23000: self.click_menu(
                img_name, name, size_l, size_m))
        cla1_widget.pz4Btn.clicked.connect(
            lambda img_name="potato", name="포테이토", size_l=25900, size_m=19000: self.click_menu(
                img_name, name, size_l, size_m))
        cla1_widget.pz5Btn.clicked.connect(
            lambda img_name="superDelux", name="슈퍼디럭스", size_l=25900, size_m=19000: self.click_menu(
                img_name, name, size_l, size_m))
        cla1_widget.pz6Btn.clicked.connect(
            lambda img_name="superSupreme", name="슈퍼스프림", size_l=25900, size_m=19000: self.click_menu(
                img_name, name, size_l, size_m))

        cla1_widget.nextBtn.clicked.connect(self.clickCla2)

        self.central_widget.addWidget(cla1_widget)
        self.central_widget.setCurrentWidget(cla1_widget)

    def clickCla2(self):
        cla1_widget = ClaWidget_2(self)
        cla1_widget.fameBtn.clicked.connect(self.clickFame)
        cla1_widget.recommendBtn.clicked.connect(self.clickRec1)
        cla1_widget.premiumBtn.clicked.connect(self.clickPre1)
        cla1_widget.orderBtn.clicked.connect(self.click_back)

        cla1_widget.pz1Btn.clicked.connect(
            lambda img_name="bacconCheddarCheese", name="베이컨체더치즈", size_l=36900, size_m=29900: self.click_menu(
                img_name, name, size_l, size_m))
        cla1_widget.pz2Btn.clicked.connect(
            lambda img_name="pepperoni", name="페퍼로니", size_l=36900, size_m=29900: self.click_menu(
                img_name, name, size_l, size_m))
        cla1_widget.pz3Btn.clicked.connect(
            lambda img_name="cheese", name="치즈", size_l=35900, size_m=29000: self.click_menu(
                img_name, name, size_l, size_m))

        cla1_widget.prevBtn.clicked.connect(self.clickCla1)

        self.central_widget.addWidget(cla1_widget)
        self.central_widget.setCurrentWidget(cla1_widget)

    def clickSub_side(self):
        rec_widget = Sub_SideWidget1(self)
        rec_widget.recommendBtn.clicked.connect(self.clickSub)
        rec_widget.sidedishBtn.clicked.connect(self.clickSub_side)
        rec_widget.drinkBtn.clicked.connect(self.clickSub_drink)
        rec_widget.etcBtn.clicked.connect(self.clickSub_etc)

        rec_widget.rec1Btn.clicked.connect(
            lambda img_name="tomato_pasta", name="셰프’s 토마토 파스타", price=9800, menu="sidedish": self.click_menu2(img_name,
                                                                                                               name,
                                                                                                               price,
                                                                                                               menu))
        rec_widget.rec2Btn.clicked.connect(
            lambda img_name="basil_pasta", name="셰프’s 트러플 바질 파스타", price=9800, menu="sidedish": self.click_menu2(
                img_name, name, price, menu))
        rec_widget.rec3Btn.clicked.connect(
            lambda img_name="rose_pasta", name="스파이시 씨푸드 로제 파스타", price=8800, menu="sidedish": self.click_menu2(
                img_name,
                name,
                price,
                menu))
        rec_widget.rec4Btn.clicked.connect(
            lambda img_name="crispy_chicken", name="크리스피 핫 순살 치킨(8조각)", price=4800, menu="sidedish": self.click_menu2(
                img_name, name,
                price, menu))
        rec_widget.rec5Btn.clicked.connect(
            lambda img_name="salad", name="샐러드 가든", price=6800, menu="sidedish": self.click_menu2(img_name, name, price,
                                                                                                  menu))
        rec_widget.rec6Btn.clicked.connect(
            lambda img_name="penne_pasta", name="펜네 파스타", price=8800, menu="sidedish": self.click_menu2(img_name, name,
                                                                                                        price, menu))

        rec_widget.nextBtn.clicked.connect(self.clickSub_side_next)

        self.central_widget.addWidget(rec_widget)
        self.central_widget.setCurrentWidget(rec_widget)

    def clickSub_side_next(self):
        rec_widget = Sub_SideWidget2(self)
        rec_widget.recommendBtn.clicked.connect(self.clickSub)
        rec_widget.sidedishBtn.clicked.connect(self.clickSub_side)
        rec_widget.drinkBtn.clicked.connect(self.clickSub_drink)
        rec_widget.etcBtn.clicked.connect(self.clickSub_etc)

        rec_widget.rec1Btn.clicked.connect(
            lambda img_name="grain_chicken", name="슈퍼곡물 치킨(10조각)", price=7800, menu="sidedish": self.click_menu2(
                img_name, name, price, menu))
        rec_widget.rec2Btn.clicked.connect(
            lambda img_name="bolognese_spaghetti", name="NEW 치즈 볼로네즈 스파게티", price=8800,
                   menu="sidedish": self.click_menu2(img_name, name,
                                                    price, menu))
        rec_widget.rec3Btn.clicked.connect(
            lambda img_name="truffle_risotto", name="트러플 리조또", price=8800, menu="sidedish": self.click_menu2(img_name,
                                                                                                            name, price,
                                                                                                            menu))
        rec_widget.rec4Btn.clicked.connect(
            lambda img_name="half_spaghetti", name="하프&하프 스파게티 (NEW 치즈 & 화이트 크림)", price=9800,
                   menu="sidedish": self.click_menu2(img_name,
                                                    name,
                                                    price, menu))
        rec_widget.rec5Btn.clicked.connect(
            lambda img_name="cream_spaghetti", name="화이트 크림 스파게티", price=8800, menu="sidedish": self.click_menu2(
                img_name, name, price, menu))
        rec_widget.rec6Btn.clicked.connect(
            lambda img_name="wings", name="갈릭&허브윙스(8조각)", price=8800, menu="sidedish": self.click_menu2(img_name, name,
                                                                                                       price, menu))

        rec_widget.prevBtn.clicked.connect(self.clickSub_side)

        self.central_widget.addWidget(rec_widget)
        self.central_widget.setCurrentWidget(rec_widget)

    def clickSub_drink(self):
        rec_widget = Sub_DrinkWidget(self)
        rec_widget.recommendBtn.clicked.connect(self.clickSub)
        rec_widget.sidedishBtn.clicked.connect(self.clickSub_side)
        rec_widget.drinkBtn.clicked.connect(self.clickSub_drink)
        rec_widget.etcBtn.clicked.connect(self.clickSub_etc)

        rec_widget.rec1Btn.clicked.connect(
            lambda img_name="cola1.25", name="코카콜라 1.25L", price=2000, menu="drink": self.click_menu(img_name, name,
                                                                                                     price, menu))
        rec_widget.rec2Btn.clicked.connect(
            lambda img_name="cola500", name="코카콜라 500ml", price=1400, menu="drink": self.click_menu(img_name, name,
                                                                                                    price, menu))
        rec_widget.rec3Btn.clicked.connect(
            lambda img_name="zerocola1.5", name="코카콜라 제로 1.5L", price=2100, menu="drink": self.click_menu(img_name,
                                                                                                          name, price,
                                                                                                          menu))
        rec_widget.rec4Btn.clicked.connect(
            lambda img_name="zerocola500", name="코카콜라 제로 500ml", price=1300, menu="drink": self.click_menu(img_name,
                                                                                                           name,
                                                                                                           price, menu))
        rec_widget.rec5Btn.clicked.connect(
            lambda img_name="sprite1.5", name="스프라이트 1.5L", price=2100, menu="drink": self.click_menu(img_name, name,
                                                                                                      price, menu))
        rec_widget.rec6Btn.clicked.connect(
            lambda img_name="sprite500", name="스프라이트 500ml", price=1300, menu="drink": self.click_menu(img_name, name,
                                                                                                       price, menu))

        self.central_widget.addWidget(rec_widget)
        self.central_widget.setCurrentWidget(rec_widget)

    def clickSub_etc(self):
        rec_widget = Sub_EtcWidget(self)
        rec_widget.recommendBtn.clicked.connect(self.clickSub)
        rec_widget.sidedishBtn.clicked.connect(self.clickSub_side)
        rec_widget.drinkBtn.clicked.connect(self.clickSub_drink)
        rec_widget.etcBtn.clicked.connect(self.clickSub_etc)

        rec_widget.rec1Btn.clicked.connect(
            lambda img_name="picklel", name="우리 피클 L", price=800, menu="etc": self.click_menu(img_name, name,
                                                                                              price, menu))
        rec_widget.rec2Btn.clicked.connect(
            lambda img_name="picklem", name="우리 피클 M", price=500, menu="etc": self.click_menu(img_name, name, price,
                                                                                              menu))
        rec_widget.rec3Btn.clicked.connect(
            lambda img_name="cereal", name="도미노 시리얼", price=400, menu="etc": self.click_menu(img_name, name, price,
                                                                                             menu))
        rec_widget.rec4Btn.clicked.connect(
            lambda img_name="chilisauce", name="스위트 칠리소스 15g", price=300, menu="etc": self.click_menu(img_name, name,
                                                                                                      price, menu))
        rec_widget.rec5Btn.clicked.connect(
            lambda img_name="garlicsauce", name="갈릭 디핑 소스 15g", price=200, menu="etc": self.click_menu(img_name, name,
                                                                                                       price, menu))
        rec_widget.rec6Btn.clicked.connect(
            lambda img_name="hotsauce", name="핫소스", price=100, menu="drink": self.click_menu(img_name, name, price,
                                                                                             menu))

        self.central_widget.addWidget(rec_widget)
        self.central_widget.setCurrentWidget(rec_widget)

    def click_subMenu(self, img_name, name, price):
        about_widget = SubAboutWidget(self)
        about_widget.test(img_name, name, price)
        about_widget.backBtn.clicked.connect(self.click_back)

        self.central_widget.addWidget(about_widget)
        self.central_widget.setCurrentWidget(about_widget)

    def click_menu2(self, img_name, name, price, menu):
        about_widget = SubAboutWidget(self)
        about_widget.test(img_name, name, price, menu)
        self.central_widget.addWidget(about_widget)
        self.central_widget.setCurrentWidget(about_widget)


class StartWidget(QWidget):
    def __init__(self, parent=None):
        super(StartWidget, self).__init__(parent)

        self.date = QDate.currentDate()
        self.time = QTime.currentTime()

        self.startBack = QLabel(self)
        self.startBack.resize(800, 950)
        pixmap = QPixmap("images/startBack.png")
        self.startBack.setPixmap(QPixmap(pixmap))

        self.realDate = QLabel(self.date.toString(Qt.ISODate), self.startBack)
        self.realDate.move(500, 60)
        self.realDate.setFont(QFont("여기어때 잘난체 OTF", 20))
        self.realDate.setStyleSheet("Color : white")

        self.realTime = QLabel(self.time.toString(Qt.DefaultLocaleShortDate), self.startBack)
        self.realTime.move(500, 110)
        self.realTime.setFont(QFont("여기어때 잘난체 OTF", 20))
        self.realTime.setStyleSheet("Color : white")

        self.adv = QPushButton('광고', self.startBack)
        self.adv.resize(700, 700)
        self.adv.move(50, 200)


class OrderWidget(QWidget):
    def __init__(self, parent=None):
        super(OrderWidget, self).__init__(parent)

        self.orderBack = QLabel(self)
        self.orderBack.resize(800, 950)
        pixmap = QPixmap("images/orderBack.png")
        self.orderBack.setPixmap(QPixmap(pixmap))

        self.pizzaBtn = QPushButton('피자', self.orderBack)
        self.pizzaBtn.resize(200, 200)
        self.pizzaBtn.move(50, 200)

        self.subBtn = QPushButton('서브메뉴 및 콜라', self.orderBack)
        self.subBtn.resize(200, 200)
        self.subBtn.move(300, 200)

        self.cart = QLabel(self)
        self.cart.move(50, 850)
        self.cart.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.buyBtn = QPushButton('구매하기', self.orderBack)
        self.buyBtn.resize(200, 200)
        self.buyBtn.move(500, 800)
        # self.buyBtn.clicked.connect(self.clickCart)

        self.myCartLabel = QLabel("---------장바구니----------", self)
        self.myCartInfo = QLabel("", self)
        self.allPrice = QLabel("", self)

        self.myCartLabel.setFont(QFont("여기어때 잘난체 OTF", 10))
        self.myCartInfo.setFont(QFont("여기어때 잘난체 OTF", 10))
        self.allPrice.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.myCartLabel.move(50, 400)
        self.myCartInfo.move(50, 420)
        self.allPrice.move(50, 700)

        self.cartPrice = 0
        self.showCart()

    # def clickCart(self):
    #     count = 0
    #     option = QMessageBox.question(self, "구매", "구매하시겠습니까?",
    #                                       QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
    #     if option == QMessageBox.Yes:
    #
    #         with open('nowPizzaCart.txt') as file:
    #             for line in file.readlines():
    #                 result = line.strip().split('\t')
    #                 name = result[0]
    #                 amount = result[1]
    #                 price = result[2]
    #                 count += int(result[1])
    #                 addTemData(name, amount, price)
    #         #open('nowPizzaCart.txt', 'w').close()
    #
    #         with open('nowSubCart.txt') as file:
    #             for line in file.readlines():
    #                 result = line.strip().split('\t')
    #                 name = result[0]
    #                 amount = result[1]
    #                 price = result[2]
    #                 #self.myCartInfo.setText(
    #         #open('nowSubCart.txt', 'w').close()

    def showCart(self):
        count = 0

        with open('nowPizzaCart.txt') as file:
            for line in file.readlines():
                result = line.strip().split('\t')
                name = result[0]
                amount = result[1]
                price = result[2]
                count += int(result[1])
                self.cartPrice += int(price)
                self.myCartInfo.setText(self.myCartInfo.text() + name + " " + str(amount) + "개 " + str(price) + "원\n")

        with open('nowSubCart.txt') as file:
            for line in file.readlines():
                result = line.strip().split('\t')
                name = result[0]
                amount = result[1]
                price = result[2]
                self.cartPrice += int(price)
                self.myCartInfo.setText(self.myCartInfo.text() + name + " " + str(amount) + "개 " + str(price) + "원\n")

        self.allPrice.setText("총 금액 " + str(self.cartPrice))


class BuyWidget(QWidget):
    def __init__(self, parent=None):
        super(BuyWidget, self).__init__(parent)
        num = 100
        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/toppingBack.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.myCartLabel = QLabel("---------장바구니----------", self)
        self.myCartInfo = QLabel("", self)
        self.allPrice = QLabel("", self)

        self.myCartLabel.setFont(QFont("여기어때 잘난체 OTF", 10))
        self.myCartInfo.setFont(QFont("여기어때 잘난체 OTF", 10))
        self.allPrice.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.myCartLabel.move(50, 400)
        self.myCartInfo.move(50, 420)
        self.allPrice.move(50, 700)

        count = 0
        self.cartPrice = 0
        with open('nowPizzaCart.txt') as file:
            for line in file.readlines():
                result = line.strip().split('\t')
                name = result[0]
                amount = result[1]
                price = result[2]
                count += int(result[1])
                self.cartPrice += int(price)
                self.myCartInfo.setText(self.myCartInfo.text() + name + " " + str(amount) + "개 " + str(price) + "원\n")
        open('nowPizzaCart.txt', 'w').close()
        with open('nowSubCart.txt') as file:
            for line in file.readlines():
                result = line.strip().split('\t')
                name = result[0]
                amount = result[1]
                price = result[2]
                self.cartPrice += int(price)
                self.myCartInfo.setText(self.myCartInfo.text() + name + " " + str(amount) + "개 " + str(price) + "원\n")
        open('nowSubCart.txt', 'w').close()
        self.allPrice.setText("총 금액 " + str(self.cartPrice) + "이 결제 되었습니다.\n주문 번호 : " + str(num))
        num += 1

        self.turnBtn = QPushButton('처음으로', self)
        self.turnBtn.resize(200, 200)
        self.turnBtn.move(500, 500)

        # 자동으로 돌아가게도 만들 것


class FameWidget(QWidget):
    def __init__(self, parent=None):
        super(FameWidget, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/pizzamenu/famePizza.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 100)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 100)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 100)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 100)

        self.orderBtn = QPushButton("<", self)
        self.orderBtn.resize(80, 80)
        self.orderBtn.move(10, 10)

        opacity = QGraphicsOpacityEffect(self.fameBtn)
        opacity.setOpacity(0)
        self.fameBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.premiumBtn)
        opacity.setOpacity(0)
        self.premiumBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.classicBtn)
        opacity.setOpacity(0)
        self.classicBtn.setGraphicsEffect(opacity)

        self.showPlot()

    def showPlot(self):
        makePlot()
        self.plotImg = QLabel(self)
        self.plotImg.setScaledContents(True)
        self.plotImg.setGeometry(QRect(50, 300, 650, 500))
        pixmap = QPixmap("plot.png")
        self.plotImg.setPixmap(QPixmap(pixmap))
        self.plotImg.repaint()


class RecWidget_1(QWidget):
    def __init__(self, parent=None):
        super(RecWidget_1, self).__init__(parent)

        self.recPz = QLabel(self)
        self.recPz.resize(800, 950)
        pixmap = QPixmap("images/pizzamenu/recPizza.png")
        self.recPz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 100)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 100)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 100)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 100)

        self.orderBtn = QPushButton("<", self)
        self.orderBtn.resize(80, 80)
        self.orderBtn.move(10, 10)

        opacity = QGraphicsOpacityEffect(self.fameBtn)
        opacity.setOpacity(0)
        self.fameBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.premiumBtn)
        opacity.setOpacity(0)
        self.premiumBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.classicBtn)
        opacity.setOpacity(0)
        self.classicBtn.setGraphicsEffect(opacity)

        self.pz1 = QLabel(self)
        self.pzName1 = QLabel("스타 쉐프 시그니쳐", self)
        self.pzPrice1 = QLabel("L 36900원~ M 29900원~", self)
        self.pzExplain1 = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pz1Btn = QPushButton(self)

        self.makeMenu(self.pz1, self.pzName1, self.pzPrice1, self.pzExplain1, self.pz1Btn, 80, 250, "starChefSignature",
                      1)

        self.prevBtn = QPushButton("&<", self)
        self.prevBtn.resize(50, 50)
        self.prevBtn.move(25, 500)

        self.nextBtn = QPushButton("&>", self)
        self.nextBtn.resize(50, 50)
        self.nextBtn.move(725, 500)

    def makeMenu(self, img, name, price, explain, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/pizzamenu/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        explain.setFont(QFont("여기어때 잘난체 OTF", 8))
        explain.setStyleSheet("Color : gray")
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
            explain.move(x, 480 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
            explain.move(x, 770 + name.height())
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class RecWidget_2(QWidget):
    def __init__(self, parent=None):
        super(RecWidget_2, self).__init__(parent)

        self.recPz = QLabel(self)
        self.recPz.resize(800, 950)
        pixmap = QPixmap("images/pizzamenu/recPizza.png")
        self.recPz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 100)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 100)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 100)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 100)

        self.orderBtn = QPushButton("<", self)
        self.orderBtn.resize(80, 80)
        self.orderBtn.move(10, 10)

        opacity = QGraphicsOpacityEffect(self.fameBtn)
        opacity.setOpacity(0)
        self.fameBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.premiumBtn)
        opacity.setOpacity(0)
        self.premiumBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.classicBtn)
        opacity.setOpacity(0)
        self.classicBtn.setGraphicsEffect(opacity)

        self.pz2 = QLabel(self)
        self.pzName2 = QLabel("스타 셰프 트러플 바질", self)
        self.pzPrice2 = QLabel("L 36900원~ M 29900원~", self)
        self.pzExplain2 = QLabel("#바질페스토와 스테이크 풍미", self)
        self.pz2Btn = QPushButton(self)

        self.makeMenu(self.pz2, self.pzName2, self.pzPrice2, self.pzExplain2, self.pz2Btn, 300, 250,
                      "starChefTruffleBazil",
                      1)

        self.prevBtn = QPushButton("&<", self)
        self.prevBtn.resize(50, 50)
        self.prevBtn.move(25, 500)

        self.nextBtn = QPushButton("&>", self)
        self.nextBtn.resize(50, 50)
        self.nextBtn.move(725, 500)

    def makeMenu(self, img, name, price, explain, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/pizzamenu/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        explain.setFont(QFont("여기어때 잘난체 OTF", 8))
        explain.setStyleSheet("Color : gray")
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
            explain.move(x, 480 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
            explain.move(x, 770 + name.height())
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class RecWidget_3(QWidget):
    def __init__(self, parent=None):
        super(RecWidget_3, self).__init__(parent)

        self.recPz = QLabel(self)
        self.recPz.resize(800, 950)
        pixmap = QPixmap("images/pizzamenu/recPizza.png")
        self.recPz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 100)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 100)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 100)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 100)

        self.orderBtn = QPushButton("<", self)
        self.orderBtn.resize(80, 80)
        self.orderBtn.move(10, 10)

        opacity = QGraphicsOpacityEffect(self.fameBtn)
        opacity.setOpacity(0)
        self.fameBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.premiumBtn)
        opacity.setOpacity(0)
        self.premiumBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.classicBtn)
        opacity.setOpacity(0)
        self.classicBtn.setGraphicsEffect(opacity)

        self.pz3 = QLabel(self)
        self.pzName3 = QLabel("글로벌 레전드4", self)
        self.pzPrice3 = QLabel("L 35900원~ M 29000원~", self)
        self.pzExplain3 = QLabel("#한국,미국,호주,프랑스 레전드 만남", self)
        self.pz3Btn = QPushButton(self)

        self.makeMenu(self.pz3, self.pzName3, self.pzPrice3, self.pzExplain3, self.pz3Btn, 520, 250,
                      "globalLegend4", 1)

        self.prevBtn = QPushButton("&<", self)
        self.prevBtn.resize(50, 50)
        self.prevBtn.move(25, 500)

        self.nextBtn = QPushButton("&>", self)
        self.nextBtn.resize(50, 50)
        self.nextBtn.move(725, 500)

    def makeMenu(self, img, name, price, explain, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/pizzamenu/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        explain.setFont(QFont("여기어때 잘난체 OTF", 8))
        explain.setStyleSheet("Color : gray")
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
            explain.move(x, 480 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
            explain.move(x, 770 + name.height())
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


# 프리미엄
class PreWidget_1(QWidget):
    def __init__(self, parent=None):
        super(PreWidget_1, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/pizzamenu/premiumPizza.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 100)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 100)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 100)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 100)

        self.orderBtn = QPushButton("<", self)
        self.orderBtn.resize(80, 80)
        self.orderBtn.move(10, 10)

        opacity = QGraphicsOpacityEffect(self.fameBtn)
        opacity.setOpacity(0)
        self.fameBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.premiumBtn)
        opacity.setOpacity(0)
        self.premiumBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.classicBtn)
        opacity.setOpacity(0)
        self.classicBtn.setGraphicsEffect(opacity)

        self.pz1 = QLabel(self)
        self.pzName1 = QLabel("스타 쉐프 시그니쳐", self)
        self.pzPrice1 = QLabel("L 36900원~ M 29900원~", self)
        self.pzExplain1 = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pz1Btn = QPushButton(self)

        self.makeMenu(self.pz1, self.pzName1, self.pzPrice1, self.pzExplain1, self.pz1Btn, 80, 250, "starChefSignature",
                      1)

        self.pz2 = QLabel(self)
        self.pzName2 = QLabel("스타 셰프 트러플 바질", self)
        self.pzPrice2 = QLabel("L 36900원~ M 29900원~", self)
        self.pzExplain2 = QLabel("#바질페스토와 스테이크 풍미", self)
        self.pz2Btn = QPushButton(self)

        self.makeMenu(self.pz2, self.pzName2, self.pzPrice2, self.pzExplain2, self.pz2Btn, 300, 250,
                      "starChefTruffleBazil",
                      1)

        self.pz3 = QLabel(self)
        self.pzName3 = QLabel("글로벌 레전드4", self)
        self.pzPrice3 = QLabel("L 35900원~ M 29000원~", self)
        self.pzExplain3 = QLabel("#한국,미국,호주,프랑스 레전드 만남", self)
        self.pz3Btn = QPushButton(self)

        self.makeMenu(self.pz3, self.pzName3, self.pzPrice3, self.pzExplain3, self.pz3Btn, 520, 250,
                      "globalLegend4", 1)

        self.pz4 = QLabel(self)
        self.pzName4 = QLabel("시리얼 칠리크랩", self)
        self.pzPrice4 = QLabel("L 34900~ M 29000원~", self)
        self.pzExplain4 = QLabel("#씨푸드부터 시리얼까지 새롭다", self)
        self.pz4Btn = QPushButton(self)

        self.makeMenu(self.pz4, self.pzName4, self.pzPrice4, self.pzExplain4, self.pz4Btn, 80, 540,
                      "serialChilliCrab", 2)

        self.pz5 = QLabel(self)
        self.pzName5 = QLabel("치즈케이크 블랙타이거", self)
        self.pzPrice5 = QLabel("L 35900원~ M 29000원~", self)
        self.pzExplain5 = QLabel("#새로운 레전드를 새우다", self)
        self.pz5Btn = QPushButton(self)

        self.makeMenu(self.pz5, self.pzName5, self.pzPrice5, self.pzExplain5, self.pz5Btn, 300, 540,
                      "cheeseCakeBlackTiger", 2)

        self.pz6 = QLabel(self)
        self.pzName6 = QLabel("30 치즈&뉴욕 스트립 스테이크", self)
        self.pzPrice6 = QLabel("L 34900원~ M 29000원~", self)
        self.pzExplain6 = QLabel("#30가지 치즈와 스테이크 조화", self)
        self.pz6Btn = QPushButton(self)

        self.makeMenu(self.pz6, self.pzName6, self.pzPrice6, self.pzExplain6, self.pz6Btn, 520, 540,
                      "30CheeseNewYorkStripStake", 2)

        self.nextBtn = QPushButton("&>", self)
        self.nextBtn.resize(50, 50)
        self.nextBtn.move(725, 500)

    def makeMenu(self, img, name, price, explain, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/pizzamenu/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        explain.setFont(QFont("여기어때 잘난체 OTF", 8))
        explain.setStyleSheet("Color : gray")
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
            explain.move(x, 480 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
            explain.move(x, 770 + name.height())
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class PreWidget_2(QWidget):
    def __init__(self, parent=None):
        super(PreWidget_2, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/pizzamenu/premiumPizza.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 100)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 100)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 100)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 100)

        self.orderBtn = QPushButton("<", self)
        self.orderBtn.resize(80, 80)
        self.orderBtn.move(10, 10)

        opacity = QGraphicsOpacityEffect(self.fameBtn)
        opacity.setOpacity(0)
        self.fameBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.premiumBtn)
        opacity.setOpacity(0)
        self.premiumBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.classicBtn)
        opacity.setOpacity(0)
        self.classicBtn.setGraphicsEffect(opacity)

        self.pz1 = QLabel(self)
        self.pzName1 = QLabel("블랙앵거스 스테이크", self)
        self.pzPrice1 = QLabel("L 34900~ M 29000원~", self)
        self.pzExplain1 = QLabel("#블랙앵거스 비프에 랍스터볼까지", self)
        self.pz1Btn = QPushButton(self)

        self.makeMenu(self.pz1, self.pzName1, self.pzPrice1, self.pzExplain1, self.pz1Btn, 80, 250, "blackAngersStake",
                      1)

        self.pz2 = QLabel(self)
        self.pzName2 = QLabel("베스트 콰트로", self)
        self.pzPrice2 = QLabel("L 34900원~ M 29000원~", self)
        self.pzExplain2 = QLabel("#4가지 피자를 한판에", self)
        self.pz2Btn = QPushButton(self)

        self.makeMenu(self.pz2, self.pzName2, self.pzPrice2, self.pzExplain2, self.pz2Btn, 300, 250, "bestQuattro",
                      1)

        self.pz3 = QLabel(self)
        self.pzName3 = QLabel("블랙타이거 슈림프", self)
        self.pzPrice3 = QLabel("L 34900원~ M 29000원~", self)
        self.pzExplain3 = QLabel("#바다와 육지의 대왕이 하나", self)
        self.pz3Btn = QPushButton(self)

        self.makeMenu(self.pz3, self.pzName3, self.pzPrice3, self.pzExplain3, self.pz3Btn, 520, 250,
                      "blackTigerShrimp", 1)

        self.pz4 = QLabel(self)
        self.pzName4 = QLabel("직화 스테이크", self)
        self.pzPrice4 = QLabel("L 33900원~ M 28000원~", self)
        self.pzExplain4 = QLabel("#직화스테이크,통새우 만남", self)
        self.pz4Btn = QPushButton(self)

        self.makeMenu(self.pz4, self.pzName4, self.pzPrice4, self.pzExplain4, self.pz4Btn, 80, 540,
                      "zikhwaStake", 2)

        self.prevBtn = QPushButton("&<", self)
        self.prevBtn.resize(50, 50)
        self.prevBtn.move(25, 500)

    def makeMenu(self, img, name, price, explain, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/pizzamenu/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        explain.setFont(QFont("여기어때 잘난체 OTF", 8))
        explain.setStyleSheet("Color : gray")
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
            explain.move(x, 480 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
            explain.move(x, 770 + name.height())
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class ClaWidget_1(QWidget):
    def __init__(self, parent=None):
        super(ClaWidget_1, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/pizzamenu/classicPizza.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 100)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 100)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 100)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 100)

        self.orderBtn = QPushButton("<", self)
        self.orderBtn.resize(80, 80)
        self.orderBtn.move(10, 10)

        opacity = QGraphicsOpacityEffect(self.fameBtn)
        opacity.setOpacity(0)
        self.fameBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.premiumBtn)
        opacity.setOpacity(0)
        self.premiumBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.classicBtn)
        opacity.setOpacity(0)
        self.classicBtn.setGraphicsEffect(opacity)

        self.pz1 = QLabel(self)
        self.pzName1 = QLabel("리얼 불고기", self)
        self.pzPrice1 = QLabel("L 27900원~ M 21000원~", self)
        self.pzExplain1 = QLabel("#프리미엄 불고기 토핑이 듬뿍", self)
        self.pz1Btn = QPushButton(self)

        self.makeMenu(self.pz1, self.pzName1, self.pzPrice1, self.pzExplain1, self.pz1Btn, 80, 250, "realBulgogi",
                      1)

        self.pz2 = QLabel(self)
        self.pzName2 = QLabel("치즈 가든", self)
        self.pzPrice2 = QLabel("L 27900원~ M 21000원~", self)
        self.pzExplain2 = QLabel("#리치한 치즈와 채소의 조화", self)
        self.pz2Btn = QPushButton(self)

        self.makeMenu(self.pz2, self.pzName2, self.pzPrice2, self.pzExplain2, self.pz2Btn, 300, 250, "cheeseGarden",
                      1)

        self.pz3 = QLabel(self)
        self.pzName3 = QLabel("우리 고구마", self)
        self.pzPrice3 = QLabel("L 29900원~ M 23000원~", self)
        self.pzExplain3 = QLabel("#고구마 큐브&무스가 듬뿍", self)
        self.pz3Btn = QPushButton(self)

        self.makeMenu(self.pz3, self.pzName3, self.pzPrice3, self.pzExplain3, self.pz3Btn, 520, 250,
                      "ourGoguma", 1)

        self.pz4 = QLabel(self)
        self.pzName4 = QLabel("포테이토", self)
        self.pzPrice4 = QLabel("L 25900원~ M 19000원~", self)
        self.pzExplain4 = QLabel("#도미노피자 No.1레전드", self)
        self.pz4Btn = QPushButton(self)

        self.makeMenu(self.pz4, self.pzName4, self.pzPrice4, self.pzExplain4, self.pz4Btn, 80, 540,
                      "potato", 2)

        self.pz5 = QLabel(self)
        self.pzName5 = QLabel("슈퍼디럭스", self)
        self.pzPrice5 = QLabel("L 25900원~ M 19000원~", self)
        self.pzExplain5 = QLabel("#누구나 사랑하는 베이직 피자", self)
        self.pz5Btn = QPushButton(self)

        self.makeMenu(self.pz5, self.pzName5, self.pzPrice5, self.pzExplain5, self.pz5Btn, 300, 540,
                      "superDelux", 2)

        self.pz6 = QLabel(self)
        self.pzName6 = QLabel("슈퍼슈프림", self)
        self.pzPrice6 = QLabel("L 25900원~ M 19000원~", self)
        self.pzExplain6 = QLabel("#콘과 파인애플의 달콤한 조화", self)
        self.pz6Btn = QPushButton(self)

        self.makeMenu(self.pz6, self.pzName6, self.pzPrice6, self.pzExplain6, self.pz6Btn, 520, 540,
                      "superSupreme", 2)

        self.nextBtn = QPushButton("&>", self)
        self.nextBtn.resize(50, 50)
        self.nextBtn.move(725, 500)

    def makeMenu(self, img, name, price, explain, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/pizzamenu/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        explain.setFont(QFont("여기어때 잘난체 OTF", 8))
        explain.setStyleSheet("Color : gray")
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
            explain.move(x, 480 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
            explain.move(x, 770 + name.height())
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class ClaWidget_2(QWidget):
    def __init__(self, parent=None):
        super(ClaWidget_2, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/pizzamenu/classicPizza.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 100)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 100)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 100)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 100)

        self.orderBtn = QPushButton("<", self)
        self.orderBtn.resize(80, 80)
        self.orderBtn.move(10, 10)

        opacity = QGraphicsOpacityEffect(self.fameBtn)
        opacity.setOpacity(0)
        self.fameBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.premiumBtn)
        opacity.setOpacity(0)
        self.premiumBtn.setGraphicsEffect(opacity)

        opacity = QGraphicsOpacityEffect(self.classicBtn)
        opacity.setOpacity(0)
        self.classicBtn.setGraphicsEffect(opacity)

        self.pz1 = QLabel(self)
        self.pzName1 = QLabel("베이컨체더치즈", self)
        self.pzPrice1 = QLabel("L 25900원~ M 19000원~", self)
        self.pzExplain1 = QLabel("#베이컨 매니아들의 원픽", self)
        self.pz1Btn = QPushButton(self)

        self.makeMenu(self.pz1, self.pzName1, self.pzPrice1, self.pzExplain1, self.pz1Btn, 80, 250,
                      "bacconCheddarCheese",
                      1)

        self.pz2 = QLabel(self)
        self.pzName2 = QLabel("페퍼로니", self)
        self.pzPrice2 = QLabel("L 22900원~ M 16000원~", self)
        self.pzExplain2 = QLabel("#짭짤한 풍미가 일품", self)
        self.pz2Btn = QPushButton(self)

        self.makeMenu(self.pz2, self.pzName2, self.pzPrice2, self.pzExplain2, self.pz2Btn, 300, 250, "pepperoni",
                      1)

        self.pz3 = QLabel(self)
        self.pzName3 = QLabel("치즈", self)
        self.pzPrice3 = QLabel("L 21900~ M 15000원~", self)
        self.pzExplain3 = QLabel("#토마토 소스와 풍부한 모차렐라", self)
        self.pz3Btn = QPushButton(self)

        self.makeMenu(self.pz3, self.pzName3, self.pzPrice3, self.pzExplain3, self.pz3Btn, 520, 250,
                      "cheese", 1)

        self.prevBtn = QPushButton("&<", self)
        self.prevBtn.resize(50, 50)
        self.prevBtn.move(25, 500)

    def makeMenu(self, img, name, price, explain, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/pizzamenu/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        explain.setFont(QFont("여기어때 잘난체 OTF", 8))
        explain.setStyleSheet("Color : gray")
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
            explain.move(x, 480 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
            explain.move(x, 770 + name.height())
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class AboutWidget(QWidget):

    def __init__(self, parent=None):
        super(AboutWidget, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/toppingBack.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.date = QDate.currentDate()
        self.time = QTime.currentTime()

        self.sizePrice = 0
        self.doughPrice = 0
        self.pizzaAmount = 1
        self.pizzaPrice = self.sizePrice + self.doughPrice
        self.resultPrice = 0

    def setting(self, img_name, name, size_l, size_m):

        self.txtPrice = QLabel(str(self.resultPrice), self)
        self.txtPrice.move(50, 850)
        self.txtPrice.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.pzPic = QLabel(self)
        self.pzPic.setPixmap(QPixmap("images/pizzamenu/" + img_name + ".jpg"))
        self.pzPic.setScaledContents(True)
        self.pzPic.setGeometry(QRect(50, 300, 300, 300))

        self.pzName = QLabel(name, self)
        self.pzName.move(50, 250)
        self.pzName.setFont(QFont("여기어때 잘난체 OTF", 20))

        self.sizeTxt = QLabel("사이즈 선택", self)
        self.sizeTxt.move(400, 280)
        self.sizeTxt.setFont(QFont("여기어때 잘난체 OTF", 15))

        self.sizeL = size_l
        self.sizeM = size_m

        self.sizeLarge = 'L ' + str(self.sizeL) + "원"
        self.sizeMid = 'M ' + str(self.sizeM) + "원"

        dSize = QComboBox(self)
        dSize.addItem('사이즈 선택')
        dSize.addItem(self.sizeLarge)
        dSize.addItem(self.sizeMid)

        dSize.move(400, 320)

        dSize.activated[str].connect(self.doughSizeFunc)

        self.doughTxt = QLabel('도우 선택', self)
        self.doughTxt.move(400, 370)
        self.doughTxt.setFont(QFont("여기어때 잘난체 OTF", 15))

        cb = QComboBox(self)
        cb.addItem('오리지널 도우(기본)')
        cb.addItem('나폴리 도우')
        cb.addItem('씬 도우(기본 갈릭디핑 소스 미제공')
        cb.addItem('슈퍼시드 함유 도우')
        cb.addItem('오리지널 도우(칠리핫도그 엣지)')
        cb.addItem('오리지널 도우(더블 치즈엣지)')
        cb.move(400, 410)

        cb.activated[str].connect(self.doughSelect)

        self.pzAmountName = QLabel('피자 수량', self)
        self.pzAmountName.move(400, 460)
        self.pzAmountName.setFont(QFont("여기어때 잘난체 OTF", 15))

        self.spinbox = QSpinBox(self)
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(10)
        self.spinbox.setSingleStep(1)
        self.spinbox.move(450, 500)

        self.pzAmountLabel = QLabel('1', self)
        self.pzAmountLabel.move(400, 500)
        self.pzAmountLabel.setFont(QFont("여기어때 잘난체 OTF", 15))

        self.spinbox.valueChanged.connect(self.value_changed)

        self.pzExplain = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pzExplain.move(520, 890)
        self.pzExplain.setFont(QFont("여기어때 잘난체 OTF", 8))
        self.pzExplain.setStyleSheet("Color : gray")

        self.cartAddBtn = QPushButton("카트 담기", self)
        self.cartAddBtn.resize(200, 100)
        self.cartAddBtn.move(400, 600)

        self.backBtn = QPushButton("뒤로가기", self)
        self.backBtn.resize(200, 100)
        self.backBtn.move(200, 600)

        self.cartAddBtn.clicked.connect(self.clickCart)

    def clickCart(self):
        if self.sizeTxt.text() == "사이즈 선택":
            QMessageBox.critical(self, "QMessageBox", "사이즈를 선택해주세요")
        else:
            option = QMessageBox.question(self, "카트", "카트에 담으시겠습니까?",
                                          QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
            if option == QMessageBox.Yes:  # 버튼의 이름을 넣으면 됩니다.
                QMessageBox.information(self, "카트", "카트에 담겼습니다!")
                with open("nowPizzaCart.txt", mode="a") as file:
                    file.write(self.pzName.text() + "\t" + str(self.pizzaAmount) + "\t" + str(self.resultPrice) + "\n")
                    print(self.pzName.text(), self.pizzaAmount, self.pizzaPrice)

    def value_changed(self):
        self.pzAmountLabel.setText(str(self.spinbox.value()))
        self.pizzaAmount = self.spinbox.value()

        self.resultPrice = self.pizzaPrice * (self.spinbox.value())

        self.txtPrice.setText(str(self.resultPrice))
        self.txtPrice.adjustSize()

        print(self.resultPrice)

    def doughSelect(self, text):
        self.doughTxt.setText(text)
        self.doughTxt.adjustSize()

        self.doughPrice = 0
        if text == '슈퍼시드 함유 도우':
            self.doughPrice += 2000
        elif text == '오리지널 도우(칠리핫도그 엣지)':
            self.doughPrice += 5000
        elif text == '오리지널 도우(더블 치즈엣지)':
            self.doughPrice += 5000

        self.pizzaPrice = (self.doughPrice + self.sizePrice)
        self.resultPrice = self.pizzaPrice * self.pizzaAmount
        self.txtPrice.setText(str(self.resultPrice))
        self.txtPrice.adjustSize()
        print(self.resultPrice)

    def doughSizeFunc(self, text):
        self.sizeTxt.setText(text)
        self.sizeTxt.adjustSize()

        self.sizePrice = 0
        if text == self.sizeLarge:
            self.sizePrice += self.sizeL
        elif text == self.sizeMid:
            self.sizePrice += self.sizeM

        self.pizzaPrice = (self.doughPrice + self.sizePrice)
        self.resultPrice = self.pizzaPrice * self.pizzaAmount
        self.txtPrice.setText(str(self.resultPrice))
        self.txtPrice.adjustSize()


# 서브 메뉴 및 콜라
class SubWidget(QWidget):
    def __init__(self, parent=None):
        super(SubWidget, self).__init__(parent)

        self.subBack = QLabel(self)
        self.subBack.resize(800, 950)
        pixmap = QPixmap("images/subMenu1.png")
        self.subBack.setPixmap(QPixmap(pixmap))

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(0, 100)

        self.sidedishBtn = QPushButton(self)
        self.sidedishBtn.resize(200, 100)
        self.sidedishBtn.move(200, 100)

        self.drinkBtn = QPushButton(self)
        self.drinkBtn.resize(200, 100)
        self.drinkBtn.move(400, 100)

        self.etcBtn = QPushButton(self)
        self.etcBtn.resize(200, 100)
        self.etcBtn.move(600, 100)

        self.orderBtn = QPushButton("<", self)
        self.orderBtn.resize(80, 80)
        self.orderBtn.move(10, 10)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.sidedishBtn)
        opacity.setOpacity(0)
        self.sidedishBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.drinkBtn)
        opacity.setOpacity(0)
        self.drinkBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.etcBtn)
        opacity.setOpacity(0)
        self.etcBtn.setGraphicsEffect(opacity)

        self.rec1 = QLabel(self)
        self.recName1 = QLabel("셰프’s 토마토 파스타", self)
        self.recPrice1 = QLabel("9800원", self)
        self.rec1Btn = QPushButton(self)
        self.makeMenu(self.rec1, self.recName1, self.recPrice1, self.rec1Btn, 80, 250, "tomato_pasta")

        self.rec2 = QLabel(self)
        self.recName2 = QLabel("셰프’s 트러플 바질 파스타", self)
        self.recPrice2 = QLabel("9800원", self)
        self.rec2Btn = QPushButton(self)
        self.makeMenu(self.rec2, self.recName2, self.recPrice2, self.rec2Btn, 300, 250, "basil_pasta")

        self.rec3 = QLabel(self)
        self.recName3 = QLabel("스파이시 씨푸드 로제 파스타", self)
        self.recPrice3 = QLabel("8800원", self)
        self.rec3Btn = QPushButton(self)
        self.makeMenu(self.rec3, self.recName3, self.recPrice3, self.rec3Btn, 520, 250, "rose_pasta")

    def makeMenu(self, img, name, price, btn, x, y, path):
        img.setPixmap(QPixmap("images/sidedish/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.move(x, 460)
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        price.move(x, 480)
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class Sub_SideWidget1(QWidget):
    def __init__(self, parent=None):
        super(Sub_SideWidget1, self).__init__(parent)

        self.recPz = QLabel(self)
        self.recPz.resize(800, 950)
        pixmap = QPixmap("images/subMenu2.png")
        self.recPz.setPixmap(QPixmap(pixmap))

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(0, 100)

        self.sidedishBtn = QPushButton(self)
        self.sidedishBtn.resize(200, 100)
        self.sidedishBtn.move(200, 100)

        self.drinkBtn = QPushButton(self)
        self.drinkBtn.resize(200, 100)
        self.drinkBtn.move(400, 100)

        self.etcBtn = QPushButton(self)
        self.etcBtn.resize(200, 100)
        self.etcBtn.move(600, 100)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.sidedishBtn)
        opacity.setOpacity(0)
        self.sidedishBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.drinkBtn)
        opacity.setOpacity(0)
        self.drinkBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.etcBtn)
        opacity.setOpacity(0)
        self.etcBtn.setGraphicsEffect(opacity)

        self.rec1 = QLabel(self)
        self.recName1 = QLabel("셰프’s 토마토 파스타", self)
        self.recPrice1 = QLabel("9800원", self)
        self.rec1Btn = QPushButton(self)
        self.makeMenu(self.rec1, self.recName1, self.recPrice1, self.rec1Btn, 80, 250, "tomato_pasta", 1)

        self.rec2 = QLabel(self)
        self.recName2 = QLabel("셰프’s 트러플 바질 파스타", self)
        self.recPrice2 = QLabel("9800원", self)
        self.rec2Btn = QPushButton(self)
        self.makeMenu(self.rec2, self.recName2, self.recPrice2, self.rec2Btn, 300, 250, "basil_pasta", 1)

        self.rec3 = QLabel(self)
        self.recName3 = QLabel("스파이시 씨푸드 로제 파스타", self)
        self.recPrice3 = QLabel("8800원", self)
        self.rec3Btn = QPushButton(self)
        self.makeMenu(self.rec3, self.recName3, self.recPrice3, self.rec3Btn, 520, 250, "rose_pasta", 1)

        self.rec4 = QLabel(self)
        self.recName4 = QLabel("크리스피 핫 순살 치킨\n(8조각)", self)
        self.recPrice4 = QLabel("4800원", self)
        self.rec4Btn = QPushButton(self)
        self.makeMenu(self.rec4, self.recName4, self.recPrice4, self.rec4Btn, 80, 540, "crispy_chicken", 2)

        self.rec5 = QLabel(self)
        self.recName5 = QLabel("샐러드 가든", self)
        self.recPrice5 = QLabel("6800원", self)
        self.rec5Btn = QPushButton(self)
        self.makeMenu(self.rec5, self.recName5, self.recPrice5, self.rec5Btn, 300, 540, "salad", 2)

        self.rec6 = QLabel(self)
        self.recName6 = QLabel("펜네 파스타", self)
        self.recPrice6 = QLabel("8800원", self)
        self.rec6Btn = QPushButton(self)
        self.makeMenu(self.rec6, self.recName6, self.recPrice6, self.rec6Btn, 520, 540, "penne_pasta", 2)

        self.nextBtn = QPushButton("&>", self)
        self.nextBtn.resize(50, 50)
        self.nextBtn.move(725, 500)

    def makeMenu(self, img, name, price, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/sidedish/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class Sub_SideWidget2(QWidget):
    def __init__(self, parent=None):
        super(Sub_SideWidget2, self).__init__(parent)

        self.recPz = QLabel(self)
        self.recPz.resize(800, 950)
        pixmap = QPixmap("images/subMenu2.png")
        self.recPz.setPixmap(QPixmap(pixmap))

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(0, 100)

        self.sidedishBtn = QPushButton(self)
        self.sidedishBtn.resize(200, 100)
        self.sidedishBtn.move(200, 100)

        self.drinkBtn = QPushButton(self)
        self.drinkBtn.resize(200, 100)
        self.drinkBtn.move(400, 100)

        self.etcBtn = QPushButton(self)
        self.etcBtn.resize(200, 100)
        self.etcBtn.move(600, 100)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.sidedishBtn)
        opacity.setOpacity(0)
        self.sidedishBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.drinkBtn)
        opacity.setOpacity(0)
        self.drinkBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.etcBtn)
        opacity.setOpacity(0)
        self.etcBtn.setGraphicsEffect(opacity)

        self.rec1 = QLabel(self)
        self.recName1 = QLabel("슈퍼곡물 치킨(10조각)", self)
        self.recPrice1 = QLabel("7800원", self)
        self.rec1Btn = QPushButton(self)
        self.makeMenu(self.rec1, self.recName1, self.recPrice1, self.rec1Btn, 80, 250, "grain_chicken", 1)

        self.rec2 = QLabel(self)
        self.recName2 = QLabel("NEW 치즈 볼로네즈 스파게티", self)
        self.recPrice2 = QLabel("8800원", self)
        self.rec2Btn = QPushButton(self)
        self.makeMenu(self.rec2, self.recName2, self.recPrice2, self.rec2Btn, 300, 250, "bolognese_spaghetti", 1)

        self.rec3 = QLabel(self)
        self.recName3 = QLabel("트러플 리조또", self)
        self.recPrice3 = QLabel("8800원", self)
        self.rec3Btn = QPushButton(self)
        self.makeMenu(self.rec3, self.recName3, self.recPrice3, self.rec3Btn, 520, 250, "truffle_risotto", 1)

        self.rec4 = QLabel(self)
        self.recName4 = QLabel("하프&하프 스파게티\n(NEW 치즈 & 화이트 크림)", self)
        self.recPrice4 = QLabel("9800원", self)
        self.rec4Btn = QPushButton(self)
        self.makeMenu(self.rec4, self.recName4, self.recPrice4, self.rec4Btn, 80, 540, "half_spaghetti", 2)

        self.rec5 = QLabel(self)
        self.recName5 = QLabel("화이트 크림 스파게티", self)
        self.recPrice5 = QLabel("8800원", self)
        self.rec5Btn = QPushButton(self)
        self.makeMenu(self.rec5, self.recName5, self.recPrice5, self.rec5Btn, 300, 540, "cream_spaghetti", 2)

        self.rec6 = QLabel(self)
        self.recName6 = QLabel("갈릭&허브윙스(8조각)", self)
        self.recPrice6 = QLabel("8800원", self)
        self.rec6Btn = QPushButton(self)
        self.makeMenu(self.rec6, self.recName6, self.recPrice6, self.rec6Btn, 520, 540, "wings", 2)

        self.prevBtn = QPushButton("&<", self)
        self.prevBtn.resize(50, 50)
        self.prevBtn.move(25, 500)

    def makeMenu(self, img, name, price, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/sidedish/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class Sub_DrinkWidget(QWidget):
    def __init__(self, parent=None):
        super(Sub_DrinkWidget, self).__init__(parent)

        self.recPz = QLabel(self)
        self.recPz.resize(800, 950)
        pixmap = QPixmap("images/subMenu3.png")
        self.recPz.setPixmap(QPixmap(pixmap))

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(0, 100)

        self.sidedishBtn = QPushButton(self)
        self.sidedishBtn.resize(200, 100)
        self.sidedishBtn.move(200, 100)

        self.drinkBtn = QPushButton(self)
        self.drinkBtn.resize(200, 100)
        self.drinkBtn.move(400, 100)

        self.etcBtn = QPushButton(self)
        self.etcBtn.resize(200, 100)
        self.etcBtn.move(600, 100)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.sidedishBtn)
        opacity.setOpacity(0)
        self.sidedishBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.drinkBtn)
        opacity.setOpacity(0)
        self.drinkBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.etcBtn)
        opacity.setOpacity(0)
        self.etcBtn.setGraphicsEffect(opacity)

        self.rec1 = QLabel(self)
        self.recName1 = QLabel("코카콜라 1.25L", self)
        self.recPrice1 = QLabel("2000원", self)
        self.rec1Btn = QPushButton(self)
        self.makeMenu(self.rec1, self.recName1, self.recPrice1, self.rec1Btn, 80, 250, "cola1.25", 1)

        self.rec2 = QLabel(self)
        self.recName2 = QLabel("코카콜라 500ml", self)
        self.recPrice2 = QLabel("1400원", self)
        self.rec2Btn = QPushButton(self)
        self.makeMenu(self.rec2, self.recName2, self.recPrice2, self.rec2Btn, 300, 250, "cola500", 1)

        self.rec3 = QLabel(self)
        self.recName3 = QLabel("코카콜라 제로 1.5L", self)
        self.recPrice3 = QLabel("2100원", self)
        self.rec3Btn = QPushButton(self)
        self.makeMenu(self.rec3, self.recName3, self.recPrice3, self.rec3Btn, 520, 250, "zerocola1.5", 1)

        self.rec4 = QLabel(self)
        self.recName4 = QLabel("코카콜라 제로 500ml", self)
        self.recPrice4 = QLabel("1300원", self)
        self.rec4Btn = QPushButton(self)
        self.makeMenu(self.rec4, self.recName4, self.recPrice4, self.rec4Btn, 80, 540, "zerocola500", 2)

        self.rec5 = QLabel(self)
        self.recName5 = QLabel("스프라이트 1.5L", self)
        self.recPrice5 = QLabel("2100원", self)
        self.rec5Btn = QPushButton(self)
        self.makeMenu(self.rec5, self.recName5, self.recPrice5, self.rec5Btn, 300, 540, "sprite1.5", 2)

        self.rec6 = QLabel(self)
        self.recName6 = QLabel("스프라이트 500ml", self)
        self.recPrice6 = QLabel("1300원", self)
        self.rec6Btn = QPushButton(self)
        self.makeMenu(self.rec6, self.recName6, self.recPrice6, self.rec6Btn, 520, 540, "sprite500", 2)

    def makeMenu(self, img, name, price, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/drink_etc/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class Sub_EtcWidget(QWidget):
    def __init__(self, parent=None):
        super(Sub_EtcWidget, self).__init__(parent)

        self.recPz = QLabel(self)
        self.recPz.resize(800, 950)
        pixmap = QPixmap("images/subMenu4.png")
        self.recPz.setPixmap(QPixmap(pixmap))

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(0, 100)

        self.sidedishBtn = QPushButton(self)
        self.sidedishBtn.resize(200, 100)
        self.sidedishBtn.move(200, 100)

        self.drinkBtn = QPushButton(self)
        self.drinkBtn.resize(200, 100)
        self.drinkBtn.move(400, 100)

        self.etcBtn = QPushButton(self)
        self.etcBtn.resize(200, 100)
        self.etcBtn.move(600, 100)

        opacity = QGraphicsOpacityEffect(self.recommendBtn)
        opacity.setOpacity(0)
        self.recommendBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.sidedishBtn)
        opacity.setOpacity(0)
        self.sidedishBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.drinkBtn)
        opacity.setOpacity(0)
        self.drinkBtn.setGraphicsEffect(opacity)
        opacity = QGraphicsOpacityEffect(self.etcBtn)
        opacity.setOpacity(0)
        self.etcBtn.setGraphicsEffect(opacity)

        self.rec1 = QLabel(self)
        self.recName1 = QLabel("우리 피클 L", self)
        self.recPrice1 = QLabel("800원", self)
        self.rec1Btn = QPushButton(self)
        self.makeMenu(self.rec1, self.recName1, self.recPrice1, self.rec1Btn, 80, 250, "picklel", 1)

        self.rec2 = QLabel(self)
        self.recName2 = QLabel("우리 피클 M", self)
        self.recPrice2 = QLabel("500원", self)
        self.rec2Btn = QPushButton(self)
        self.makeMenu(self.rec2, self.recName2, self.recPrice2, self.rec2Btn, 300, 250, "picklem", 1)

        self.rec3 = QLabel(self)
        self.recName3 = QLabel("도미노 시리얼", self)
        self.recPrice3 = QLabel("400원", self)
        self.rec3Btn = QPushButton(self)
        self.makeMenu(self.rec3, self.recName3, self.recPrice3, self.rec3Btn, 520, 250, "cereal", 1)

        self.rec4 = QLabel(self)
        self.recName4 = QLabel("스위트 칠리소스 15g", self)
        self.recPrice4 = QLabel("300원", self)
        self.rec4Btn = QPushButton(self)
        self.makeMenu(self.rec4, self.recName4, self.recPrice4, self.rec4Btn, 80, 540, "chilisauce", 2)

        self.rec5 = QLabel(self)
        self.recName5 = QLabel("갈릭 디핑 소스 15g", self)
        self.recPrice5 = QLabel("200원", self)
        self.rec5Btn = QPushButton(self)
        self.makeMenu(self.rec5, self.recName5, self.recPrice5, self.rec5Btn, 300, 540, "garlicsauce", 2)

        self.rec6 = QLabel(self)
        self.recName6 = QLabel("핫소스", self)
        self.recPrice6 = QLabel("100원", self)
        self.rec6Btn = QPushButton(self)
        self.makeMenu(self.rec6, self.recName6, self.recPrice6, self.rec6Btn, 520, 540, "hotsauce", 2)

    def makeMenu(self, img, name, price, btn, x, y, path, floor):
        img.setPixmap(QPixmap("images/drink_etc/" + path + ".jpg"))
        img.setScaledContents(True)
        img.setGeometry(QRect(x, y, 200, 200))
        name.setFont(QFont("여기어때 잘난체 OTF", 10))
        name.resize(name.sizeHint())
        if floor == 1:
            name.move(x, 460)
            price.move(x, 460 + name.height())
        else:
            name.move(x, 750)
            price.move(x, 750 + name.height())
        price.setFont(QFont("여기어때 잘난체 OTF", 9))
        btn.resize(200, 260)
        btn.move(x, y)
        opacity = QGraphicsOpacityEffect(btn)
        opacity.setOpacity(0)
        btn.setGraphicsEffect(opacity)


class SubAboutWidget(QWidget):
    def __init__(self, parent=None):
        super(SubAboutWidget, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/toppingBack.png")
        self.famePz.setPixmap(QPixmap(pixmap))

    def test(self, img_name, name, price, menu):
        self.price = price

        self.pz1 = QLabel(self)
        if menu == "sidedish":
            self.pz1.setPixmap(QPixmap("images/sidedish/" + img_name + ".jpg"))
        else:
            self.pz1.setPixmap(QPixmap("images/drink_etc/" + img_name + ".jpg"))
        self.pz1.setScaledContents(True)
        self.pz1.setGeometry(QRect(50, 300, 300, 300))

        self.pzName = QLabel(self)
        self.pzName.setText(name)
        self.pzName.move(50, 250)
        self.pzName.setFont(QFont("여기어때 잘난체", 20))

        self.num_lbl = QLabel('수량 선택', self)
        self.num_lbl.move(380, 310)
        self.num_lbl.setFont(QFont("여기어때 잘난체", 15))

        self.num_spin = QSpinBox(self)
        self.num_spin.move(650, 310)
        self.num_spin.setRange(0, 99)
        self.num_spin.setValue(1)
        self.num_spin.setSuffix(" 개")
        self.num_spin.valueChanged.connect(self.setPrice)

        self.pzPrice = QLabel(str(price) + "원", self)
        self.pzPrice.move(380, 650)
        self.pzPrice.setFont(QFont("여기어때 잘난체", 25))

        self.putBtn = QPushButton("카트담기", self)
        self.putBtn.resize(100, 50)
        self.putBtn.move(650, 650)

        self.backBtn = QPushButton("뒤로가기", self)
        self.backBtn.resize(200, 100)
        self.backBtn.move(200, 600)

    def setPrice(self):
        self.pzPrice.setText(str(self.num_spin.value() * self.price) + "원")
        self.pzPrice.resize(self.pzPrice.sizeHint())

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def clickCart(self):
        option = QMessageBox.question(self, "카트", "카트에 담으시겠습니까?",
                                      QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if option == QMessageBox.Yes:  # 버튼의 이름을 넣으면 됩니다.
            QMessageBox.information(self, "카트", "카트에 담겼습니다!")
            with open("nowSubCart.txt", mode="a") as file:
                file.write(self.pzName.text() + "\t" + str(self.num_spin.value()) + "\t" + self.pzPrice.text() + "\n")
                print(self.pzName.text(), str(self.num_spin.value()), self.pzPrice.text())


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
elif sys.exit():
    open('nowPizzaCart.txt', 'w').close()
    open('nowSubCart.txt', 'w').close()
