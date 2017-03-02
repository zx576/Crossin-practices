'''

'''

import sys
from PyQt5.QtWidgets import (QPushButton, QWidget,
    QLineEdit, QApplication)

class Button(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True)

    def dragenterevent(self,e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropevent(self,e):
        self.setText(e.mimeData().text())

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        edit = QLineEdit('',self)
        edit.setDragEnabled(True)
        edit.move(50,65)

        button = Button('Button',self)
        button.move(190,65)


        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QComboBox')
        # self

    def onactivated(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
