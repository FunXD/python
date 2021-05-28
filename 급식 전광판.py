from datetime import datetime
import requests
from bs4 import BeautifulSoup

def lunch():
    webpage = requests.get("http://icpa.icehs.kr/foodlist.do?m=070306&s=icpa")
    soup = BeautifulSoup(webpage.content, "html.parser")
    menu = soup.select_one('td.today').get_text()
    print(menu[2:])

def weather():
    webpage = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = BeautifulSoup(webpage.content, "html.parser")
    data1 = soup.find('div', {'class':'weather_box'})
    find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
    print('현재 온도: '+find_currenttemp+'℃')

print(datetime.today().strftime("%m월 %d일 %p %H:%M"))
weather()
print('-'*25)
lunch()
