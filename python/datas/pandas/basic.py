import pandas as pd


# Series
# 1차원의 데이터 (정수, 실수, 문자열 등)
# index 자동 생성
temp = pd.Series([-20, -10, 10, 20])
print(temp)

print(temp[0]) # 0번째 데이터 출력 : -20
print(temp[1]) # 1번째 데이터 출력 : -10
print(temp[2]) # 2번째 데이터 출력 : 10
print(temp[3]) # 3번째 데이터 출력 : 20


# Series 객체 생성 (index 지정)
temp = pd.Series([-20, -10, 10, 20], index=['Jan', 'Fed', 'Mar', 'Apr'])
print(temp)

print(temp['Jan']) # index가 'Jan'인 데이터 출력 : -20
print(temp['Fed']) # index가 'Fed'인 데이터 출력 : -10
print(temp['Mar']) # index가 'Mar'인 데이터 출력 : 10
print(temp['Apr']) # index가 'Apr'인 데이터 출력 : 20

# print(temp['jun']) # 해당하는 index명이 없을 때 에러



######################3

# Data Frame
# 2차원 데이터 (Series 모음)
# 사전(dictionary)형태

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data)
print(df)

# Data Frame의 데이터 접근
print(df['이름'])
print(df['키'])

# 2개 이상의 데이터 접근 (대괄호 안에 list 넣어줌)
print(df[['이름', '키']])


# Data Frame Column 지정
df = pd.DataFrame(data, columns=['이름', '학교', '키'])
print(df)

df = pd.DataFrame(data, columns=['학교', '이름', '키'])
print(df)



############## index ##############

# Data Frame에 index 지정
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
print(df.index)


# index에 column 이름 생성
df.index.name = '지원번호'
print(df)


# index 새로 추가
df.reset_index()

# index로 사용하던 '지원하기' 칼럼 삭제(drop) 및 실제 데이터에 바로 반영(inplace)
df.reset_index(drop=True, inplace=True)
print(df)


# 기존의 column중 하나를 index로 사용하기
df.set_index('이름', inplace=True)
print(df)


# index 정렬
# 오름차순
df.sort_index(inplace=True)
print(df)

# 내림차순
df.sort_index(ascending=False, inplace=True)
print(df)