# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
'''
learn from zetcode
code no.1
build a simple application
'''

if __name__ == '__main__':
    # 建立pyqt应用
    app = QApplication(sys.argv)
    # 组件初始化
    w = QWidget()
    # 定义大小
    w.resize(250,150)
    # 定义位置
    w.move(300,300)
    # 定义标题
    w.setWindowTitle('simple')
    # 显示
    w.show()
    # 退出
    sys.exit(app.exec_())