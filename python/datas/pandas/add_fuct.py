import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)


# 데이터에 함수 적용하기
def add_cm(height):
    return str(height)+'cm'

df['키'] = df['키'].apply(add_cm)
print(df)


# SW특기의 맨 앞글자를 대문자로 변경하는 함수
def capitalize(lang):
    if pd.notnull(lang): # pandas 내장함수
        return lang.capitalize() # 내장함수

    return lang 

df['SW특기'] = df['SW특기'].apply(capitalize)
print(df)