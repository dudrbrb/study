import tkinter.ttk as ttk
from tkinter import *
import tkinter.font

root = Tk()
root.title("약") #제목
root.geometry("1100x700")  #사이즈
root.resizable(False, False)   #사이즈 조절가능하게 하냐? no no

font= tkinter.font.Font(family="맑은 고딕", size=12)

checklist = ['두통', '편두통' , '치통' , '생리통' , '발열' , '오한 ', '기침' , '콧물 ','소화불량' , '복부팽만' , '배탈' , '급체' ]
medicine = {
    '타이레놀' : {
        '증상' : ['두통', '치통', '생리통', '편두통', '발열', '오한'],
        '성분' : '아세트아미노펜' 
    },
    '타이레놀 콜드 에스' : {
        '증상' : ['기침', '콧물', '오한'],
        '성분' : '아세트아미노펜' 
    },
    '이지엔6이브' : {
        '증상' : ['두통', '치통', '생리통', '편두통', '발열', '붓기'],
        '성분' : '이부프로펜' 
    },
    '베아제 정' : {
        '증상' : ['소화불량', '복부팽만', '과식'],
        '성분' : '판크레아틴' 
    },
    '훼스탈 플러스' : {
        '증상' : ['소화불량', '복부팽만', '과식'],
        '성분' : '판크레아틴' 
    },
    '아나프록스' : {
        '증상' : ['두통', '편두통', '소염제', '치통'],
        '성분' : '나프록센' 
    },
    '에어탑' : {
        '증상' : ['진통제', '편두통', '소염제', '치통'],
        '성분' : '아세클로페낙' 
    },
    '부스코판' : {
        '증상' : ['장염', '위염', '배탈'],
        '성분' : '부틸스코폴라민브롬화물' 
    },
    '포타겔' : {
        '증상' : ['장염', '위염', '배탈'],
        '성분' : '디옥타헤드랄스멕타이트' 
    },
}



allname = []
for i in range(len(checklist)) :
    name = 'Variation' + str(i)
    
    name  = IntVar()
    allname.append(name)
    boxname = 'chkbox' + str(i)
    boxname = Checkbutton(root,text = checklist[i],variable = name,font = font)
    boxname.pack()
    boxname.place(x = i*150 + 130,
            y = 180)
    if i > 5 :
        boxname.place(x = (i-6)*150 + 130,
            y = 230)


def setting():


    listissue = []
    global text
    text = ''
    for i in range(len(checklist)):
        if allname[i].get() == 1 :
            listissue.append(checklist[i])
    print(listissue)
    
    for now in listissue :

        for mediName, datas in medicine.items(): # key, value
            status = datas['증상'] 
            if now in status:
                text = text +  mediName + ', ' 
    
    text = text[:-2]
    label2.config(text = text)

    
    


btn1 = Button(root, text ='데이터수집하기',font = font,command=setting)
btn1.pack()
btn1.place(x = 450,
        y = 85,
        width=200,
        height=40)


label2 = Label(root, text = '결과',font = font)
label2.place(x=130, y=300)


root.mainloop()