# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class Communicate(QObject):
    closeAPP = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.c = Communicate()
        self.c.closeAPP.connect(self.close)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('practice14')
        self.show()

    def mousePressEvent(self):
        self.c.closeAPP.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
