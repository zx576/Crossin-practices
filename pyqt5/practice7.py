# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
'''
调出状态
'''
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 状态栏的显示
        self.statusBar().showMessage('ready')
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
