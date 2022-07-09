#PASS

#일반유닛
class unit: 
    def __init__(self,name,hp,speed): #생성자
        self.name=name
        self.hp=hp
        self.speed = speed
        
    def move(self,location):
        print("[지상유닛이동")
        print("{}가 {}방향으로 이동합니다.[속도 : {}]".format(self.name,location,self.speed))
        
#PASS사용
#일단은 그냥 넘긴다는 것임
class buildingUnit_pass(unit):
    def __init__(self, name, hp, location):
        pass
    
bu = buildingUnit_pass("호날두",100,"1시")

#super사용
class buildingUnit(unit):
    def __init__(self, name, hp, location):
        #unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0) #speed is 0
        self.location = location
        
        
#super 문제점
class unit2:
    def __init__(self):
        print("unit 생성자")
        
class flyable2:
    def __init__(self):
        print("flyable 생성자")

class flyingUnit(unit2,flyable2):
    def __init__(self):
        super().__init__()
        
dropship = flyingUnit() ## unit 생성자만 호출됨
#순서상 앞 부분만 이닛 함수만 호출됨
#다중상속을 할 때는 명시적으로 호출해라

class flyingUnit2(unit2,flyable2):
    def __init__(self):
        unit2.__init__(self)
        flyable2.__init__(self)
        
dropship2 = flyingUnit2()







