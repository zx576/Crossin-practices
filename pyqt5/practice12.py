
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication,QAction)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        positions = [(i,j)for i in range(5) for j in range(4)]
        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.handle)
            grid.addWidget(button,*position)
    # def click(self,btn,name):
        # print(btn)
        # btn.clicked.connect(print(name))
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('practice12')
        self.show()
    def handle(self):
        sender = self.sender().text()
        # sender = self.sender()
        # self.statusBar().showMessage(sender.text()+' was pressed')
        # print(name)
        # print(sender)

        # 绑定一个事件
        # selfaction =



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
