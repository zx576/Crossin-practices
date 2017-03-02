'''

'''

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl = QLabel('ubantu',self)
        combo = QComboBox(self)
        combo.addItem('ubantu')
        combo.addItem('mandriva')
        combo.addItem('arch')

        combo.move(50,50)
        self.lbl.move(50,150)
        combo.activated[str].connect(self.onactivated)

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QComboBox')
        self.show()

    def onactivated(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
