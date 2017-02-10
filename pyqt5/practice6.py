# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication,QDesktopWidget
'''
code 6
centering window
'''
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(300,300)
        self.center()
        self.setWindowTitle('center')
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())