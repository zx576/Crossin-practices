'''
2017.2.22:需要添加一个qframe
'''


import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
QLineEdit,QPushButton, QApplication,QAction,qApp,QFrame)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.accept = []
        self.accept_str = ''
    def initUI(self):

        grid = QGridLayout()
        # 将界面加入 frame
        # frame = QFrame(grid)
        # frame.setFrameShape(QFrame.StyledPanel)

        self.setLayout(grid)
        # 显示部分
        self.line1 = QLineEdit()
        grid.addWidget(self.line1,0,1)
        # 计算机主体
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        positions = [(i,j)for i in range(1,6) for j in range(1,5)]
        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.accept_input)
            grid.addWidget(button,*position)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('practice12')
        self.setWindowOpacity(0.5)
        self.show()
    def accept_input(self):
        sender = self.sender().text()
        self.handle_input(sender)
        self.line1.setText(self.accept_str)
    def handle_input(self,sender):
        # sender = str(sender)
        if sender == '=':
            self.caculate()
        elif sender == 'Cls':
            self.accept_str = ''
        elif sender == 'Bck':
            self.accept_str = self.accept_str[:-1]
        elif sender == 'Close':
            self.closeapp()
        else:
            self.accept_str += sender
    def closeapp(self):
        qApp.quit
    def caculate(self):
        last_word = self.accept_str[-1]
        first_word = self.accept_str[0]
        # 去掉头尾的运算符号
        if last_word == '+' or last_word == '-' or \
            last_word == '*' or last_word == '/':
            self.accept_str = self.accept_str[:-1]
        elif first_word == '+' or first_word == '-' or \
            first_word == '*' or first_word == '/':
            self.accept_str = self.accept_str[1:]
        result = eval(self.accept_str)
        self.accept_str = str(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
