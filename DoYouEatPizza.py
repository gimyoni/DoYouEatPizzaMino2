#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 스택 위젯의 기본 사용법
# * 여러 위젯을 한 위젯 공간에 선택될 수 있도록 한다.

import sys
import pandas as pd
import self as self

from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


def addData(date, amount, price):
    pizza_data = pd.read_excel("pizzaInfo.xlsx", sheet_name="Sheet1")
    new_row = {'날짜': date, '메뉴': '스타 셰프 시그니처', '개수': amount, '가격': price}
    pizza_data = pizza_data.append(new_row, ignore_index=True)
    print(pizza_data)

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

        self.central_widget.addWidget(sub_widget)
        self.central_widget.setCurrentWidget(sub_widget)

    def clickRec(self):

        rec_widget = RecWidget(self)
        rec_widget.fameBtn.clicked.connect(self.clickFame)
        rec_widget.premiumBtn.clicked.connect(self.clickPre)
        rec_widget.classicBtn.clicked.connect(self.clickCla)

        self.central_widget.addWidget(rec_widget)
        self.central_widget.setCurrentWidget(rec_widget)

    def clickPre(self):

        pre_widget = PreWidget(self)
        pre_widget.fameBtn.clicked.connect(self.clickFame)
        pre_widget.recommendBtn.clicked.connect(self.clickRec)
        pre_widget.classicBtn.clicked.connect(self.clickCla)
        pre_widget.pz1Btn.clicked.connect(self.clickPz1)

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



class AboutWidget(QWidget):
    def __init__(self, parent=None):
        super(AboutWidget, self).__init__(parent)

        self.sizePrice = 0
        self.doughPrice = 0
        self.pizzaAmount = 1
        self.pizzaPrice = self.sizePrice + self.doughPrice
        self.resultPrice = 0

        self.date = QDate.currentDate()
        self.time = QTime.currentTime()

        self.result = []
        self.famePz = QLabel(self)
        self.famePz.resize(800, 950)
        pixmap = QPixmap("images/toppingBack.png")
        self.famePz.setPixmap(QPixmap(pixmap))

        self.pizzaPrice = 0
        self.txtPrice = QLabel(str(self.pizzaPrice), self)
        self.txtPrice.move(50, 850)
        self.txtPrice.setFont(QFont("여기어때 잘난체 OTF", 10))

        self.pz1 = QLabel(self)
        self.pz1.setPixmap(QPixmap("images/starChefSignature.png"))
        self.pz1.setGeometry(QRect(50, 300, 300, 300))

        self.pzName1 = QLabel("스타 쉐프 시그니쳐", self)
        self.pzName1.move(50, 250)
        self.pzName1.setFont(QFont("여기어때 잘난체 OTF", 20))

        self.sizeTxt = QLabel("사이즈 선택", self)
        self.sizeTxt.move(400, 280)
        self.sizeTxt.setFont(QFont("여기어때 잘난체 OTF", 15))


        dSize = QComboBox(self)
        dSize.addItem('사이즈 선택')
        dSize.addItem('L 36,900원')
        dSize.addItem('M 29,900원')

        dSize.move(400, 320)

        dSize.activated[str].connect(self.doughSizeFunc)

        self.doughTxt = QLabel('도우 선택', self)
        self.doughTxt.move(400, 370)
        self.doughTxt.setFont(QFont("여기어때 잘난체 OTF", 15))

        cb = QComboBox(self)
        cb.addItem('도우 선택')
        cb.addItem('슈퍼시드 함유 도우')
        cb.addItem('오리지널 도우(칠리핫도그 엣지)')
        cb.addItem('오리지널 도우(더블 치즈엣지)')
        cb.addItem('오리지널 도우(기본)')
        cb.addItem('나폴리 도우')
        cb.addItem('씬 도우(기본 갈릭디핑 소스 미제공')
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

        self.pzAmountLabel = QLabel('1',self)
        self.pzAmountLabel.move(400, 500)
        self.pzAmountLabel.setFont(QFont("여기어때 잘난체 OTF", 15))

        self.spinbox.valueChanged.connect(self.value_changed)

        self.pzExplain1 = QLabel("#드라이에이징_스테이크 #트러플", self)
        self.pzExplain1.move(520, 890)
        self.pzExplain1.setFont(QFont("여기어때 잘난체 OTF", 8))
        self.pzExplain1.setStyleSheet("Color : gray")


        self.buyBtn = QPushButton("구매", self)
        self.buyBtn.resize(200, 100)
        self.buyBtn.move(400, 600)
        self.buyBtn.clicked.connect(self.clickBuy)

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

        # if self.doughPrice>0 and self.price > 0:
        #     self.pizzaPrice -= self.doughPrice
        self.doughPrice = 0
        if text=='슈퍼시드 함유 도우':
            self.doughPrice += 2000
        elif text =='오리지널 도우(칠리핫도그 엣지)':
            self.doughPrice += 5000
        elif text =='오리지널 도우(더블 치즈엣지)':
            self.doughPrice += 5000

        self.pizzaPrice = (self.doughPrice+self.sizePrice)
        self.resultPrice = self.pizzaPrice* self.pizzaAmount
        self.txtPrice.setText(str(self.resultPrice))
        self.txtPrice.adjustSize()
        print(self.resultPrice)

    def doughSizeFunc(self, text):
        self.sizeTxt.setText(text)
        self.sizeTxt.adjustSize()

        # if self.doughPrice > 0 and self.price > 0:
        #     self.price -= self.doughPrice
        self.sizePrice = 0
        if text == 'L 36,900원':
            self.sizePrice += 36900
        elif text == 'M 29,900원':
            self.sizePrice += 29900

        self.pizzaPrice = (self.doughPrice+self.sizePrice)
        self.resultPrice = self.pizzaPrice * self.pizzaAmount
        self.txtPrice.setText(str(self.resultPrice))
        self.txtPrice.adjustSize()
        print(self.resultPrice)

    def clickBuy(self):
        print(self.resultPrice)
        addData(self.date.toString(Qt.ISODate), self.pizzaAmount, self.resultPrice)

        


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

        opacity = QGraphicsOpacityEffect(self.pz2Btn)
        opacity.setOpacity(0)
        self.pz2Btn.setGraphicsEffect(opacity)

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

        opacity = QGraphicsOpacityEffect(self.pz3Btn)
        opacity.setOpacity(0)
        self.pz3Btn.setGraphicsEffect(opacity)

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

        opacity = QGraphicsOpacityEffect(self.pz4Btn)
        opacity.setOpacity(0)
        self.pz4Btn.setGraphicsEffect(opacity)

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

        opacity = QGraphicsOpacityEffect(self.pz5Btn)
        opacity.setOpacity(0)
        self.pz5Btn.setGraphicsEffect(opacity)

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

        opacity = QGraphicsOpacityEffect(self.pz6Btn)
        opacity.setOpacity(0)
        self.pz6Btn.setGraphicsEffect(opacity)

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

        opacity = QGraphicsOpacityEffect(self.pz2Btn)
        opacity.setOpacity(0)
        self.pz2Btn.setGraphicsEffect(opacity)

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

        opacity = QGraphicsOpacityEffect(self.pz3Btn)
        opacity.setOpacity(0)
        self.pz3Btn.setGraphicsEffect(opacity)

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

        opacity = QGraphicsOpacityEffect(self.pz4Btn)
        opacity.setOpacity(0)
        self.pz4Btn.setGraphicsEffect(opacity)

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

        opacity = QGraphicsOpacityEffect(self.pz5Btn)
        opacity.setOpacity(0)
        self.pz5Btn.setGraphicsEffect(opacity)

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

        opacity = QGraphicsOpacityEffect(self.pz6Btn)
        opacity.setOpacity(0)
        self.pz6Btn.setGraphicsEffect(opacity)

class SubWidget(QWidget):
    def __init__(self, parent=None):
        super(SubWidget, self).__init__(parent)

        self.subBack = QLabel(self)
        self.subBack.resize(800, 950)
        pixmap = QPixmap("images/toppingBack.png")
        self.subBack.setPixmap(QPixmap(pixmap))



if __name__ == '__main__':
       app = QApplication([])
       window = MainWindow()
       window.show()
       app.exec_()