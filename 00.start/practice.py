# 숫자형
print(5)
print(-10)
print(3.14)
print(100000000000)
print(5 + 3)
print(2 * 3)
print(3 * (3 + 1))

# 문자형
print('풍선')
print("나비")
print("ㅋ" * 9)

# 참 / 거짓
print(5 > 10)
print(10 > 5)
print(True)
print(False)
print(not True)
print(not (5 > 10))

# 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal  + "의 이름은 " + name +"에요")
hobby = "공놀이"                                                               # 변수를 다시 선언하면 아랫꺼가 적용
print(name + "는 " + str(age) +"살이며, " + hobby + "을 아주 좋아해요")         # 정수형을 출력할때는 str()로 감싸준다.
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")                  # , 를 활용해서 출력 가능하고 사용 시 str() 제거 가능
print(name +"는 어른일까요? " + str(is_adult))                                 # boolean형도 출력할 때 str()로 감싸준다.

