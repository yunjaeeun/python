cabinet = {3:"유재석",100:"김태호"}

print(cabinet[3])       # dic[a] -> a 키값의 값 출력, 존재하지 않는 키값을 넣으면 오류 발생
print(cabinet.get(3))   # dic.get(a) -> a 키값의 값 출력, 존재하지 않는 키 값을 넣으면 None 출력

print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))   # dic.get(a, b) a라는 키값이 없으면 b 출력

print(3 in cabinet) # 3이라는 키값이 있는지 확인 -> True

cabinet["C-20"] = "조세호"        # C-20이라는 키 값에 조세호라는 값을 넣음(이미 키가 존재한다면 값을 업데이트)
cabinet[3] = "김종국"
print(cabinet)

del cabinet[3]        # 3번 키와 값을 제거
print(cabinet)

print(cabinet.keys())   # 키값만 출력
print(cabinet.values()) # 밸류만 출력
print(cabinet.items())    # 둘 다 출력

cabinet.clear()         # 비우기
print(cabinet)