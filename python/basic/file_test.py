# 파일 새로 만들고 내용 추가하기
# score_file = open("score.txt", "w", encoding="utf8") # score.txt 파일을 쓰기("w") 모드로 열기
# print("수학 : 0", file=score_file) # score.txt 파일에 내용 쓰기
# print("영어 : 50", file=score_file) # score.txt 파일에 내용 쓰기
# score_file.close() # score.txt 파일 닫기




# 기존 파일의 마지막줄 뒤에 내용 더 추가하기
# score_file = open("score.txt", "a", encoding="utf8") # score.txt 파일을 쓰기("a") 모드로 열기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # write 는 줄바꿈 안해주기 때문에 탈출문자(\n)로 줄바꿈 추가
# score_file.close()


# 터미널로 파일 출력
# score_file = open("score.txt", "r", encoding="utf8") # score.txt 파일을 읽기("r") 모드로 열기
# print(score_file.read()) # 파일 전체 읽어오기
# score_file.close()



# 터미널로 파일 출력 + 한줄씩 출력
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 줄바꿈 중복을 방지하기 위해 end="" 처리
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()



# 모든 줄을 list에 저장한 후 for문으로 출력
score_file = open("score.txt", "r", encoding="utf8")

lines = score_file.readlines() # 모든 줄을 읽어와서 list 형태로 저장
for line in lines:
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
    
score_file.close()

