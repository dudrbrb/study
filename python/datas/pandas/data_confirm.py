import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')




### data frame 확인
print(df.describe())

# column 별 정보
print(df.info())

# 처음 5개의 row를 가져옴
print(df.head())
# 처음 7개의 row를 가져옴
print(df.head(7))

# 마지막 5개의 row를 가져옴
print(df.tail())
# 마지막 7개의 row를 가져옴
print(df.tail(7))

# list 형태로 출력
print(df.values)

# index 정보 불러오기
print(df.index)

# columns 확인
print(df.columns)

# row, column 갯수 확인
print(df.shape)



#####################################


### series 확인
# series 정보
print (df['키'].describe())


# series 중 max에 해당하는 cell
print (df['키'].max())
# series 중 min에 해당하는 cell
print (df['키'].min())


# 값이 제일 큰 n개의 데이터 출력
print(df['키'].nlargest(3))

# 평균 값
print(df['키'].mean())

# 값을 모두 더한 값
print(df['키'].sum())

# 존재하는 데이터의 갯수 확인
print(df['SW특기'].count())

# 중복되는 값을 제외한 데이터 확인
print(df['학교'].unique())
# 중복되는 값을 제외한 데이터의 갯수 확인
print(df['학교'].nunique())





#####################################