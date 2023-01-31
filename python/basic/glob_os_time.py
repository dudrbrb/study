import module.byme as byme
byme.sign()

# glob모듈
import glob
print(glob.glob("*.py")) # 확장자가 py 인 모든 파일


# os모듈

import os
print(os.getcwd()) # 현재 디렉토리

# 폴더 새로 만들기 + 동일 폴더명이 있을 시 삭제하기
folder = "sample_dir" # 새로 만들 폴더 이름

if os.path.exists(folder): # 같은 이름의 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")

    os.rmdir(folder) # 폴더 삭제
    print(folder, "폴더를 삭제하였습니다.") # 삭제 문구 출력
else: # 같은 이름의 폴더가 존재하지 않으면
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")



print(os.listdir())




# time 모듈

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초


# datetime

import datetime
print("오늘 날짜는", datetime.date.today())


today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후