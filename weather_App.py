import sys
import threading

from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *

from bs4 import BeautifulSoup
import requests

form_class = uic.loadUiType('ui/weatherApp.ui')[0] # ui 불러오기

class WeatherCrawler(QThread): # 쓰레드 클래스로 선언
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def weather_crawling(self, weather_area):
        weather_result = [] # 날씨 크롤링 결과를 반환할 빈리스트 생성
        result_flug = 0

        weather_html = requests.get(f'https://search.naver.com/search.naver?query={weather_area}날씨')
        # print(weather_html) # 200 응답코드 확인

        weather_soup = BeautifulSoup(weather_html.text, 'html.parser')  # 파싱한 응답결과 html
        # print(weather_soup)
        try:
            area_title = weather_soup.find('h2', {'class': 'title'}).text  # 날씨를 검색한 지역명 크롤링
            today_temper = weather_soup.find('div', {'class': 'temperature_text'}).text  # 오늘 기온 크롤링
            today_temper = today_temper[6:9].strip()  # 오늘 기온만 인덱싱한 후 양쪽 공백문자 제거
            yesterday_weather = weather_soup.find('p', {'class': 'summary'}).text  # 어제날씨비교 크롤링
            yesterday_weather = yesterday_weather[0:13].strip()
            today_weather = weather_soup.find('span',
                                              {'class': 'weather before_slash'}).text  # 오늘 날씨(ex:맑음, 흐림, 구름많음...)
            today_rain = weather_soup.find('dd', {'class': 'desc'}).text  # 강수확률


            ## 강수확률, 습도, 풍속 크롤링
            # weather_list = weather_soup.select('dl.summary_list>dd')
            # print('강수확률:', weather_list[0].text)
            # print('습도:', weather_list[1].text)
            # print('풍속:', weather_list[2].text)
            # print(weather_list)

            dust_info = weather_soup.find_all('span', {'class': 'txt'})  # 미세먼지 정보
            dust1 = dust_info[0].text  # 미세먼지
            dust2 = dust_info[1].text  # 초미세먼지
        except:
            # 해외 도시 검색시 크롤링될 태그 정의
            try:
                area_title = weather_soup.find('span', {'class': 'btn_select'}).text  # 날씨를 검색한 지역명 크롤링
                area_title = area_title.strip()
                today_temper = weather_soup.find('span', {'class': 'todaytemp'}).text  # 오늘 기온 크롤링
                today_temper = f"{today_temper}°"
                today_weather = weather_soup.find('p', {'class': 'cast_txt'}).text  # 오늘 날씨(ex:맑음, 흐림, 구름많음...)
                today_weather = today_weather[0:2].strip()
                yesterday_weather = weather_soup.find('p', {'class': 'cast_txt'}).text
                today_rain = '-'
                dust1 = '-'
                dust2 = '-'
                result_flug = 0
            except:
                area_title = '검색한 지역은 날씨정보 없음'
                today_temper = '-'
                today_weather = '-'
                yesterday_weather = '-'
                today_rain = '-'
                dust1 = '-'
                dust2 = '-'

        weather_result.append(area_title)
        weather_result.append(today_temper)
        weather_result.append(today_weather)
        weather_result.append(yesterday_weather)
        weather_result.append(today_rain)
        weather_result.append(dust1)
        weather_result.append(dust2)
        weather_result.append(result_flug)

        return weather_result




class WeatherApp(QMainWindow, form_class):
    def __init__(self, parent=None): # 초기화자
        super().__init__(parent)
        self.setupUi(self) # 만들어 놓은 test.ui 연결
        self.setWindowTitle('오늘의 날씨') # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/test_icon.png')) # 윈도우 아이콘 설정
        self.statusBar().showMessage('Weather Application Ver 1.0') # 윈도우 상태표시줄 입력
        self.weatherInfo = WeatherCrawler(self) # 날씨크롤러 클래스의 객체를 생성

        self.search_button.clicked.connect(self.weather_start)
        self.search_button.clicked.connect(self.reflash_function)

    def closeEvent(self):
        self.weatherInfo.close()


    def reflash_function(self):
        self.weather_start()
        threading.Timer(600,self.weather_start).start()

    def weather_start(self): #600초마다 날씨를 다시 호출
        input_area = self.area_input.text() # 입력된 지역명 가져오기
        if input_area ==' ':
            QMessageBox.about(self, '입력오류!','날씨 검색 지역명을 입력하지 않으셨습니다.')
        weather_data = self.weatherInfo.weather_crawling(input_area)
        # 쓰레드 클래스의 weather_crawling 메서드 호출
        # weather_crawling 함수의 리턴값 저장(크롤링한 날씨 정보 리스트)
        # ['남동구 구월동', '3°', '맑음', '어제보다 4° 높아요', '0%', '좋음', '좋음']
        self.temper_label.setText(weather_data[1])
        self.area_label.setText(weather_data[0])
        # self.weather_label.setText(weather_data[2])
        if weather_data[2] == '맑음':
            weather_image = QPixmap('img/sun.png')
            self.weather_label.setPixmap(QPixmap(weather_image))
        elif weather_data[2] == '흐림':
            weather_image = QPixmap('img/cloud.png')
            self.weather_label.setPixmap(QPixmap(weather_image))
        elif weather_data[2] == '비':
            weather_image = QPixmap('img/rain.png')
            self.weather_label.setPixmap(QPixmap(weather_image))
        elif weather_data[2] == '눈':
            weather_image = QPixmap('img/snow.png')
            self.weather_label.setPixmap(QPixmap(weather_image))
        elif weather_data[2] == '구름많음':
            weather_image = QPixmap('img/cloud.png')
            self.weather_label.setPixmap(QPixmap(weather_image))
        else :
            self.weather_label.setText(weather_data[2])


        self.yesterday_label.setText(weather_data[3])
        self.rain_label.setText(weather_data[4])
        self.dust1_label.setText(weather_data[5])
        self.dust2_label.setText(weather_data[6])
        if weather_data[7] == 0:
            QMessageBox.about(self, '지역명 오류!', '입력하신 지역명을 확인하시길 바랍니다.')
        if weather_data[7] == 2:
            QMessageBox.about(self, '해외지역검색', '해외의 지역은 강수확률,미세먼지,초미세먼지 정보가 제공되지 않습니다.')





app = QApplication(sys.argv)
window = WeatherApp()
window.show()
app.exec_()