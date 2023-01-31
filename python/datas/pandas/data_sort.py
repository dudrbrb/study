import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')


# 오름차순으로 정렬
print(df.sort_values('키'))

# 내림차순으로 정렬
print(df.sort_values('키', ascending=False))

# 수학 점수로 정렬한 후 동점자가 있으면 영어 점수로 정렬
print(df.sort_values(['수학', '영어'], ascending=False))

# 수학 점수는 내림차순, 영어점수는 오름차순으로 정렬
print(df.sort_values(['수학', '영어'], ascending=[False, True]))


# 하나의 col을 가지고 정렬하기
# 오름차순
print(df['키'].sort_values())
# 내림차순
print(df['키'].sort_values(ascending=False))


# index로 정렬하기
# 오름차순
print(df.sort_index())
# 내림차순
print(df.sort_index(ascending=False))




