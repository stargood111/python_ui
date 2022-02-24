import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('ui/test.ui')[0] #ui 불러오기

class MyWindow(QMainWindow, form_class):
    def __init__(self): #초기화자
        super().__init__()
        self.setupUi(self) #만들어놓은 test.ui 연결
        self.setWindowTitle('연습용 프로그램') #윈도우 제목 설정
        self.setWindowIcon(QIcon('img/test_icon.png')) #윈도우 아이콘 설정
        self.statusBar().showMessage('Test Application Ver1.0') #윈도우 상태표시줄 입력
        self.test_button.clicked.connect(self.btn_clicked) #버튼 연결
        self.test_button.clicked.connect(self.btn_clicked2)
        self.clear_button.clicked.connect(self.clear_text)

    def btn_clicked(self):
        # print('버튼이 클릭되었습니다.')
        self.output_label.setText('안녕!반갑습니다!!!')

    def btn_clicked2(self):
        self.output_label2.setText('두번째 텍스트 출력!!!')

    def clear_text(self):
        self.output_label.clear()
        self.output_label2.clear()


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

