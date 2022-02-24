import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('ui/signal.ui')[0] #ui 불러오기

class Mysignal(QMainWindow, form_class):
    def __init__(self):  # 초기화자
        super().__init__()
        self.setupUi(self)  # 만들어놓은 test.ui 연결
        self.setWindowTitle('신호전송')  # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/test_icon.png'))  # 윈도우 아이콘 설정
        self.statusBar().showMessage('Signal Application Ver1.0')  # 윈도우 상태표시줄 입력
        self.dial.valueChanged.connect(self.lcdNumber.display)



app = QApplication(sys.argv)
window = Mysignal()
window.show()
app.exec_()