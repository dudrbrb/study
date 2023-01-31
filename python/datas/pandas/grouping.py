import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)


# 그룹화
print(df.groupby('학교'))

# 그룹 선택
print(df.groupby('학교').get_group('북산고'))

# 계산 가능한 데이터들의 평균값
print(df.groupby('학교').mean())

# 그룹별 데이터 갯수
print(df.groupby('학교').size())

# 그룹 중 하나의 값만 불러오기
print(df.groupby('학교').size()['능남고'])


# 하나의 데이터 평균값 구하기
print(df.groupby('학교')['키'].mean())

# 일부 데이터 평귱값 구하기
print(df.groupby('학교')[['국어','영어','수학']].mean())



###### 학교별, 학년별로 그룹핑 ######
# 학년 column 추가
df['학년'] = [3,3,2,1,1,3,2,2]
# list 형태로 학교, 학년 넣어주면 된다.
print(df.groupby(['학교', '학년']).mean())


# 학년만 그룹핑
print(df.groupby('학년').mean())

# 키 순으로 정렬
print(df.groupby('학년').mean().sort_values('키'))

# 총 합 구하기
print(df.groupby(['학교', '학년']).sum())


# 갯수 세기
# SW특기가 있는 학생 수 세기
print(df.groupby('학교')['SW특기'].count())
print(df.groupby('학교')[['이름', 'SW특기']].count())

# 학교로 그룹핑 한 후 학년별 학생 수 세기
school = df.groupby('학교')
print(school['학년'].value_counts())


# 하나의 학교의 학년별 학생 수 세기
print(school['학년'].value_counts().loc['북산고'])

# 학년별 비율 구하기
print(school['학년'].value_counts(normalize=True).loc['북산고'])
