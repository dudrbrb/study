import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')




##################### column 선택
# 하나만 선택
print(df['이름'])
print(df['키'])


# 여러개 선택
print(df[['이름','키', '학교']])


# 정수 index로 불러오기
# 원하는 column의 index확인
print(df.columns)

# 원하는 column의 index가 맞는지 확인
print(df.columns[0])

# 원하는 column의 정보 출력
print(df[df.columns[0]])

#맨 마지막 column 불러오기
print(df[df.columns[-1]])



######################## 슬라이싱
# 문자열 자르던 [n:n] 문법으로 데이터 슬라이싱 가능
print(df['영어'][0:5])
print(df[3:])



######################## 데이터 선택 (loc)
# row data 불러오기
print(df.loc['1번'])

# row에서 원하는 데이터 선택
print(df.loc['1번', '국어'])

# 여러개의 row에서 col값 선택
print(df.loc[['1번', '2번'], '영어'])

# 여러개의 row에서 여러개의 col값 선택
print(df.loc[['1번', '2번'], ['영어', '수학']])

# row와 col을 범위로 지정하기
print(df.loc['1번':'5번', '국어':'사회'])




######################## 데이터 선택 (iloc)
# 0번째 row 데이터 불러오기
print(df.iloc[0])

# 슬라이싱 가능
print(df.iloc[0:5])

# row에서 원하는 데이터 선택
print(df.iloc[0, 1])

# 여러개의 row에서 col값 선택
print(df.iloc[[0, 1], 4])

# 여러개의 row에서 여러개의 col값 선택
print(df.iloc[[0, 1], [4, 5]])

# row와 col을 범위로 지정하기
print(df.iloc[:3, 4:8])




######################## 데이터 선택 (조건)
# 조건에 해당하는 데이터 선택

print(df['키'] >= 185) # 학생들의 키다 185 이상인지 여부를 True / False로 출력

# filter 만들어서 적용하기
filt = (df['키'] >= 185 )
print(df[filt])

# filter를 역으로 적용하기
print(df[~filt])

# 필터링한 row의 col 출력
print(df.loc[filt, '수학'])
print(df.loc[filt, ['이름', '수학', '과학']])



### 다양한 조건
# & 그리고
# 학교는 북산고 + 키 185 이상
filt = ( df['키'] >= 185) & (df['학교'] == '북산고')
print(df.loc[filt])


# | 또는
# 키가 170 미만이거나 200 보다 큰 데이터
filt = ( df['키'] < 170) | (df['키'] > 200)
print(df.loc[filt])



### str 함수
# 시작하는 글자로 조건
filt = df['이름'].str.startswith('송')
print(df[filt])

# 글자 포함 여부로 조건
filt = df['이름'].str.contains('태')
print(df[filt])

# 글자 포함 여부로 조건
print(df[~filt])


# 단어 포함 여부
# 대소문자 구분을 없애기 위해 소문자로 통일
langs = ['python', 'java']
filt = df['SW특기'].str.lower().isin(langs)
print(df[filt])

# contains는 NaN이 그대로 출력됨
# na = True로 NaN데이터에 대해서 False로 인지
filt = df['SW특기'].str.contains('Java', na=False)
print(df[filt])
