gun = 10

def checkpoint_global(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 을 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint_global(2)
print("남은 총: {0}".format(gun))