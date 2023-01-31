import pandas as pd
# import openpyxl

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

# dictionary를 data frame으로 변환
# df의 index를 1번~8번으로 변환
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])

# df의 index column에 이름 할당
df.index.name = '지원번호'

print(df)


###############################


# 저장하기 
# csv파일로 저장
df.to_csv('score.csv', encoding='utf-8-sig', index=False)

# excel 파일로 저장
df.to_excel('score.xlsx')

# txt 파일로 저장
# sep = 구분자
# \t = tab으로 구분된 덱스트 파일
df.to_csv('score.txt', sep='\t')


###############################


# 파일 열기 
# csv 파일 열기
df = pd.read_csv('score.csv')
print(df)

# txt 파일 열기
df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')
print(df)

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)


# # row 무시하기
# # 위에서부터 입력한 갯수만큼 row 무시
# df = pd.read_csv('score.csv', skiprows=1)
# print(df)

# # list에 해당하는 row 무시
# df = pd.read_csv('score.csv', skiprows=[1, 3, 5])
# print(df)


# 원하는 row만 출력
# df = pd.read_csv('score.csv', nrows=4)
# print(df)


# skiprows와 nrows 같이 사용하기
# df = pd.read_csv('score.csv', skiprows=2,  nrows=4)
# print(df)
