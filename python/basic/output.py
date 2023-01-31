print("Python", "Java")

print("Python" + "Java")

print("Python", "Java", sep=",") # 값들을 콤마(,) 로 구분

print("Python", "Java", "JavaScript", sep=" vs ") # 값들을 " vs " 로 구분


print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")


scores = {"수학":0, "영어":50, "코딩":100}
print(scores.items())
for subject, score in scores.items(): # key, value
    print(subject, score)

