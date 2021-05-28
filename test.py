from datetime import datetime
import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://weather.naver.com/today/11185106')
soup = BeautifulSoup(webpage.content, "html.parser")

def 날씨():
    webpage = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = BeautifulSoup(webpage.content, "html.parser")
    data1 = soup.find('div', {'class':'weather_box'})
    find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
    print('현재 온도: '+find_currenttemp+'℃')

def 미세먼지():
    data1 = soup.find('li', {'class':'item_today level4_2'})
    find_currentdust = data1.find('em',{'class': 'level_text'}).text
    print('미세먼지: '+find_currentdust)

def 초미세먼지():
    data1 = soup.find('li', {'class':'item_today level4_1'})
    find_currentstrongdust = data1.find('em',{'class': 'level_text'}).text
    print('초미세먼지: '+find_currentstrongdust)

def 습도():
    find_currenthum = data1.find('span',{'class': 'todayhum'}).text
    print('현재 습도: '+find_currenthum+'%')


print(datetime.today().strftime("%m월 %d일 %p %H:%M"))
날씨()
미세먼지()
초미세먼지()
