#일반유닛
class unit: 
    def __init__(self,name,hp,speed): #생성자
        self.name=name
        self.hp=hp
        self.speed = speed
        print("{}유닛이 생성되었습니다.".format(self.name))
        
    def move(self,location):
        print("[지상유닛이동")
        print("{}가 {}방향으로 이동합니다.[속도 : {}]".format(self.name,location,self.speed))

    def damaged(self,damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name,damage)) 
        self.hp-=damage
        print("{0} : 현재 남은 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 죽었습니다.".format(self.name))


#공격유닛
class attackUnit(unit):
    def __init__(self,name,hp,speed,damage):
        unit.__init__(self,name,hp,speed)
        self.damage=damage
        
    def attack(self,location):
        print("{0} : {1}방향으로 적군을 공격합니다.[공격력:{2}]".format(self.name,location,self.damage))


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
        
    ##추가된 부분 : 재정의 #######################
    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)
        ##추가된 부분 : 재정의 #######################
        

class marine(attackUnit):
    def __init__(self):
        attackUnit.__init__(self,"마린",40,1,5)
        
    #스팀팩 : 일정 시간동안 공격속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{}가 스팀팩을 사용합니다.".format(self.name))
        else:
             print("{}가 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class tank(attackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격가능, 이동불가
    seize_developed = False #시즈모드 개발여부
    
    def __init__(self):
        attackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False
        
    def set_seize_mode(self):
        if tank.seize_developed == False:
            return
        
        #현재 시즈 모드가 아닐때 -> 시즈모드
        if tank.set_seize_mode == False:
            print("{}가 현재 시즈모드가 아닙니다.".format(self.name))
            self.damage *=2
            self.seize_mode = True
        #현재 시즈모드 일때 - > 시즈모드 해지
        else:
            print("{}가 현재 시즈모드입니다.".format(self.name))
            self.damage /=2
            self.seize_mode = False


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
        attackUnit.__init__(self,name,hp,0,damage)
        flyable.__init__(self,flying_speed)
        
        
            
class wraith(flyableAttackUnit):
    def __init__(self):
        flyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked = False #클로킹모드(해제 상태)
    def clocking(self):
        if self.clocked == True:
            print("{} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True
            

def game_start():
    print("게임 시작합니다.")
    
def game_over():
    print("player : gg")
    
    
#게임 진행
game_start()

m1 = marine()
m2=marine()
m3=marine()

t1=tank()
t2=tank()

w1 = wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units :
    unit.move("1시")
    
tank.seize_developed = True
print("탱크 시즈모드 개발이 완료되었습니다.")

#공격 모드 준비 마린:스팀팩, 탱크:시즈모드, 레이스 : 클로킹
for unit in attack_units:
    if isinstance(unit,marine): #지금 객체가 어떤 클래스의 객체인지 확인함
        unit.stimpack()
    elif isinstance(unit,tank):
        unit.set_seize_mode()
    elif isinstance(unit,wraith):
        unit.clocking()
        
#전군 공격
for unit in attack_units:
    unit.attack("1시")

from random import *
#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격을 랜덤으로 받음
    
#게임 종료
game_over()    
    


            
    
    
    








        