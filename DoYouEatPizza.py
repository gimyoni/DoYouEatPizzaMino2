import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.time = QTime.currentTime()
        self.initUI()


    def initUI(self):

        self.realDate = QLabel(self.date.toString(Qt.ISODate), self)
        self.realDate.move(50, 50)

        self.realTime = QLabel(self.time.toString(Qt.DefaultLocaleShortDate),self)
        self.realTime.move(140, 50)

        self.adv = QPushButton('광고', self)
        self.adv.resize(700, 750)
        self.adv.move(50, 100)
        self.adv.clicked.connect(self.clickMethod)

        self.setWindowTitle('PizzaKiosk')
        self.setWindowIcon(QIcon('images/pizzaIcon.png'))
        self.resize(800, 900)
        self.center()
        self.show()


    def clickMethod(self):
        print('Clicked Pyqt button.')


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())