class BigNumberError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

try:   
    print("한자리 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("출력하고 싶은 메세지")
    print("{0} / {1} = {2}".format(num1, num2, num1 / num2))
except ValueError:
    print("숫자만 입력하세요!")
except BigNumberError as err:
    print("에러가 발생했습니다 한 자리 숫자만 입력하세요")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다")  # finally는 무조건 실행되는 구문