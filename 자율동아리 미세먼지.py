from datetime import datetime
import requests
from bs4 import BeautifulSoup

def weather():
    webpage = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = BeautifulSoup(webpage.content, "html.parser")
    data1 = soup.find('div', {'class':'weather_box'})
    find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
    print('현재 온도: '+find_currenttemp+'℃')

def dust():
    webpage = requests.get('https://weather.naver.com/today/11185106')
    soup = BeautifulSoup(webpage.content, "html.parser")
    data1 = soup.find('div', {'class':'ttl_area'})
    global find_currentdust
    find_currentdust = data1.find('em',{'class': 'level_text'}).text
    print('미세먼지: '+find_currentdust)



print(datetime.today().strftime("%m월 %d일 %p %H:%M"))
weather()
dust()
if find_currentdust == '좋음' or find_currentdust == '보통':
    print('현재 미세먼지는',find_currentdust,'으로 야외활동에 적합합니다')
else:
    print('야외활동 금지!')
print('-'*25)
