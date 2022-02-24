import sys
import threading

from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *

from bs4 import BeautifulSoup
import requests


form_class = uic.loadUiType('ui/CalculatorApp.ui')[0] # ui 불러오기


class CalculatorApp(QMainWindow, form_class):
    def __init__(self):  # 초기화자
        super().__init__()
        self.setupUi(self)  # 만들어놓은 test.ui 연결
        self.setWindowTitle('계산기')  # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/google_logo.png'))  # 윈도우 아이콘 설정
        self.statusBar().showMessage('Calculator Application Ver1.0')  # 윈도우
        self.num1_button.clicked.connect(self.num1_button_clicked)


    def num1_button_clicked(self):
        self.txt_label.setText('1')


        # def trans_button_clicked(self):
        #     trans_txt = self.txtKor.text()
        #     trans = googletrans.Translator()

        # cal = cal + num1
        # # print(cal)
        # oper1 = input('사칙연산자:')
        # cal = cal + oper1
        # # print(cal)
        # num2 = input('두번째 클릭한 숫자:')
        # cal = cal + num2
        # # print(cal)
        # result = eval(cal)
        # print(f"{cal}={result}")

app = QApplication(sys.argv)
window = CalculatorApp()
window.show()
app.exec_()


