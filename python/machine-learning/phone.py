# 기존 프로그램
def get_price(최대금액, 액정파손, 번인, 찍힘, 생활기스, 배터리):
    적정금액 = 최대금액 # 하자 없을 시 금액 : 300000
    if 액정파손 == True:
        적정금액 -= 150000
    elif 번인 == True:
        적정금액 -= 50000

    if 찍힘 >= 3: # 3군데 이상
        적정금액 -= 30000
    elif 생활기스 == True:
        적정금액 -= 5000

    if  배터리 < 10: # 10시간 미만
        적정금액 -= 20000

    return 적정금액

    