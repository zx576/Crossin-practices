'''

'''

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(r'E:\GIT\practice\Crossin-practices\pyqt5\rain.jpg')

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300,300)
        self.setWindowTitle('QCheckBox')
        self.show()

    # def changetitle(self,state):
    #     if state == Qt.Checked:
    #         self.setWindowTitle('QCheckBox')
    #     else:
    #         self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
