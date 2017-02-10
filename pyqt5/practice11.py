# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        okbtn = QPushButton('ok',self)
        cancelbtn = QPushButton('cancel',self)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okbtn)
        hbox.addWidget(cancelbtn)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('practice11')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

