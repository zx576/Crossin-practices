# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
'''
设置点击退出
'''
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 初始化一个动作
        exitAction = QAction('&Exit',self)
        # 设置这个动作的快捷键
        exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('Exit application')
        # 这个动作的触发函数
        exitAction.triggered.connect(qApp.quit)
        # 增加工具栏
        self.toolbar = self.addToolBar('Exit')
        #
        self.addToolBar('&File')
        self.toolbar.addAction(exitAction)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('menubar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
