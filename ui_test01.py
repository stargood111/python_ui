import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

label1 = QLabel('안녕하세요')
label1.show()

btn1 = QPushButton('검색버튼')
btn1.show()

app.exec_()