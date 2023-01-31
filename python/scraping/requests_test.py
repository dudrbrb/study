import requests
from bs4 import BeautifulSoup
import pandas as pd


alltitle = []
allprice = []
headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0%2014&cat_id=&frm=NVSHATC'
s = requests.Session()

res = s.get(url, headers = headers) 
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')



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