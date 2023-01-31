import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)


### column 수정 ###
# 학교명 바꾸기
print(df['학교'].replace({'북산고' : '상북고'}))

# 2개 이상 바꾸기
print(df['학교'].replace({'북산고' : '상북고', '능남고' : '바뀐고'}))

# 모든 데이터 바꾸기
# SW특기 모두 소문자로 바꾸기
df['SW특기'] = df['SW특기'].str.lower()
print(df)


# 모든 col 데이터에 글자 추가
df['학교'] = df['학교'] + '등학교'
print(df)






### column 추가 ###
df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['사회'] + df['과학']
print(df)

# 총합이 400점 이상인 학생은 합격, 400점 미만인 학생은 불합격
df['결과'] = '불합격'
df.loc[df['총합'] >= 400, '결과'] = '합격'
print(df)





### column 삭제 ###
df.drop(columns=['총합'])
df.drop(columns=['과학', '사회'])


### row 삭제 ###
df.drop(index=['4번'])


### 조건에 맞게 삭제 ###
filt = df['수학'] < 80
target = df[filt].index

df.drop(index=target)
print(df.drop(index=target))



### row 추가 ###
df.loc['9번'] = ['이정환', '해남고등학교', 184, 90, 90, 90, 90, 90, 'Kotlin', 450, '합격']


### Cell 수정 ###
# 하나만 수정
df.loc['4번', 'SW특기'] = 'Python'

# 2개 이상 수정
df.loc['5번', ['학교','SW특기']] = ['능남고등학교', 'C']


### Column 순서 변경 ###
cols = list(df.columns)
print(cols)

# 제일 마지막의 데이터를 맨 앞으로 바꾸기
# cols[-1] : 맨 뒤의 col 선택
# cols[0: -1] : 맨 앞부터 마지막 하나 전까지 col 선택

# 합치기
df = df[[cols[-1] + cols[0: -1]]]


# column 이름 변경
# list로 할당해주면 됨
# df.columns = ['Name', 'School', 'Height', ...]








