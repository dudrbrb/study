# 랜덤함수
from random import *
print(int(random() * 45) + 1) 

####################################################

# 문자열과 인덱스
text1 = '가나다라마바사'
print(text1[1]) # 나
print(text1[3:6]) # 라마바
print(text1[4:]) # 마바사
print(text1[:4]) # 가나다라
print(text1[-2:]) # 바사



# 문자열 포맷
# 포맷 버전1
text2 = '피카츄는 {}, {}, {}이가 있습니다.'.format('그린','노랭','뉴랭')
print(text2)

# 포맷 버전2
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 포맷 버전3
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") 



#####################################################



# 리스트 (=배열)
list = ['사과', '바나나', '키위', '블루베리']

# 리스트에소 요소 인덱스 도출
print(list.index("키위")) # 2

# 리스트 맨 뒤에 추가
list.append("오렌지")
print(list)

# 리스트 중간에 추가 
list.insert(1, "감")
print(list)

# 리스트 맨 뒤의 것 제거
list.pop()
print(list) # 오렌지 삭제됨

# 중복 값 세기
list2 = ['사과', '바나나', '사과', '바나나', '사과']
print(list2.count('사과')) # 2

# 리스트 정렬
num_list = [5, 2, 4, 3, 1]
print('원래 배열 : ', num_list)

num_list.sort() # 오름차순으로 정렬
print('오름차순 정렬 : ', num_list) # [1, 2, 3, 4, 5]

num_list.reverse() # 순서 뒤집기
print('거꾸로 정렬 : ', num_list) # [5, 4, 3, 2, 1]

# 리스트 확장
num_list.extend(list) # num_list와 list 합치기
print('합치기 : ', num_list) 


# 리스트 모두 지우기
num_list.clear()
print('전체삭제 : ', num_list) # []



#########################################################33


# 사전 
example = {'name': '홍길동', age : '20'}
print(example['name']) 
print(example.get('name')) 



















