class Unit:
    def __init__(self, name, hp, damage):       # __init__ -> 생성자
        self.name = name                        # self.name -> 멤버 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.hp))  # 멤버 변수를 외부에서도 사용 가능.

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True             # 외부에서 변수를 추가로 할당 가능.

if wraith2.clocking == True:
    print("{0} is cloaking.".format(wraith2.name))