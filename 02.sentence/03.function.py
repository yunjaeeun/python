python = "Python is Amazing"
print(python.lower())       # str.lower() -> 소문자로 출력
print(python.upper())       # str.upper() -> 대문자로 출력
print(python[0].isupper())  # str[a].isupper() -> a번째 인덱스가 대문자인지
print(len(python))          # len(str) -> str의 길이
print(python.replace("Python", "Java")) # str.replace("a", "b") -> a를 b로 바꿈

index = python.index("n")   # str.index("a") -> a가 나오는 위치(없는 문자열이면 오류 발생)
print(index)
index = python.index("n", index + 1) # 두번째 n이 나오는 위치
print(index)

print(python.find("n"))     # str.find("a") -> a의 위치(없는 문자열이면 -1 반환)

print(python.count("n"))    # str.count("a") ->  a가 몇번 나왔는지