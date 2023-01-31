import requests
from bs4 import BeautifulSoup
import pandas as pd
import math 

allkeyword = []
alltitle = []
alldate = []
allurl = []
allsitetitle = []
allnewscontents = []


headers = {'User-Agent': 'Mozilla/5.0'}
keyword = input('검색어를 입력하세요 : ')




# 페이지 수 구하기
url = 'https://www.donga.com/news/search?p=1&query={}&check_news=91&more=1&sorting=1&search_date=3&v1=&v2='.format(keyword)
s = requests.Session()

res = s.get(url, headers = headers) 
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

allpage = math.ceil(int(soup.find('span', attrs={'class' : 'news_count'}).get_text()[:-1]) / 15) -1




for i in range(0, allpage):
        
    url = 'https://www.donga.com/news/search?p={}&query={}&check_news=91&more=1&sorting=1&search_date=3&v1=&v2='.format((15* i)+1, keyword)

    res = s.get(url, headers = headers) 
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')


    contents = soup.find('div', attrs={'class' : 'result_cont'}).find_all('div', attrs={'class' : 'articleList'})
    for content in contents :
        title = content.find('span', attrs={'class' : 'tit'}).get_text()
        date = content.find('span', attrs={'class' : 'date'}).get_text()
        url = content.find('span', attrs={'class' : 'tit'}).find('a')['href']

        


        allkeyword.append(keyword)
        allsitetitle.append('동아일보')
        alltitle.append(title)
        alldate.append(date)
        allurl.append(url)


        res = s.get(url, headers = headers) 
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')

        newscontent =  soup.find('div', attrs={'class' : 'article_txt'}).get_text()
        allnewscontents.append(newscontent)

            


data = {
        '뉴스 사이트' : allsitetitle,
        '키워드' : allkeyword,
        '뉴스 제목' : alltitle,
        '발행 날짜' : alldate,
        'url' : allurl,
        '본문 내용' : allnewscontents
        }


df = pd.DataFrame(data = data, columns = ['뉴스 사이트', '키워드', '뉴스 제목', '발행 날짜', 'url', '본문 내용'])
df.to_excel('테스트.xlsx')