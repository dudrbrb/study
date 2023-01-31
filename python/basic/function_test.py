result = 0


def std_weight(gender, height):
    height = height*0.01 # cm에서 m로 변환

    if gender == '남': # 남자 식
        result = height*height*22 
        result = round(result,2) # 소수점 둘째자리까지 반올림
        return print(result)
    else : # 여자 식
        result = height*height*21
        result = round(result,2) # 소수점 둘째자리까지 반올림
        return print(result)


std_weight('남', 175)