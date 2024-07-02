print(abs(-5))      # 절대값 abs()
print(pow(4, 2))    # 제곱 pow(a, b) = a^b
print(max(5, 12))   # 최댓값 max(a, b)
print(min(5, 12))   # 최소값 min(a, b)
print(round(4.56))  # 반올림

from math import *
print(floor(4.99))  # 내림
print(ceil(4.12))   # 올림
print(sqrt(16))     # 제곱근

# 랜덤함수
from random import *
print(random())         # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)    # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 45))  # 1 ~ 45 미만의 임의의 값 생성   
print(randint(1, 45))    # 1 ~ 45 이하의 임의의 값 생성