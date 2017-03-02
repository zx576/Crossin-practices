# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
'''
添加标签
'''
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 添加label
        lbl1 = QLabel('zetcode',self)
        # 设置位置
        lbl1.move(15,10)
        lbl2 = QLabel('label2',self)
        lbl2.move(35,40)
        lbl3 = QLabel('label3',self)
        lbl3.move(55,70)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('practice10')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
