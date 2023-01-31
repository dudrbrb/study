import requests
from urllib import parse
from bs4 import BeautifulSoup
keyword = input("검색어 : ")
# url = "https://bsearch.interpark.com/dsearch/book.jsp?sch=all&query=" + parse.quote(keyword)

# headers = {'User-Agent':'--ari/537.36'}
# res = requests.get(url, headers = headers)
# res.raise_for_status() # 오류가 생기면 셀종료
# soup = BeautifulSoup(res.text, "html.parser")

# print(url)

print( parse.quote(keyword).encode('euc-kr'))

# allprice = []

# #국내 도서
# allcontents = soup.find('span',attrs = {'id' :'bookresult'}).find_all('div',attrs = {'class': 'list_wrap'})


# for contents in allcontents:
#     price = contents.find('div',attrs ={'class': 'price'})

#     if price != None:

#         try :
#             price1 = contents.find('span',attrs ={'class': 'nowMoney'}).get_text()
#             allprice.append(price1)
#         except :
#             try:
#                 price1 = contents.find('p',attrs = {'class': 'defaultNum'}).get_text()
#                 allprice.append(price1)
#             except :
#                 allprice.append(price.get_text())


# #해외 도서
# allcontents = soup.find('span',attrs = {'id' :'foreignresult'}).find_all('div',attrs = {'class': 'list_wrap'})


# for contents in allcontents:
#     price = contents.find('div',attrs ={'class': 'price'})

#     if price != None:

#         try :
#             price1 = contents.find('span',attrs ={'class': 'nowMoney'}).get_text()
#             allprice.append(price1)
#         except :
#             try:
#                 price1 = contents.find('p',attrs = {'class': 'defaultNum'}).get_text()
#                 allprice.append(price1)
#             except :
#                 allprice.append(price.get_text())



# print(allprice)