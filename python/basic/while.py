# # 5번 부른 후 폐기하는 카페
# customer = "홍길동" # 손님
# index = 5 # 부르는 횟수, 총 5회

# while index >= 1: # 부르는 횟수가 1 이상인 경우에만 반복 실행
#     print("{0}님, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))    
#     index -= 1 # 부르는 횟수 감소
#     if index == 0: # 5번 모두 불렀다면 while문 탈출
#         print("커피는 폐기처분되었습니다.")


# # 손님이 올 때 까지 부르는 카페
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}님, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1



# 이름을 입력받고 일치하면 커피 주는 카페
customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}님, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")