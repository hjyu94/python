gun = 10

def checkpoint_local(soldiers): # 경계근무
    gun = gun - soldiers
    # UnboundLocalError: local variable 'gun' referenced before assignment
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint_local(2)
print("남은 총: {0}".format(gun))
