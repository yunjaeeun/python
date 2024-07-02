jumin = "990120-1234567"

print("성별: " + jumin[7])          # 변수명[a] -> a번째 출력
print("연도: "+ jumin[0:2])         # 변수명[a:b] -> a번째부터 b번째 직전까지
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])
print("생년월일: " + jumin[:6])     # 변수명[:a] -> 처음부터 a번째 직전까지
print("뒤 7자리: " + jumin[7:])     # 변수명[a:] -> a번째부터 마지막까지
print("뒤 7자리 (뒤부터): " + jumin[-7:])   # 맨 뒤 7번째부터 끝까지