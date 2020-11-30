#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 스택 위젯의 기본 사용법
# * 여러 위젯을 한 위젯 공간에 선택될 수 있도록 한다.

import sys

from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        start_widget = StartWidget(self)
        start_widget.adv.clicked.connect(self.clickAdv)
        self.central_widget.addWidget(start_widget)

        self.setWindowTitle('PizzaKiosk')
        self.setWindowIcon(QIcon('images/dominoLogo.png'))
        self.setFixedSize(800, 950)
        self.center()

    def clickAdv(self):
        order_widget = OrderWidget(self)
        order_widget.pizzaBtn.clicked.connect(self.clickFame)
        order_widget.subBtn.clicked.connect(self.clickSub)
        self.central_widget.addWidget(order_widget)
        self.central_widget.setCurrentWidget(order_widget)

    def clickFame(self):
        fame_widget = FameWidget(self)
        fame_widget.recommendBtn.clicked.connect(self.clickRec)
        fame_widget.premiumBtn.clicked.connect(self.clickPre)
        fame_widget.classicBtn.clicked.connect(self.clickCla)

        self.central_widget.addWidget(fame_widget)
        self.central_widget.setCurrentWidget(fame_widget)

    def clickSub(self):
        sub_widget = SubWidget(self)
        sub_widget.sidedishBtn.clicked.connect(self.clickSub_side)
        sub_widget.drinkBtn.clicked.connect(self.clickSub_drink)
        sub_widget.etcBtn.clicked.connect(self.clickSub_etc)

        sub_widget.rec1Btn.clicked.connect(
            lambda img_name="tomato_pasta", name="셰프’s 토마토 파스타", price=9800, menu="sidedish": self.click_menu(img_name,
                                                                                                              name,
                                                                                                              price,
                                                                                                              menu))
        sub_widget.rec2Btn.clicked.connect(
            lambda img_name="basil_pasta", name="셰프’s 트러플 바질 파스타", price=9800, menu="sidedish": self.click_menu(
                img_name, name, price, menu))
        sub_widget.rec3Btn.clicked.connect(
            lambda img_name="rose_pasta", name="스파이시 씨푸드 로제 파스타", price=8800, menu="sidedish": self.click_menu(img_name,
                                                                                                               name,
                                                                                                               price,
                                                                                                               menu))

        self.central_widget.addWidget(sub_widget)
        self.central_widget.setCurrentWidget(sub_widget)

    def clickRec(self):
        rec_widget = RecWidget(self)
        rec_widget.fameBtn.clicked.connect(self.clickFame)
        rec_widget.premiumBtn.clicked.connect(self.clickPre)
        rec_widget.classicBtn.clicked.connect(self.clickCla)
        rec_widget.pz1Btn.clicked.connect(self.clickPz1)

        self.central_widget.addWidget(rec_widget)
        self.central_widget.setCurrentWidget(rec_widget)

    def clickPre(self):
        pre_widget = PreWidget(self)
        pre_widget.fameBtn.clicked.connect(self.clickFame)
        pre_widget.recommendBtn.clicked.connect(self.clickRec)
        pre_widget.classicBtn.clicked.connect(self.clickCla)

        self.central_widget.addWidget(pre_widget)
        self.central_widget.setCurrentWidget(pre_widget)

    def clickCla(self):
        cla_widget = ClaWidget(self)
        cla_widget.fameBtn.clicked.connect(self.clickFame)
        cla_widget.recommendBtn.clicked.connect(self.clickRec)
        cla_widget.premiumBtn.clicked.connect(self.clickPre)

        self.central_widget.addWidget(cla_widget)
        self.central_widget.setCurrentWidget(cla_widget)

    def clickPz1(self):
        about_widget = AboutWidget(self)
        self.central_widget.addWidget(about_widget)
        self.central_widget.setCurrentWidget(about_widget)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clickSub_side(self):
        rec_widget = Sub_SideWidget1(self)
        rec_widget.recommendBtn.clicked.connect(self.clickSub)
        rec_widget.sidedishBtn.clicked.connect(self.clickSub_side)
        rec_widget.drinkBtn.clicked.connect(self.clickSub_drink)
        rec_widget.etcBtn.clicked.connect(self.clickSub_etc)

        rec_widget.rec1Btn.clicked.connect(
            lambda img_name="tomato_pasta", name="셰프’s 토마토 파스타", price=9800, menu="sidedish": self.click_menu(img_name,
                                                                                                              name,
                                                                                                              price,
                                                                                                              menu))
        rec_widget.rec2Btn.clicked.connect(
            lambda img_name="basil_pasta", name="셰프’s 트러플 바질 파스타", price=9800, menu="sidedish": self.click_menu(
                img_name, name, price, menu))
        rec_widget.rec3Btn.clicked.connect(
            lambda img_name="rose_pasta", name="스파이시 씨푸드 로제 파스타", price=8800, menu="sidedish": self.click_menu(img_name,
                                                                                                               name,
                                                                                                               price,
                                                                                                               menu))
        rec_widget.rec4Btn.clicked.connect(
            lambda img_name="crispy_chicken", name="크리스피 핫 순살 치킨(8조각)", price=4800, menu="sidedish": self.click_menu(
                img_name, name,
                price, menu))
        rec_widget.rec5Btn.clicked.connect(
            lambda img_name="salad", name="샐러드 가든", price=6800, menu="sidedish": self.click_menu(img_name, name, price,
                                                                                                 menu))
        rec_widget.rec6Btn.clicked.connect(
            lambda img_name="penne_pasta", name="펜네 파스타", price=8800, menu="sidedish": self.click_menu(img_name, name,
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
            lambda img_name="grain_chicken", name="슈퍼곡물 치킨(10조각)", price=7800, menu="sidedish": self.click_menu(
                img_name, name, price, menu))
        rec_widget.rec2Btn.clicked.connect(
            lambda img_name="bolognese_spaghetti", name="NEW 치즈 볼로네즈 스파게티", price=8800,
                   menu="sidedish": self.click_menu(img_name, name,
                                                    price, menu))
        rec_widget.rec3Btn.clicked.connect(
            lambda img_name="truffle_risotto", name="트러플 리조또", price=8800, menu="sidedish": self.click_menu(img_name,
                                                                                                            name, price,
                                                                                                            menu))
        rec_widget.rec4Btn.clicked.connect(
            lambda img_name="half_spaghetti", name="하프&하프 스파게티 (NEW 치즈 & 화이트 크림)", price=9800,
                   menu="sidedish": self.click_menu(img_name,
                                                    name,
                                                    price, menu))
        rec_widget.rec5Btn.clicked.connect(
            lambda img_name="cream_spaghetti", name="화이트 크림 스파게티", price=8800, menu="sidedish": self.click_menu(
                img_name, name, price, menu))
        rec_widget.rec6Btn.clicked.connect(
            lambda img_name="wings", name="갈릭&허브윙스(8조각)", price=8800, menu="sidedish": self.click_menu(img_name, name,
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

    def click_menu(self, img_name, name, price, menu):
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


class FameWidget(QWidget):
    def __init__(self, parent=None):
        super(FameWidget, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/famePizza.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 200)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 200)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 200)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 200)

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


class RecWidget(QWidget):
    def __init__(self, parent=None):
        super(RecWidget, self).__init__(parent)

        self.recPz = QLabel(self)
        self.recPz.resize(800, 950)
        pixmap = QPixmap("images/recPizza.png")
        self.recPz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 200)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 200)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 200)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 200)

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
        self.pz1.setPixmap(QPixmap("images/starChefSignature.jpg"))
        self.pz1.setGeometry(QRect(80, 350, 200, 200))

        self.pzName1 = QLabel("스타 쉐프 시그니쳐", self)
        self.pzName1.move(80, 560)
        self.pzName1.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.pzPrice1 = QLabel("L 36900원~ M 29900원~", self)
        self.pzPrice1.move(80, 580)
        self.pzPrice1.setFont(QFont("여기어때 잘난체 OTF", 9))

        self.pzExplain1 = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pzExplain1.move(80, 600)
        self.pzExplain1.setFont(QFont("여기어때 잘난체 OTF", 8))
        self.pzExplain1.setStyleSheet("Color : gray")

        self.pz1Btn = QPushButton(self)
        self.pz1Btn.resize(200, 260)
        self.pz1Btn.move(80, 350)

        opacity = QGraphicsOpacityEffect(self.pz1Btn)
        opacity.setOpacity(0)
        self.pz1Btn.setGraphicsEffect(opacity)

        self.pz2 = QLabel(self)
        self.pz2.setPixmap(QPixmap("images/starChefSignature.jpg"))
        self.pz2.setGeometry(QRect(300, 350, 200, 200))

        self.pzName2 = QLabel("스타 쉐프 시그니쳐", self)
        self.pzName2.move(300, 560)
        self.pzName2.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.pzPrice2 = QLabel("L 36900원~ M 29900원~", self)
        self.pzPrice2.move(300, 580)
        self.pzPrice2.setFont(QFont("여기어때 잘난체 OTF", 9))

        self.pzExplain2 = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pzExplain2.move(300, 600)
        self.pzExplain2.setFont(QFont("여기어때 잘난체 OTF", 8))
        self.pzExplain2.setStyleSheet("Color : gray")

        self.pz2Btn = QPushButton(self)
        self.pz2Btn.resize(200, 260)
        self.pz2Btn.move(300, 350)

        self.pz3 = QLabel(self)
        self.pz3.setPixmap(QPixmap("images/starChefSignature.jpg"))
        self.pz3.setGeometry(QRect(520, 350, 200, 200))

        self.pzName3 = QLabel("스타 쉐프 시그니쳐", self)
        self.pzName3.move(520, 560)
        self.pzName3.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.pzPrice3 = QLabel("L 36900원~ M 29900원~", self)
        self.pzPrice3.move(520, 580)
        self.pzPrice3.setFont(QFont("여기어때 잘난체 OTF", 9))

        self.pzExplain3 = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pzExplain3.move(520, 600)
        self.pzExplain3.setFont(QFont("여기어때 잘난체 OTF", 8))
        self.pzExplain3.setStyleSheet("Color : gray")

        self.pz3Btn = QPushButton(self)
        self.pz3Btn.resize(200, 260)
        self.pz3Btn.move(520, 350)

        self.pz4 = QLabel(self)
        self.pz4.setPixmap(QPixmap("images/starChefSignature.jpg"))
        self.pz4.setGeometry(QRect(80, 640, 200, 200))

        self.pzName4 = QLabel("스타 쉐프 시그니쳐", self)
        self.pzName4.move(80, 850)
        self.pzName4.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.pzPrice4 = QLabel("L 36900원~ M 29900원~", self)
        self.pzPrice4.move(80, 870)
        self.pzPrice4.setFont(QFont("여기어때 잘난체 OTF", 9))

        self.pzExplain4 = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pzExplain4.move(80, 890)
        self.pzExplain4.setFont(QFont("여기어때 잘난체 OTF", 8))
        self.pzExplain4.setStyleSheet("Color : gray")

        self.pz4Btn = QPushButton(self)
        self.pz4Btn.resize(200, 260)
        self.pz4Btn.move(80, 640)

        self.pz5 = QLabel(self)
        self.pz5.setPixmap(QPixmap("images/starChefSignature.jpg"))
        self.pz5.setGeometry(QRect(300, 640, 200, 200))

        self.pzName5 = QLabel("스타 쉐프 시그니쳐", self)
        self.pzName5.move(300, 850)
        self.pzName5.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.pzPrice5 = QLabel("L 36900원~ M 29900원~", self)
        self.pzPrice5.move(300, 870)
        self.pzPrice5.setFont(QFont("여기어때 잘난체 OTF", 9))

        self.pzExplain5 = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pzExplain5.move(300, 890)
        self.pzExplain5.setFont(QFont("여기어때 잘난체 OTF", 8))
        self.pzExplain5.setStyleSheet("Color : gray")

        self.pz5Btn = QPushButton(self)
        self.pz5Btn.resize(200, 260)
        self.pz5Btn.move(300, 640)

        self.pz6 = QLabel(self)
        self.pz6.setPixmap(QPixmap("images/starChefSignature.jpg"))
        self.pz6.setGeometry(QRect(520, 640, 200, 200))

        self.pzName6 = QLabel("스타 쉐프 시그니쳐", self)
        self.pzName6.move(520, 850)
        self.pzName6.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.pzPrice6 = QLabel("L 36900원~ M 29900원~", self)
        self.pzPrice6.move(520, 870)
        self.pzPrice6.setFont(QFont("여기어때 잘난체 OTF", 9))

        self.pzExplain6 = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pzExplain6.move(520, 890)
        self.pzExplain6.setFont(QFont("여기어때 잘난체 OTF", 8))
        self.pzExplain6.setStyleSheet("Color : gray")

        self.pz6Btn = QPushButton(self)
        self.pz6Btn.resize(200, 260)
        self.pz6Btn.move(520, 640)


class AboutWidget(QWidget):
    def __init__(self, parent=None):
        super(AboutWidget, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/toppingBack.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.pz1 = QLabel(self)
        self.pz1.setPixmap(QPixmap("images/starChefSignature.png"))
        self.pz1.setGeometry(QRect(50, 300, 300, 300))

        self.pzName1 = QLabel("스타 쉐프 시그니쳐", self)
        self.pzName1.move(50, 250)
        self.pzName1.setFont(QFont("여기어때 잘난체 OTF", 20))

        self.pzPrice6 = QLabel("사이즈 선택", self)
        self.pzPrice6.move(400, 280)
        self.pzPrice6.setFont(QFont("여기어때 잘난체 OTF", 15))

        sizeL = QRadioButton('L 36,900원', self)
        sizeL.move(400, 315)
        sizeL.setChecked(True)

        sizeM = QRadioButton(self)
        sizeM.move(510, 315)
        sizeM.setText('M 29,900원')

        self.lbl = QLabel('도우 선택', self)
        self.lbl.move(400, 370)
        self.lbl.setFont(QFont("여기어때 잘난체 OTF", 15))

        cb = QComboBox(self)
        cb.addItem('도우 선택')
        cb.addItem('슈퍼시드 함유 도우')
        cb.addItem('오리지널 도우(칠리핫도그 엣지)')
        cb.addItem('오리지널 도우(더블 치즈엣지)')
        cb.addItem('오리지널 도우(기본)')
        cb.addItem('나폴리 도우')
        cb.addItem('씬 도우(기본 갈릭디핑 소스 미제공')
        cb.move(400, 400)

        cb.activated[str].connect(self.onActivated)

        self.pzExplain1 = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pzExplain1.move(520, 890)
        self.pzExplain1.setFont(QFont("여기어때 잘난체 OTF", 8))
        self.pzExplain1.setStyleSheet("Color : gray")

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


class PreWidget(QWidget):
    def __init__(self, parent=None):
        super(PreWidget, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/premiumPizza.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 200)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 200)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 200)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 200)

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


class ClaWidget(QWidget):
    def __init__(self, parent=None):
        super(ClaWidget, self).__init__(parent)

        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/classicPizza.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.fameBtn = QPushButton(self)
        self.fameBtn.resize(200, 100)
        self.fameBtn.move(0, 200)

        self.recommendBtn = QPushButton(self)
        self.recommendBtn.resize(200, 100)
        self.recommendBtn.move(200, 200)

        self.premiumBtn = QPushButton(self)
        self.premiumBtn.resize(200, 100)
        self.premiumBtn.move(400, 200)

        self.classicBtn = QPushButton(self)
        self.classicBtn.resize(200, 100)
        self.classicBtn.move(600, 200)

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

    def setPrice(self):
        self.pzPrice.setText(str(self.num_spin.value() * self.price) + "원")
        self.pzPrice.resize(self.pzPrice.sizeHint())

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
