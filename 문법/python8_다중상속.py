#다중상속

#일반유닛
class unit: 
    def __init__(self,name,hp): #생성자
        self.name=name
        self.hp=hp

#공격유닛
class attackUnit(unit):
    def __init__(self,name,hp,damage):
        unit.__init__(self,name,hp)
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
    def __init__(self, name, hp, damage,flying_speed):
        attackUnit.__init__(self,name,hp,damage)
        flyable.__init__(self,flying_speed)
        
#발키리 : 공중 공격 유닛
valkyrie = flyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"1시")





##메소드 오버라이딩 : 자식클래스에서 부모클래스의 함수 쓰고 싶을 떄 ??

        