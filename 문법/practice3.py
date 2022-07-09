def open_account():
    print("계좌가 생성되었습니다.")
    
def deposit(balance,money):
    print("입금이 완료되었습니다. {}원이 계좌에 있습니다.".format(balance+money))
    return balance+money

def withdraw(balance,money):
    if(balance >= money):
        print("출금이 가능합니다. {}원이 남았습니다.".format(balance-money))
        return balance-money
    else:
        print("출금할 수 없습니다. {}원이 있습니다.".format(balance))
        return balance

def withdraw_night(balance,money):
    commision = 100
    print("밤에 출금이 정상적으로 되었습니다. 수수료가 나갑니다.")
    return commision,balance-money-commision                        # 리턴에 튜플형식

open_account()
balance = 0
balance = deposit(balance,3000)
balance = withdraw(balance,1500)
(commision,balance) = withdraw_night(balance,500)
print("수수료는 {0}이며, {1}원이 남았습니다.".format(commision,balance))










# 기본값 #########################################################################################################
#같은 고등학교면 나이가 같고 같은 수업듣잖아? 그럼 매번 써주니?
def profile(name,age=19,main_lang="C언어"):
    print("이름은 {0}이고 나이는 {1}살이며 {2}를 사용한다.".\
        format(name,age,main_lang))
    
profile("김현배",29,"C++")
profile("이종윤",30,"JavaScript")

profile("마노")
profile("이창민")





# 키워드값 #########################################################################################################
def profile2(name,age,main_lang):
    print(name,age,main_lang)
    
profile2(age=20,main_lang="C",name="이창민")
profile2(main_lang="python",age=32,name="개머민")







# 가변인자 #########################################################################################################
def profile3(name,age,*language):
    print("이름은 {0}\t나이는 {1}\t".format(name,age), end = " ") #줄바꿈안함
    for lang in language:
        print(lang, end=" ")
    print()
    
profile3("김태호",40,"C","C++","C#","javaScript","python")
profile3("이창민",30,"C")









#지역변수 전역변수 #########################################################################################################
gun = 10 #전역변수
def checkPoints(soliders):
    global gun #전역공간에 있는 gun변수 사용
    gun = gun - soliders
    print("남은 총은 {}자루입니다.".format(gun))
    
def checkPoints_ret(gun,soliders):
    gun = gun - soliders
    print("남은 총은 {}자루입니다.".format(gun))
    return gun
    
print("총 건의 수는 {}자루입니다.".format(gun))
checkPoints(3)

#gun = 7
checkPoints_ret(gun,5)















# Quiz ################################################################################################
def std_weight(height,gender):
    if gender == "남자":
        weight = round((height*0.01) * (height*0.01) * 22, 2)
        print("키 {0}cm 남자의 표준체중은{1}kg입니다.".format(height,weight))
    elif gender == "여자":
        weight = round((height*0.01) * (height*0.01) * 21, 2)
        print("키 {0}cm 여자의 표준체중은{1}kg입니다.".format(height,weight))
        
std_weight(175,"남자")