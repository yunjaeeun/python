class Unit:
    def __init__(self, name, hp, speed):       
        self.name = name                        
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
              .format(self.name, location, self.speed))

# Unit 클래스를 상속
class AttackUnit(Unit):
        def __init__(self, name, hp, speed,damage):       
            Unit.__init__(self, name, hp, speed)
            self.damage = damage

        def attack(self, location):
            print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
                  .format(self.name, location, self.damage))
            
        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스(다중상속)
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

# 재정의 하지 않으면 지상유닛의 move()가 작동
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("별쳐", 80, 10, 20)

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")