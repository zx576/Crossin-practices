'''

'''

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
    QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        hbox = QHBoxLayout(self)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame()

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
