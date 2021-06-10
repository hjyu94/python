from random import *

print(random()) # 0.0 이상 1.0 미만의 값 생성
print(random() * 10) # 0.0 이상 10.0 미만의 값 생성
print(int(random() * 10)) # 0 이상 10 미만의 정수
print(int(random() * 10) + 1) # 1 이상 11 미만의 정수

print(randrange(1, 46)) # 1 ~ 46 미만의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 값 생성