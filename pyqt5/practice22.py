'''

'''

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(30,100)
        self.lbl.move(30,50)
        # str 会最为参数传入 onchanged 函数
        qle.textChanged[str].connect(self.onchanged)


        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QCheckBox')
        self.show()

    def onchanged(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
