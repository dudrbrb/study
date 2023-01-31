from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from bs4 import BeautifulSoup

alltitle = []
allprice = []
keyword = input('키워드를 입력하세요 : ')

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(3)

for i in range(1,4):
    url = 'https://search.shopping.naver.com/search/all?query={}&cat_id=&frm=NVSHATC&pagingIndex={}'.format(keyword, i)
    driver.get(url)


    #스크롤 내리기 이동 전 위치
    scroll_location = driver.execute_script("return document.body.scrollHeight")

    while True:
        #현재 스크롤의 가장 아래로 내림
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
        #전체 스크롤이 늘어날 때까지 대기
        time.sleep(2)
        
        #늘어난 스크롤 높이
        scroll_height = driver.execute_script("return document.body.scrollHeight")

        #늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
        if scroll_location == scroll_height:
            break
            
        #같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
        else:
            #스크롤 위치값을 수정
            scroll_location = driver.execute_script("return document.body.scrollHeight")



    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    contents = soup.find('ul', attrs={'class' : 'list_basis'}).find_all('li', attrs={'class' : 'basicList_item__0T9JD'})
    for content in contents :
        title = content.find('div', attrs={'class' : 'basicList_title__VfX3c'}).get_text()
        price = content.find('span', attrs={'class' : 'price_num__S2p_v'}).get_text()[:-1]

        alltitle.append(title)
        allprice.append(price)


print(alltitle)
data = {
        '상품명' : alltitle,
        '가격' : allprice
        }


df = pd.DataFrame(data = data, columns = ['상품명','가격'])
df.to_excel('테스트.xlsx')