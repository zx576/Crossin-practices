# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
'''

'''

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAction = QAction(QIcon('exit.png'),'&Exit',self)
        # 设置快捷键
        exitAction.setShortcut('Ctrl+Q')
        # 设置状态提示
        exitAction.setStatusTip('Exit application')
        # 绑定退出函数
        exitAction.triggered.connect(qApp.quit)
        # 设置状态标签
        self.statusBar()
        # 目录
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&file')
        # 添加触发函数
        fileMenu.addAction(exitAction)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('menubar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
