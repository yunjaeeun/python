# 비교 연산자
print(10 > 3)       # True
print(4 >= 7)       # False
print(10 < 3)       # False
print(5 <= 5)       # True

print("----------------------------")
print(3 == 3)       # 앞과 뒤의 값이 같은지 True
print(4 == 2)       # False
print(3 + 4 == 7)   # True
print("7" == 7)     # False

print("----------------------------")
print(5 != 3)       # 앞과 뒤의 값이 같지 않은지 True
print(not( 1 != 3)) # False

print("----------------------------")
print(5 > 4 > 3)    # 5는 4보다 크고 4는 3보다 크다 True
print(5 > 4 > 7)    # 5는 4보다 크고 4는 7보다 크다 False