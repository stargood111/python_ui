import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import googletrans

trans = googletrans.Translator() #구글 번역 클래스 Translator로 객체생성

form_class = uic.loadUiType('ui/google_trans.ui')[0] #ui 불러오기

class TransApp(QMainWindow, form_class):
    def __init__(self):  # 초기화자
        super().__init__()
        self.setupUi(self)  # 만들어놓은 test.ui 연결
        self.setWindowTitle('한줄 번역기')  # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/google_logo.png'))  # 윈도우 아이콘 설정
        self.statusBar().showMessage('Google Trans Application Ver1.0')  # 윈도우 상태표시줄 입력
        self.trans_button.clicked.connect(self.trans_button_clicked)
        self.trans_button.clicked.connect(self.trans_button_clicked1)
        self.trans_button.clicked.connect(self.trans_button_clicked2)
        self.clear_botton.clicked.connect(self.clear_botton_clicked)

    def trans_button_clicked(self):
        trans_txt = self.txtKor.text()
        trans = googletrans.Translator()

        ret1 = trans.translate(trans_txt, dest='en')
        self.txtEng.setText(ret1.text)

    def trans_button_clicked1(self):
        trans_txt = self.txtKor.text()
        trans = googletrans.Translator()

        ret2 = trans.translate(trans_txt, dest='ja')
        self.txtJap.setText(ret2.text)

    def trans_button_clicked2(self):
        trans_txt = self.txtKor.text()
        trans = googletrans.Translator()

        ret3 = trans.translate(trans_txt, dest='zh-cn')
        self.txtChi.setText(ret3.text)

    def clear_botton_clicked(self):
        self.txtKor.clear()
        self.txtEng.clear()
        self.txtJap.clear()
        self.txtChi.clear()







app = QApplication(sys.argv)
window = TransApp()
window.show()
app.exec_()
