# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# 표준체중: 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자: 키(m) * 키(m) * 22
# 여자: 키(m) * 키(m) * 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
            # 함수명 : std_weight
        # 전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째 자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.36kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        weight = round((height * 0.01) * (height * 0.01) * 22, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, weight))
    elif gender == "여자":
        weight = (height * 0.01) * (height * 0.01) * 21
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, weight))
    else:
        print("외계인이세요?")

std_weight(175, "남자")