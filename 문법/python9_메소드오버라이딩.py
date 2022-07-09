##메소드 오버라이딩 : 자식클래스에서 부모클래스의 함수 쓰고 싶을 떄 ??

#일반유닛
class unit: 
    def __init__(self,name,hp,speed): #생성자
        self.name=name
        self.hp=hp
        self.speed = speed
        
    def move(self,location):
        print("[지상유닛이동")
        print("{}가 {}방향으로 이동합니다.[속도 : {}]".format(self.name,location,self.speed))


#공격유닛
class attackUnit(unit):
    def __init__(self,name,hp,speed,damage):
        unit.__init__(self,name,hp,speed)
        self.damage=damage
        
    def attack(self,location):
        print("{0} : {1}방향으로 적군을 공격합니다.[공격력:{2}]".format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name,damage)) 
        self.hp-=damage
        print("{0} : 현재 남은 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 죽었습니다.".format(self.name))
            
#날 수 있는 기능을 가진 클래스
#드랍쉽 : 공중유닛, 수송기, 공격X
class flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self,name,location):
        print("{} : {} 방향으로 날아갑니다. [속도 {} ]".format(self.name,location,self.flying_speed))
        
        
#공중 공격 유닛
class flyableAttackUnit(attackUnit,flyable):
    def __init__(self, name, hp, damage, flying_speed): 
        attackUnit.__init__(self,name,hp, 0,damage) #지상스피드는 0
        flyable.__init__(self,flying_speed)
        

#벌쳐
vulture = attackUnit("벌쳐",80,10,20)

#배틀크류져
battleCruiser = flyableAttackUnit("배틀크루져",500,25,3)

vulture.move("11시")
battleCruiser.fly(battleCruiser.name,"9시")

#객체가 공중 유닛인지, 지상유닛인지 확인해서 move할 지 fly할 지 선택 해야하는데 귀찮다...
#메소드 오버라이딩의 등장으로 move로 통일할 수 있다?

