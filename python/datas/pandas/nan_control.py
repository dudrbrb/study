import pandas as pd
import numpy as np

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# # data frame의 모든 NaN값 채우기
# print(df.fillna('없음'))

# # '학교'를 의도적으로 NaN으로 만들기
# df['학교'] = np.nan
# print(df)


# # data frame의 모든 NaN값 채우기
# df.fillna('모름', inplace=True)
# print(df)


# # 일부 col의 NaN 채우기
# df['SW특기'].fillna('확인중', inplace=True)
# print(df)


# 데이터가 빈 값이 있는 row 삭제
# df.dropna(inplace=True)
# print(df)

# df.dropna(axis='index', how='any', inplace=True)
# print(df)

df.dropna(axis='columns', how='any', inplace=True)
print(df)

df['학교']= np.nan
df.dropna(axis='columns', how='all', inplace=True)

print(df)





















