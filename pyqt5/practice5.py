# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

'''
code 5
Message Box
'''
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle('messagebox')
        self.show()
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message','r u sure to quit?',QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())