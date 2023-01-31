from random import *
 
users = list(range(1, 21)) # range 를 list 로 바로 감싸면 한 줄 더 줄일 수 있어요!
shuffle(users) # 리스트 내에서 순서 섞기

chicken_winner = sample(users, 1) # 치킨 당첨자 1명 추첨
remain_users = set(users) - set(chicken_winner) # 전체 집합에서 치킨 당첨자 집합을 제외
coffee_winners = sample(remain_users, 3) # 남은 19명 중에서 3명 추첨

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(chicken_winner))
print("커피 당첨자 : {0}".format(coffee_winners))
print("-- 축하합니다 --")
