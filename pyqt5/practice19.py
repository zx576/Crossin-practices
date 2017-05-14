'''

'''

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        cb = QCheckBox('showtitle',self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changetitle)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changetitle(self,state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
