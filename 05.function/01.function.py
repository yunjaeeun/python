# # 함수 생성
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# 함수 호출
# open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다,".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(0, 1000)
balance = withdraw(balance,  500)
commission, balance = withdraw_night(balance, 400)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))