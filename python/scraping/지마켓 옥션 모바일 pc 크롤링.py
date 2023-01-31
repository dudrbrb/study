import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.font
from tksheet import Sheet
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import openpyxl
import re
import datetime

root = Tk()
root.title("G마켓 옥션 데이터수집 프로그램") #제목
root.geometry("1100x700")  #사이즈
root.resizable(False, False)   #사이즈 조절가능하게 하냐? no no
allNotul = []
allshopping = []
allrank = []
allname = []
allprice = []
allship = []
allmarket = []
allreview = []
allshipplace = []
allinternet = []
allsell = []
alladd = []
def Gmarket(keyword, kim) :
    headers = {'User-Agent': 'Mozilla/5.0'}
    basic3 = len(allname)
    for k in range(1,kim+1):
        url = 'https://browse.gmarket.co.kr/search?keyword={}&k=32&p={}'.format(keyword,k)

        try :
            s = requests.Session()
            res = s.get(url,headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'lxml')
        except:
            time.sleep(2)
            s = requests.Session()
            res = s.get(url,headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'lxml')


        lis = soup.find_all('div', attrs = {'module-design-id' : '15'})
        stopper = False
        i = 1
        for lisss in lis :  

            for li in lisss : 
            
                link = li.find('p', attrs= {'class' : 'text__title'})
                if link == None : 
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)
                        allNotul.append('먼저 둘러보세요')
                        alladd.append(k)
                        i += 1 
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == '' or ship == None:
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            

                            allship.append(ship)

                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())
                    

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)

                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                
                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')






                else:
                    if link.get_text() == '먼저 둘러보세요' : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)
                        allNotul.append('먼저 둘러보세요') 
                        alladd.append(k)
                        allrank.append(1)    
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()

                        allprice.append(price)       
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == '' or ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            

                            allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})
                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)




                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        stopper = True 
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                

                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')


                        stopper = True 
                    else :
                        stopper = False


        i = 1
        for lisss in lis :  

            for li in lisss :    

                link = li.find('p', attrs= {'class' : 'text__title'})
                if link == None : 
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)
                        allNotul.append('오늘의 상품이에요')       
                        alladd.append(k)                        
                        i += 1 
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == '' or ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            
                            allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)
            

                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                
                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')

                else:
                    if link.get_text() == '오늘의 상품이에요' : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)
                        allNotul.append('오늘의 상품이에요')    
                        alladd.append(k)                            
                        allrank.append(1)    
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == ''or ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            

                            allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)


                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                
                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')

                        stopper = True 
                    else :
                        stopper = False

        i = 1
        for lisss in lis :  

            for li in lisss :    

                link = li.find('p', attrs= {'class' : 'text__title'})
                if link == None : 
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)

                        allNotul.append('이 상품은 어떠세요?')     
                        alladd.append(k)                          
                        i += 1 
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == ''or ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            

                            allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)


                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                
                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')

                else:
                    if link.get_text() == '이 상품은 어떠세요?' : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)
                        allNotul.append('이 상품은 어떠세요?')
                        alladd.append(k)                        
                        allrank.append(1)            
                        stopper = True 
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == ''or ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            

                            allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)
            

                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                
                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')
                        stopper = True 
                    else :
                        stopper = False
        i = 1
        for lisss in lis :  

            for li in lisss :        

                link = li.find('p', attrs= {'class' : 'text__title'})
                if link == None : 
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 

                        allname.append(name)
                        allNotul.append('스마일배송')   
                        alladd.append(k)                            
                        i += 1 
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == ''or ship == None:
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            

                            allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)


                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                
                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')

                else:
                    if link.get_text() == '스마일배송' : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)
                        alladd.append(k)                        
                        allNotul.append('스마일배송')       
                        allrank.append(1)     
                        stopper = True 
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == '' or ship == None:
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            

                            allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)
                

                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                
                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')
                        stopper = True 
                    else :
                        stopper = False
        i = 1
        for lisss in lis :  

            for li in lisss :      

                link = li.find('p', attrs= {'class' : 'text__title'})
                if link == None : 
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)
                        alladd.append(k)                        
                        allNotul.append('주목할 만한 상품이에요')       
                        i += 1 
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == '' or ship == None:
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            

                            allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)
            

                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)

                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                
                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')

                else:
                    if link.get_text() == '주목할 만한 상품이에요' : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)
                        alladd.append(k)                        
                        allNotul.append('주목할 만한 상품이에요')  
                        allrank.append(1)          
                        stopper = True 
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == '' or ship == None:
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            

                            allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)
                

                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                
                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')
                        stopper = True 
                    else :
                        stopper = False
        i = 1
        for lisss in lis :  

            for li in lisss : 

                link = li.find('p', attrs= {'class' : 'text__title'})
                if link == None : 
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)
                        alladd.append(k)                        
                        allNotul.append('일반상품')       
                        i += 1 
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        ship = li.find('span',attrs = {'class' : 'text__tag'})
                        if ship == None or ship == '' :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)
                            if ship == '' or ship == None :
                                allship.append('무료배송')
                            else :
                                allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)
                

                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                
                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')

                else:
                    if link.get_text() == '일반상품' : 
                        name = li.find('span',attrs = {'class' : 'text__item'}).get_text() 
                        allname.append(name)
                        alladd.append(k)                        
                        allNotul.append('일반상품')    
                        allrank.append(1)        

                        price = li.find('strong',attrs = {'class' : 'text text__value'}).get_text()
                        allprice.append(price)
                        ship = li.find('span',attrs = {'class' : 'text__tag'}).get_text()
                        if ship == '' or None :
                            allship.append('무료배송')
                        else : 
                            ship = re.sub(r'[^0-9]', '', ship)
                            

                            allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text__seller'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            allmarket.append(market.get_text())

                        score = li.find('span',attrs = {'class' : 'image__awards-points'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.get_text()
                            score = re.sub(r'[^0-9]', '', score) 
                            score = int(score)
                            score = str(round(score *0.01 *5,1)) + '점'
                            allreview.append(score)


                        num = li.find('li',attrs = {'class': 'list-item list-item__pay-count'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.find('span').get_text()
                            num = re.sub(r'[^0-9]', '', num)
                            allsell.append(num)
                        shipping = li.find('span', attrs = {'class': 'box__brand'})
                        if shipping  == None :
                            allshipplace.append('국내배송')                

                        else:
                            if shipping.find('span',attrs = {'class': 'text'}) == None :
                                allshipplace.append('국내배송')
                            else :
                                shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                allshipplace.append('해외배송')

                        stopper = True 
                    else :
                        stopper = False

    print(len(allname))
    print(len(allNotul))
    print(len(allrank))
    print(len(allprice))
    print(len(allship))
    print(len(allmarket))
    print(len(allreview))
    print(len(alladd))
    for i in range(basic3, len(allname)):
        allshopping.append('G마켓')

        allinternet.append('PC')
    print(len(allshopping))
    print(len(allshipplace))
    print(len(allreview))

def Auction(keyword,kim):
    basic4 = len(allname)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'} 
    for k in range(1, kim+1): 

        url = 'http://browse.auction.co.kr/search?keyword={}&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%ec%98%a8%ec%8a%b5%eb%8f%84%ea%b3%84&acode=SRP_SU_0100&arraycategory=&encKeyword={}&k=32&p={}'.format(keyword,keyword,k)
        try: 
            s = requests.Session()
            res = s.get(url,headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'lxml')
        except:
            time.sleep(2)
            s = requests.Session()
            res = s.get(url,headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'lxml')        
        lisk = soup.find('div', attrs = { 'id' : 'section--inner_content_body_container'})

        lis = lisk.find_all('div', attrs = {'module-design-id' :'17'})


        stopper = False
        i = 1
        for lisss in lis :     

            for li in lisss :


                link = li.find('p', attrs= {'class' : 'text--title'})
                if link == None :       
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('먼저 둘러보세요')
                        alladd.append(k)                               
                        i += 1 
                        allrank.append(i)

                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)
        
                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append(None)
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)
                    

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)

                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)



                else:
                    if link.get_text() == '먼저 둘러보세요' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('먼저 둘러보세요') 
                        alladd.append(k)                               
                        allrank.append(1)    
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()

                        allprice.append(price)       
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)
                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append('무료배송')
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)



                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)
                        stopper = True 





                    else :
                        stopper = False
        stopper = False
        i = 1
        for lisss in lis :     

            for li in lisss :


                link = li.find('p', attrs= {'class' : 'text--title'})
                if link == None :       
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('오늘의 상품이에요')
                        alladd.append(k)                               
                        i += 1 
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)

                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append(None)
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)
                    

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)

                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)



                else:
                    if link.get_text() == '오늘의 상품이에요' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('오늘의 상품이에요') 
                        alladd.append(k)                               
                        allrank.append(1)    
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()

                        allprice.append(price)       
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)
                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append('무료배송')
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)



                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)
                        stopper = True 





                    else :
                        stopper = False
        stopper = False
        i = 1
        for lisss in lis :     

            for li in lisss :


                link = li.find('p', attrs= {'class' : 'text--title'})
                if link == None :       
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('이 상품은 어떠세요?')
                        alladd.append(k)                               
                        i += 1 
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)

                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append(None)
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)
                    

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)

                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)



                else:
                    if link.get_text() == '이 상품은 어떠세요?' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('이 상품은 어떠세요?') 
                        allrank.append(1)    
                        alladd.append(k)       

                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()

                        allprice.append(price)       
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)
                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append('무료배송')
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)



                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)
                        stopper = True 





                    else :
                        stopper = False
        stopper = False
        i =1
        for lisss in lis :     

            for li in lisss :


                link = li.find('p', attrs= {'class' : 'text--title'})
                if link == None :       
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        alladd.append(k)                               
                        allNotul.append('스마일배송')
                        i += 1 
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)

                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append(None)
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)
                    

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)

                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)



                else:
                    if link.get_text() == '스마일배송' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('스마일배송') 
                        alladd.append(k)                               
                        allrank.append(1)    
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()

                        allprice.append(price)       
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)
                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append('무료배송')
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)



                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)
                        stopper = True 





                    else :
                        stopper = False
        stopper = False
        i = 1
        for lisss in lis :     

            for li in lisss :


                link = li.find('p', attrs= {'class' : 'text--title'})
                if link == None :       
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('주목할 만한 상품이에요')
                        i += 1 
                        allrank.append(i)
                        alladd.append(k)                               
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)

                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append(None)
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)
                    

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)

                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)



                else:
                    if link.get_text() == '주목할 만한 상품이에요' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('주목할 만한 상품이에요') 
                        allrank.append(1)    
                        alladd.append(k)                               
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()

                        allprice.append(price)       
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)
                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append('무료배송')
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)



                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)
                        stopper = True 





                    else :
                        stopper = False
        stopper = False
        i = 1
        for lisss in lis :     

            for li in lisss :


                link = li.find('p', attrs= {'class' : 'text--title'})
                if link == None :       
                    if stopper == True : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        alladd.append(k)                               
                        allNotul.append('일반상품')
                        i += 1 
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)

                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append(None)
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)
                    

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)

                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)



                else:
                    if link.get_text() == '일반등록' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        alladd.append(k)                               
                        allNotul.append('일반상품') 
                        allrank.append(1)    
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()

                        allprice.append(price)       
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            ship = re.sub(r'[^0-9]', '', ship)
                            if ship == '원' or ship == '' or ship == ' ' or ship == None:
                                allship.append('무료배송')
                            else :
                                allship.append(ship)


                        market = li.find('a',attrs = {'class': 'link--shop'})
                        if market == None :
                            allmarket.append('스마일배송')
                        else :
                            market = market.get_text()
                            market = market.replace('판매자', '')
                            allmarket.append(market)

                        score = li.find('li',attrs = {'class' : 'item awards'})

                        if score == None :
                            allreview.append(None)
                        else : 
                            score = score.find('span').get_text()
                            score = score.replace('후기평점 ', '')
                            allreview.append(score)



                        num = li.find('span',attrs = {'class': 'text--buycnt'})
                        if num == None :
                            allsell.append(None)
                        else :
                            num = num.get_text()
                            num = num.replace('구매 ', '')
                            allsell.append(num)
                        stopper = True 





                    else :
                        stopper = False



    print(len(allname))
    print(len(allNotul))
    print(len(allrank))
    print(len(allprice))
    print(len(allship))
    print(len(allmarket))
    print(len(allreview))
    print(len(allsell))

    for i in range(basic4, len(allname)):
        allshopping.append('옥션')
        allshipplace.append(None)
        allinternet.append('PC')







def GmarketMobile(keyword,kim)  :
    before = len(allinternet)

    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'}
    for k in range(1,kim+1):
        url = 'https://browse.gmarket.co.kr/m/search?keyword={}&p={}'.format(keyword,k)

        try: 
            s = requests.Session()
            res = s.get(url,headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'lxml')
        except :
            try: 
                time.sleep(2)
                s = requests.Session()
                res = s.get(url,headers=headers)
                res.raise_for_status()
                soup = BeautifulSoup(res.text, 'lxml')
                print('에러, 2초 쉬었다가 함')   
            except :
                time.sleep(2)
                s = requests.Session()
                res = s.get(url,headers=headers)
                res.raise_for_status()
                soup = BeautifulSoup(res.text, 'lxml')
                print('에러, 마지막 기회')   



        lis = soup.find('div', attrs = { 'id' : 'section__inner-content-body-container'}).find_all('div', attrs = {'class' :'box__module-wrap'})


        stopper = False
        i = 0
        for lisss in lis :

            for li in lisss :
                link = li.find(attrs = {'class':'text__banner'})
                print(link)

                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text__title'}).get_text() 

                            alladd.append(k)       
                            allname.append(name)   

                            allNotul.append('먼저 둘러보세요')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()

            
                                if ship == '무료배송' :
                                    allship.append('무료배송')

                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 

                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송')


                        except :
                            pass

                else:
                    if link.get_text() == '먼저 둘러보세요' : 
                        name = li.find('span',attrs = {'class' : 'text__title'})
                        if name != None :
                            allname.append(name.get_text())


                            allNotul.append('먼저 둘러보세요')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()


                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송')


                        stopper = True 
                    else :
                        stopper = False








        


        stopper = False
        i = 0
        for lisss in lis :

            for li in lisss :
                link = li.find(attrs = {'class':'text__banner'})
                print(link)

                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text__title'}).get_text() 

                            alladd.append(k)       
                            allname.append(name)   

                            allNotul.append('이 상품은 어떠세요?')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()

            
                                if ship == '무료배송' :
                                    allship.append('무료배송')

                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 

                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)

                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송')
                        except :
                            pass

                else:
                    if link.get_text() == '이 상품은 어떠세요?' : 
                        name = li.find('span',attrs = {'class' : 'text__title'})
                        if name != None :
                            allname.append(name.get_text())


                            allNotul.append('이 상품은 어떠세요?')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()


                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송')
                        stopper = True 
                    else :
                        stopper = False


        stopper = False
        i = 0
        for lisss in lis :

            for li in lisss :
                link = li.find(attrs = {'class':'text__banner'})
                print(link)

                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text__title'}).get_text() 

                            alladd.append(k)       
                            allname.append(name)   

                            allNotul.append('오늘의 상품이에요')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()

            
                                if ship == '무료배송' :
                                    allship.append('무료배송')

                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 

                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송')

                        except :
                            pass

                else:
                    if link.get_text() == '오늘의 상품이에요' : 
                        name = li.find('span',attrs = {'class' : 'text__title'})
                        if name != None :
                            allname.append(name.get_text())


                            allNotul.append('오늘의 상품이에요')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()


                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송') 
                        stopper = True 
                    else :
                        stopper = False







        stopper = False
        i = 0
        for lisss in lis :

            for li in lisss :
                link = li.find(attrs = {'class':'text__banner'})
                print(link)

                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text__title'}).get_text() 

                            alladd.append(k)       
                            allname.append(name)   

                            allNotul.append('스마일배송')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()

            
                                if ship == '무료배송' :
                                    allship.append('무료배송')

                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 

                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송')

                        except :
                            pass

                else:
                    if link.get_text() == '오늘 주문! 내일 도착!' : 
                        name = li.find('span',attrs = {'class' : 'text__title'})
                        if name != None :
                            allname.append(name.get_text())


                            allNotul.append('스마일배송')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()


                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송') 
                        stopper = True 
                    else :
                        stopper = False




                
        stopper = False
        i = 0
        for lisss in lis :

            for li in lisss :
                link = li.find(attrs = {'class':'text__banner'})
                print(link)

                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text__title'}).get_text() 

                            alladd.append(k)       
                            allname.append(name)   

                            allNotul.append('주목할 만한 상품이에요')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()

            
                                if ship == '무료배송' :
                                    allship.append('무료배송')

                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 

                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송')

                        except :
                            pass

                else:
                    if link.get_text() == '주목할 만한 상품이에요' : 
                        name = li.find('span',attrs = {'class' : 'text__title'})
                        if name != None :
                            allname.append(name.get_text())


                            allNotul.append('주목할 만한 상품이에요')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()


                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송')                                
                        stopper = True 
                    else :
                        stopper = False





                    
 
    

        stopper = False
        i = 0
        for lisss in lis :

            for li in lisss :
                link = li.find(attrs = {'class':'text__banner'})
                print(link)

                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text__title'}).get_text() 

                            alladd.append(k)       
                            allname.append(name)   

                            allNotul.append('일반상품')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()

            
                                if ship == '무료배송' :
                                    allship.append('무료배송')

                                elif ship == '' :
                                    allship.append('스마트배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 

                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송')

                        except :
                            pass

                else:
                    if link.get_text() == '일반상품' : 
                        name = li.find('span',attrs = {'class' : 'text__title'})
                        if name != None :
                            allname.append(name.get_text())


                            allNotul.append('일반상품')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text__delivery'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()


                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text__brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'text__score'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.get_text()

                                    allreview.append(score+'점')
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                            if num == None :
                                allsell.append(None)
                            else :
                                num = num.get_text()
                                num = num.replace('구매 ', '').replace('건','')
                                allsell.append(num)
                            shipping = li.find('span', attrs = {'class': 'box__brand'})
                            if shipping  == None :
                                allshipplace.append('국내배송')                
                            else:
                                if shipping.find('span',attrs = {'class': 'text'}) == None :
                                    allshipplace.append('국내배송')
                                else :
                                    shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                                    allshipplace.append('해외배송')

                        stopper = True 

                    else :
                        stopper = False




        i = 0
        try :
            lis = soup.find('div', attrs = {'module-design-id' :'2011'}).find_all('li', attrs = {'class' :'list-item'})
            for li in lis :
                name = li.find('span',attrs = {'class' : 'text__title'}).get_text() 

                alladd.append(k)  
                allname.append(name)   
                allNotul.append('이것도 둘러보세요')
                i += 1 

                allrank.append(i)
                price = li.find('strong',attrs = {'class' : 'text__price-seller'}).get_text()
                allprice.append(price)
                
                ship = li.find('span',attrs = {'class' : 'text__delivery'})
                if ship == None :
                    allship.append('무료배송')
                else : 
                    ship = ship.get_text()
                    if ship == '무료배송' :
                        allship.append('무료배송')
                        
                    elif ship == '' :
                        allship.append('스마일배송')   

                    else :
                        ship = re.sub(r'[^0-9]', '', ship)
                        allship.append(ship)
                market = li.find('span',attrs = {'class': 'text__brand'})
                if market == None :
                    allmarket.append(None)
                else :
                    allmarket.append(market.get_text())
            
                try: 
                    score = li.find('span',attrs = {'class' : 'text__score'})

                    if score == None :
                        allreview.append(None)
                    else : 

                        score = score.get_text()

                        allreview.append(score+'점')
                except :
                    allreview.append(None)
                        
                
                num = li.find('span',attrs = {'class': 'box__score-buycnt'})
                if num == None :
                    allsell.append(None)
                else :
                    num = num.get_text()
                    num = num.replace('구매 ', '').replace('건','')
                    allsell.append(num)
                shipping = li.find('span', attrs = {'class': 'box__brand'})
                if shipping  == None :
                    allshipplace.append('국내배송')                
                else:
                    if shipping.find('span',attrs = {'class': 'text'}) == None :
                        allshipplace.append('국내배송')
                    else :
                        shipping.find('span',attrs = {'class': 'text'}).get_text() == "해외직구" 
                        allshipplace.append('해외배송')

        except:
            pass



    print(len(allname))
    print(len(allNotul))
    print(len(allrank))
    print(len(allprice))
    print(len(allship))
    print(len(allmarket))
    print(len(allreview))
    print(len(allsell))
    print(len(alladd),'')

    for i in range(before, len(allname)):
        allshopping.append('G마켓')

        allinternet.append('모바일')

def AuctionMobile(keyword, kim):
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'}

    basic2 = len(allname)
    for k in range(1,kim+1):
        url = 'http://browse.auction.co.kr/m/search?keyword={}&p={}'.format(keyword,k)
        try: 
            s = requests.Session()
            res = s.get(url,headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'lxml')
        except :
            try: 
                time.sleep(2)
                s = requests.Session()
                res = s.get(url,headers=headers)
                res.raise_for_status()
                soup = BeautifulSoup(res.text, 'lxml')
                print('에러, 2초 쉬었다가 함')   
            except :
                time.sleep(2)
                s = requests.Session()
                res = s.get(url,headers=headers)
                res.raise_for_status()
                soup = BeautifulSoup(res.text, 'lxml')
                print('에러, 마지막 기회')   



        lis = soup.find('div', attrs = { 'id' : 'section--inner_content_body_container'}).find_all('div', attrs = {'class' :'section--module_wrap'})

        i = 0
        stopper = False

        for lisss in lis :     
            print(lisss)

            for li in lisss :



                link = li.find('span', attrs= {'class' : 'section--banner_text'})

                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                            alladd.append(k)  

                            allname.append(name)   

                            allNotul.append('먼저 둘러보세요')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()
                                if ship == '무료배송' :
                                    allship.append('무료배송')
                                    
                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)


                            market = li.find('span',attrs = {'class': 'text--brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'score--awards'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.find('span').get_text()
                                    score = score.replace('후기평점 ', '')
                                    allreview.append(score)
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                            if num == None :
                                allsell.append(None)
                            else :
                                allsell.append(num.get_text())


                        except :
                            pass

                else:
                    if link.get_text() == '먼저 둘러보세요' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('먼저 둘러보세요')
                        i += 1 
                        alladd.append(k)  
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                    
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)


                        market = li.find('span',attrs = {'class': 'text--brand'})
                        if market == None :
                            allmarket.append(None)
                        else :
                            allmarket.append(market.get_text())
                    
                        try: 
                            score = li.find('span',attrs = {'class' : 'score--awards'})

                            if score == None :
                                allreview.append(None)
                            else : 
                                score = score.find('span').get_text()
                                score = score.replace('후기평점 ', '')
                                allreview.append(score)
                        except :
                            allreview.append(None)
                        
                        num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                        if num == None :
                            allsell.append(None)
                        else :
                            allsell.append(num.get_text())

                        stopper = True 
                    else :
                        stopper = False

        i = 0
        stopper = False
        for lisss in lis :     
            

            for li in lisss :



                link = li.find('span', attrs= {'class' : 'section--banner_text'})
                
                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                            alladd.append(k)  

                            allname.append(name)   

                            allNotul.append('이 상품은 어떠세요?')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()
                                if ship == '무료배송' :
                                    allship.append('무료배송')
                                    
                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)

                            market = li.find('span',attrs = {'class': 'text--brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'score--awards'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.find('span').get_text()
                                    score = score.replace('후기평점 ', '')
                                    allreview.append(score)
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                            if num == None :
                                allsell.append(None)
                            else :
                                allsell.append(num.get_text())


                        except :
                            pass

                else:
                    if link.get_text() == '이 상품은 어떠세요?' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('이 상품은 어떠세요?')
                        i += 1 
                        alladd.append(k)  
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text--brand'})
                        if market == None :
                            allmarket.append(None)
                        else :
                            allmarket.append(market.get_text())
                    
                        try: 
                            score = li.find('span',attrs = {'class' : 'score--awards'})

                            if score == None :
                                allreview.append(None)
                            else : 
                                score = score.find('span').get_text()
                                score = score.replace('후기평점 ', '')
                                allreview.append(score)
                        except :
                            allreview.append(None)
                        
                        num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                        if num == None :
                            allsell.append(None)
                        else :
                            allsell.append(num.get_text())

                        stopper = True 
                    else :
                        stopper = False

        i = 0
        stopper = False
        for lisss in lis :     
            

            for li in lisss :



                link = li.find('span', attrs= {'class' : 'section--banner_text'})
                
                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                            alladd.append(k)  

                            allname.append(name)   

                            allNotul.append('오늘의 상품이에요')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()


                                if ship == '무료배송' :
                                    allship.append('무료배송')
                                    
                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)
                            market = li.find('span',attrs = {'class': 'text--brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'score--awards'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.find('span').get_text()
                                    score = score.replace('후기평점 ', '')
                                    allreview.append(score)
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                            if num == None :
                                allsell.append(None)
                            else :
                                allsell.append(num.get_text())


                        except :
                            pass

                else:
                    if link.get_text() == '오늘의 상품이에요' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('오늘의 상품이에요')
                        i += 1 
                        alladd.append(k)  
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)

                        market = li.find('span',attrs = {'class': 'text--brand'})
                        if market == None :
                            allmarket.append(None)
                        else :
                            allmarket.append(market.get_text())
                    
                        try: 
                            score = li.find('span',attrs = {'class' : 'score--awards'})

                            if score == None :
                                allreview.append(None)
                            else : 
                                score = score.find('span').get_text()
                                score = score.replace('후기평점 ', '')
                                allreview.append(score)
                        except :
                            allreview.append(None)
                        
                        num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                        if num == None :
                            allsell.append(None)
                        else :
                            allsell.append(num.get_text())

                        stopper = True 
                    else :
                        stopper = False

        i = 0
        stopper = False
        for lisss in lis :     
            

            for li in lisss :



                link = li.find('span', attrs= {'class' : 'section--banner_text'})
                print(link)
                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                            alladd.append(k)  

                            allname.append(name)   

                            allNotul.append('스마일배송')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()
                                if ship == '무료배송' :
                                    allship.append('무료배송')
                                    
                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)

                            market = li.find('span',attrs = {'class': 'text--brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'score--awards'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.find('span').get_text()
                                    score = score.replace('후기평점 ', '')
                                    allreview.append(score)
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                            if num == None :
                                allsell.append(None)
                            else :
                                allsell.append(num.get_text())


                        except :
                            pass

                else:
                    if link.get_text() == '오늘 주문! 내일 도착!' or link.get_text() == '스마일배송 검색결과 더보기':
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        
                        allNotul.append('스마일배송')
                        i += 1 
                        alladd.append(k)  
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)

                        market = li.find('span',attrs = {'class': 'text--brand'})
                        if market == None :
                            allmarket.append(None)
                        else :
                            allmarket.append(market.get_text())
                    
                        try: 
                            score = li.find('span',attrs = {'class' : 'score--awards'})

                            if score == None :
                                allreview.append(None)
                            else : 
                                score = score.find('span').get_text()
                                score = score.replace('후기평점 ', '')
                                allreview.append(score)
                        except :
                            allreview.append(None)
                        
                        num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                        if num == None :
                            allsell.append(None)
                        else :
                            allsell.append(num.get_text())

                        stopper = True 
                    else :
                        stopper = False

        i = 0
        stopper = False
        for lisss in lis :     
            

            for li in lisss :



                link = li.find('span', attrs= {'class' : 'section--banner_text'})
                
                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 


                            allname.append(name)   
                            alladd.append(k)  
                            allNotul.append('주목할 만한 상품이에요')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()
                                if ship == '무료배송' :
                                    allship.append('무료배송')
                                    
                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)

                            market = li.find('span',attrs = {'class': 'text--brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'score--awards'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.find('span').get_text()
                                    score = score.replace('후기평점 ', '')
                                    allreview.append(score)
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                            if num == None :
                                allsell.append(None)
                            else :
                                allsell.append(num.get_text())


                        except :
                            pass

                else:
                    if link.get_text() == '주목할 만한 상품이에요' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('주목할 만한 상품이에요')
                        i += 1 
                        alladd.append(k)  
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)
                        market = li.find('span',attrs = {'class': 'text--brand'})
                        if market == None :
                            allmarket.append(None)
                        else :
                            allmarket.append(market.get_text())
                    
                        try: 
                            score = li.find('span',attrs = {'class' : 'score--awards'})

                            if score == None :
                                allreview.append(None)
                            else : 
                                score = score.find('span').get_text()
                                score = score.replace('후기평점 ', '')
                                allreview.append(score)
                        except :
                            allreview.append(None)
                        
                        num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                        if num == None :
                            allsell.append(None)
                        else :
                            allsell.append(num.get_text())

                        stopper = True 
                    else :
                        stopper = False

        i = 0
        stopper = False
        for lisss in lis :     
            

            for li in lisss :



                link = li.find('span', attrs= {'class' : 'section--banner_text'})
                
                if link == None :       
                    if stopper == True : 

                        try: 
                            name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 

                            alladd.append(k)  
                            allname.append(name)   

                            allNotul.append('일반상품')
                            i += 1 

                            allrank.append(i)
                            price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                            allprice.append(price)
                            
                            ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                            if ship == None :
                                allship.append('무료배송')
                            else : 
                                ship = ship.get_text()
                                if ship == '무료배송' :
                                    allship.append('무료배송')
                                    
                                elif ship == '' :
                                    allship.append('스마일배송')   

                                else :
                                    ship = re.sub(r'[^0-9]', '', ship)
                                    allship.append(ship)

                            market = li.find('span',attrs = {'class': 'text--brand'})
                            if market == None :
                                allmarket.append(None)
                            else :
                                allmarket.append(market.get_text())
                        
                            try: 
                                score = li.find('span',attrs = {'class' : 'score--awards'})

                                if score == None :
                                    allreview.append(None)
                                else : 
                                    score = score.find('span').get_text()
                                    score = score.replace('후기평점 ', '')
                                    allreview.append(score)
                            except :
                                allreview.append(None)
                            
                            num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                            if num == None :
                                allsell.append(None)
                            else :
                                allsell.append(num.get_text())


                        except :
                            pass

                else:
                    if link.get_text() == '일반등록' : 
                        name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 
                        allname.append(name)
                        allNotul.append('일반상품')
                        i += 1 
                        alladd.append(k)  
                        allrank.append(i)
                        price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                        allprice.append(price)
                        
                        ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                        if ship == None :
                            allship.append('무료배송')
                        else : 
                            ship = ship.get_text()
                            if ship == '무료배송' :
                                allship.append('무료배송')
                                
                            elif ship == '' :
                                allship.append('스마일배송')   

                            else :
                                ship = re.sub(r'[^0-9]', '', ship)
                                allship.append(ship)

                        market = li.find('span',attrs = {'class': 'text--brand'})
                        if market == None :
                            allmarket.append(None)
                        else :
                            allmarket.append(market.get_text())
                    
                        try: 
                            score = li.find('span',attrs = {'class' : 'score--awards'})

                            if score == None :
                                allreview.append(None)
                            else : 
                                score = score.find('span').get_text()
                                score = score.replace('후기평점 ', '')
                                allreview.append(score)
                        except :
                            allreview.append(None)
                        
                        num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                        if num == None :
                            allsell.append(None)
                        else :
                            allsell.append(num.get_text())

                        stopper = True 
                    else :
                        stopper = False

        i = 0
        try :
            lis = soup.find('div', attrs = {'module-design-id' :'2029'}).find_all('li', attrs = {'class' :'item'})
            for li in lis :
                name = li.find('span',attrs = {'class' : 'text--title'}).get_text() 


                allname.append(name)   
                allNotul.append('이것도 둘러보세요')
                i += 1 
                alladd.append(k)  
                allrank.append(i)
                price = li.find('strong',attrs = {'class' : 'text--price_seller'}).get_text()
                allprice.append(price)
                
                ship = li.find('span',attrs = {'class' : 'text--addinfo'})
                if ship == None :
                    allship.append('무료배송')
                else : 
                    ship = ship.get_text()
                    if ship == '무료배송' :
                        allship.append('무료배송')
                        
                    elif ship == '' :
                        allship.append('스마일배송')   

                    else :
                        ship = re.sub(r'[^0-9]', '', ship)
                        allship.append(ship)

                market = li.find('span',attrs = {'class': 'text--brand'})
                if market == None :
                    allmarket.append(None)
                else :
                    allmarket.append(market.get_text())
            
                try: 
                    score = li.find('span',attrs = {'class' : 'score--awards'})

                    if score == None :
                        allreview.append(None)
                    else : 
                        allreview.append(score.find('span').get_text())
                except :
                    allreview.append(None)
                
                num = li.find('span',attrs = {'class': 'text--buycnt__num'})
                if num == None :
                    allsell.append(None)
                else :
                    allsell.append(num.get_text())


        except:
            pass



    print(len(allname))
    print(len(allNotul))
    print(len(allrank))
    print(len(allprice))
    print(len(allship))
    print(len(allmarket))
    print(len(allreview))
    print(len(allsell))

    for i in range(basic2,len(allsell)):
        allshopping.append('옥션')
        allshipplace.append(None)
        allinternet.append('모바일')







def data(allinternet, allshopping, allNotul, allrank, alladd, allname, allprice, allship, allmarket, allsell, allreview, allshipplace):



    data = {
        '기기' : allinternet,
        '쇼핑몰' : allshopping,
        '노출영역' : allNotul,
        '페이지' : alladd,
        '순위' : allrank,
        '상품명' : allname,
        '판매가' : allprice,
        '배송비' : allship,
        '판매처': allmarket,
        '판매량': allsell,
        '리뷰': allreview,
        '배송지': allshipplace,
    }

    print(len(allinternet), len(allshopping), len(allNotul), len(allrank), len(allname), len(allprice), len(allship), len(allmarket), len(allsell), len(allreview), len(allshipplace))


    df0 = pd.DataFrame(data = data, columns = ['기기', '쇼핑몰', '노출영역','페이지','순위','상품명','판매가','배송비','판매처','판매량','리뷰','배송지'])
    df1 = None
    df2 = None 
    df3 = None 
    df4 = None 
    df5 = None 
    df6 = None 
    if C_Var1.get() == 1 :
        
        df1 = df0[df0['노출영역'] == '먼저 둘러보세요']
    
    if C_Var2.get() == 1 :
        
        df2 = df0[df0['노출영역'] == '오늘의 상품이에요']

    if C_Var3.get() == 1 :
        
        df3 = df0[df0['노출영역'] == '이 상품은 어떠세요?']

    if C_Var4.get() == 1 :
        
        df4 = df0[df0['노출영역'] == '스마일배송']

    if C_Var5.get() == 1 :
        
        df5 = df0[df0['노출영역'] == '주목할 만한 상품이에요']

    if C_Var6.get() == 1 :
        
        df6 = df0[df0['노출영역'] == '일반상품']
    global df
    df = None
    df = pd.concat([df1,df2,df3,df4,df5,df6], ignore_index=True)

    allinternet.clear()
    allshopping.clear()
    allshipplace.clear()
    allname.clear()
    allNotul.clear()
    allrank.clear()
    allprice.clear()
    allship.clear()
    allmarket.clear()
    allreview.clear()
    allsell.clear()
    alladd.clear()
    sheet = Sheet(root, data= df.values.tolist())
    sheet.headers(['기기', '쇼핑몰', '노출영역','페이지','순위','상품명','판매가','배송비','판매처','판매량','리뷰','배송지'])
    sheet.place(x = 20,
            y = 300,
            width=1000,
            height=400)

    sheet = None




def setting():
    print(C_Var1.get()) #먼저 둘러보세요
    print(C_Var2.get()) #오늘의 상품이에요
    print(C_Var3.get()) #이 상품은 어떠세요? 
    print(C_Var4.get()) #스마일 배송
    print(C_Var5.get()) #주목할 만한 상품이에요
    print(C_Var6.get()) #일반상품
    print(C_Var7.get())
    print(C_Var8.get())

    print(e.get())
    global keyword
    keyword = None
    keyword = e.get()

    print(e1.get())
    kim = int(e1.get())

    if C_Var7.get() == 1:
        GmarketMobile(keyword,kim)   
    print(C_Var7.get())
    if C_Var8.get() == 1 :
        AuctionMobile(keyword,kim)
    if C_Vargmarket.get() == 1 :
        Gmarket(keyword,kim)
    print(C_Var8.get())
    if C_Varauction.get() == 1 :
        Auction(keyword,kim)
    data(allinternet, allshopping, allNotul, allrank,alladd, allname, allprice, allship, allmarket, allsell, allreview, allshipplace)
    change()
def down():
    text1 = str(text)
    text1 = re.sub(r'[^0-9]', '', text1)
    df.to_excel('{} {}.xlsx'.format(keyword,text1))

#지마켓
    
def change():
    d = datetime.datetime.now()
    global text
    text = d.replace(microsecond = 0) 
    label100.config(text = text)






font= tkinter.font.Font(family="맑은 고딕", size=15)
label0 = Label(root, text = 'G마켓 옥션 데이터수집 프로그램',font = font)
label0.place(x=3, y=5)
label1 = Label(root, text = '키워드',font = font)
label1.place(x=50, y=80)


btn1 = Button(root, text ='데이터수집하기',font = font,command=setting)
btn1.pack()
btn1.place(x = 450,
        y = 85,
        width=200,
        height=40)

label2 = Label(root, text = '설정',font = font)
label2.place(x=50, y=130)
C_Vargmarket = IntVar()
chkbox10 = Checkbutton(root,text = 'G마켓 PC',variable =C_Vargmarket,font = font)
chkbox10.pack()
chkbox10.place(x = 600,
        y = 130)
chkbox10.select()



C_Varauction = IntVar()
chkbox10 = Checkbutton(root,text = '옥션 PC',variable =C_Varauction,font = font)
chkbox10.pack()
chkbox10.place(x = 800,
        y = 130)
chkbox10.select()

e = Entry(root)
e.place(x = 200,
        y = 85,
        width=200,
        height=40)
e.insert(0,'')



C_Var1 = IntVar()
chkbox1 = Checkbutton(root,text = '먼저 둘러보세요',variable = C_Var1,font = font)
chkbox1.pack()
chkbox1.place(x = 200,
        y = 180)
print(C_Var1.get())
chkbox1.select()


C_Var2 = IntVar()
chkbox2 = Checkbutton(root,text = '오늘의 상품이에요',variable = C_Var2,font = font)
chkbox2.pack()
chkbox2.place(x = 450,
        y = 180)
print(C_Var2.get())
chkbox2.select()


C_Var3 = IntVar()
chkbox3 = Checkbutton(root,text = '이 상품은 어떠세요?',variable = C_Var3,font = font)
chkbox3.pack()
chkbox3.place(x = 700,
        y = 180)
print(C_Var3.get())
chkbox3.select()


C_Var4 = IntVar()
chkbox4 = Checkbutton(root,text = '스마일 배송',variable = C_Var4,font = font)
chkbox4.pack()
chkbox4.place(x = 200,
        y = 210)
print(C_Var4.get())
chkbox4.select()


C_Var5 = IntVar()
chkbox5 = Checkbutton(root,text = '주목할 만한 상품이에요',variable = C_Var5,font = font)
chkbox5.pack()
chkbox5.place(x = 450,
        y = 210)
print(C_Var5.get())

chkbox5.select()

C_Var6 = IntVar()
chkbox6 = Checkbutton(root,text = '일반상품',variable = C_Var6,font = font)
chkbox6.pack()
chkbox6.place(x = 700,
        y = 210)

print(C_Var6.get())

chkbox6.select()

C_Var7 = IntVar()
chkbox7 = Checkbutton(root,text = 'G마켓 모바일',variable = C_Var7,font = font)
chkbox7.pack()
chkbox7.place(x = 200,
        y = 130)

print(C_Var7.get())

chkbox7.select()

C_Var8 = IntVar()
chkbox8 = Checkbutton(root,text = '옥션 모바일',variable = C_Var8,font = font)
chkbox8.pack()
chkbox8.place(x = 400,
        y = 130)

print(C_Var8.get())

chkbox8.select()


label3 = Label(root, text = '검색 페이지 수 :',font = font)
label3.place(x=50, y=250)
e1 = Entry(root)
e1.place(x = 210,
        y = 250,
        width=40,
        height=40)
e1.insert(0,'')

label4 = Label(root, text = '페이지 까지 조회',font = font)
label4.place(x=250, y=250)

btn2 = Button(root, text ='엑셀다운',font = font,command=down)
btn2.pack()
btn2.place(x = 800,
        y = 250,
        width=200,
        height=40)


label100 = Label(root, text = '시간', font = font)
label100.place(x=600, y=250)





root.mainloop()




