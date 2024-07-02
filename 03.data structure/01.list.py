subway = [10, 20, 30]

print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇번째 위치에 있는지
print(subway.index("조세호"))

subway.append("하하")       # arr.append() -> 추가
print(subway)

# 정형돈을 유재석과 조세호 사이에 추가
subway.insert(1, "정형돈")  # arr.insert(a,b) -> a 위치에 b 추가
print(subway)

# 한명씩 뒤에서 제거 -> arr.pop()
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬 -> arr.sort()
num_list = [5,2,1,3,6]
num_list.sort()
print(num_list)

# 뒤집기(역정렬 아님) -> arr.reverse()
num_list.reverse()
print(num_list)

# 모두 비우기 -> arr.clear()
num_list.clear()
print(num_list)

# 다양한 자료형 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장 -> arr1.extent(arr2)
num_list.extend(mix_list)
print(num_list)