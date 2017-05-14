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
        # 初始化父类
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置提示栏字体
        QToolTip.setFont(QFont('Monoca',10))
        # 设置提示内容
        self.setToolTip('this is a <b>Qwidget</b> widget')
        # 新建 btn
        btn = QPushButton('Button',self)
        # 设置 btn 提示
        btn.setToolTip('this is a <b>pushbutton</b> widget')
        # 自适应大小
        btn.resize(btn.sizeHint())
        # btn 位置
        btn.move(10,50)
        # 设置 GUI 框大小及位置
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
