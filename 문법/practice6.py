#클래스
#일반유닛
class unit: 
    def __init__(self,name,hp,damage): #생성자
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{}유닛이 생성되었습니다. 체력은{} 공격력은 {}입니다.".format(self.name,self.hp,self.damage))
        
marine1=unit("마린",5,5) #클래스의 인스턴스
marine2=unit("마린",5,5)
tank=unit("탱크",150,35)

wraith1=unit("레이스",50,5)
#멤버변수는 기본적으로 public인듯
print("{}의 공격력은 {}입니다.".format(wraith1.name,wraith1.damage))

wraith2=unit("빼앗은 레이스",50,5)
#파이선에서는 외부에서 추가로 객체에 멤버변수 넣을 수 있음
wraith2.clocking = True
if(wraith2.clocking == True) :
    print("{}은 현재 클로킹 상태입니다.".format(wraith2.name))
#wraith1에는 clocking 멤버변수 없는 상태임

#공격유닛
class attackUnit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp=hp
        self.damage=damage
        print("파이어뱃 생성")
        
    def attack(self,location):
        print("{0} : {1}방향으로 적군을 공격합니다.[공격력:{2}]".format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name,damage)) 
        self.hp-=damage
        print("{0} : 현재 남은 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 죽었습니다.".format(self.name))
            
firebat1=attackUnit("파이어뱃",50,16)
firebat1.attack("1시")
firebat1.damaged(25)
firebat1.damaged(25)


