# 배열 반복문
num_list = [0, 1, 2, 3, 4]
for n in num_list:
    print("LIST 번호 : {0}".format(n)) # {0} 위치에는 waiting_no 의 값이 들어가요

# 세트 반복문
num_set = {0, 1, 2, 3, 4}
for n in num_list:
    print("SET 번호 : {0}".format(n)) # {0} 위치에는 waiting_no 의 값이 들어가요


# range 반복문
for n in range(1, 101): # 1부터 101직전까지 (1~100)
    print("대기번호 : {0}".format(n))



#continue
absent = [2, 5] # 결석한 학생 출석번호
for student in range(1, 11): # 출석번호 1~10번
    if student in absent: # 결석했으면 책을 읽지 않고 다음 학생으로 넘어가기
        continue
    print("{0}, 책을 읽어봐".format(student))

