# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('practice14')
        self.show()
    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape():
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

