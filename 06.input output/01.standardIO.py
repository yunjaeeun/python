print("Python", "Java")
print("Python", "Java", sep=",", end="?")    # sep -> 구분자 설정, end -> 마지막에 글자 추가
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)    # stdout -> 표준 출력
print("Python", "Java", file=sys.stderr)    # stderr -> 표준 오류

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(3), str(score).rjust(4), sep=":")          # ljust(a) -> a칸의 공간을 확보하고 왼쪽으로 정렬


for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))    #zfill(a) -> a칸만큼 빈공간을 채움


answer = input("아무 값이나 입력하세요 : ")
print(answer)