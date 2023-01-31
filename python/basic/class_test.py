class TEST:
    def __init__(self): 
        # class 호출 시 시작 함수 (__init__(self)는 고정)
        print('TEST 클래스 선언')
    
    def later(self):
        print('later 함수')

# class를 변수에 저장
CallTEST = TEST()

# class 호출. init함수 자동 실행
CallTEST

# class 내의 later함수 호출
CallTEST.later()







# 자기소개 클래스
class JSS:
    def __init__(self):
        print('자기소개서 class 실행')
        self.name = input('이름 : ')
        self.age = input('나이 : ')
    
    def result(self):
        print('내 이름은 {name}입니다. 나이는 {age}세 입니다.'.format(name = self.name, age = self.age))

CallJSS = JSS()

CallJSS
CallJSS.result()


# class JSS2(JSS):
#     def __init__(self):
#         print('JSS 클래스의 init함수는 사라지고, JSS2의 init 함수가 실행됨')

# class JSS2(JSS):
#     pass # JSS의 내용 그대로 진행할 때

class JSS2(JSS):
    def __init__(self):
       super().__init__() # super() = 괄호안의 class를 불러오는 것
       self.gender = input('성별 : ')

CallJSS2 = JSS2()

CallJSS2