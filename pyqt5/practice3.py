# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

'''
code 3
Showing a tooltip
'''

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('this is a <b>Qwidget</b> widget')
        btn = QPushButton('Button',self)
        btn.setToolTip('this is a <b>pushbutton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())