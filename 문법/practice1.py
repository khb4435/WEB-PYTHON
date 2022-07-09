print("ㅋ"*10)

animal = "강아지"
name = "연탄이"
age = 4
hobby="산책"
is_adult = age>=3 #true

print("우리집 " +animal+ "의 이름은 " +name+ "이에요") #문자열 더하기
hobby = "공놀이"

#print(name+"는 "+str(age)+"살이며 "+hobby+"을 아주 좋아해요")
print(name,"는 ", age, "살이며 ", hobby, "를 아주 좋아해요") #여러 자료형 ,

print(name+"는 어른일까요?"+str(is_adult))

'''
이렇게 하면 여러 문장이 주석처리됩니다.
또 주석처리 하고 싶은 문장들을 드래그시키고 command + /을 하면 됩니다.
'''

print(10/3) #3.33333333
print(10//3) #3
print(2**3) #8 : 2^3
print(1!=3) #true


#print(!(1!=3)) #이거 오류

print(not (1!=3)) #false
print((3>5)and(1>2)) #false
print((3>5)&(1>2)) #false
print((3>5)or(1>2)) #false
print((3>5)|(1>2)) #false
print(4>1>7) #false
print(abs(-5)) #5
print(pow(4,3)) #4^3
print(max(5,2))
print(min(5,2))
print(round(3.1)) #반올림

from math import *
print("수학모듈사용")
print(ceil(3.1)) #4
print(floor(3.9)) #3
print(sqrt(16)) #4

number = 4
number += 2
print(number)

from random import *
print(random()) #0.0~1.0
print(random()*10) #0.0~10.0
print(int(random()*10)) #0~10
print(randrange(1,45)) #1~45

sentence1='나는 소년입니다.' #어? 문자열을 ' ' 처리로도 가능하네 
print(sentence1)
sentence2="파이선이 쉬워요"
print(sentence2)

sentence3='''
나는 소년입니다.
파이선이 쉬워요
'''
print(sentence3)

sentence4="""
나는 소년입니다.
파이선이 싫어요
"""
print(sentence4)







#문자열 슬라이싱 ########################################################################
jumin = "940204-1352482"
print("성별은 "+jumin[7]) #1
print("년"+jumin[0:2]) #0부터 2직전까지 #94
print("월"+jumin[2:4]) #02
print("일"+jumin[4:6]) #04
print("생년월일"+jumin[:6]) #처음부터 6직전까지
print("뒤7자리"+jumin[7:]) #7번째부터 끝까지
print("뒤7자리(뒤에서부터)"+jumin[-7:]) 







#문자열 처리함수 ########################################################################
python = "Python is Amazing"
print(python.lower()) 
print(python.upper())
print(python[0].upper())
print(len(python))
print(python.replace("Python","java"))

index = python.index("n")
print(index)
index = python.index("n",index+1)
print(index)

print(python.find("java")) #없을 때 -1 리턴
#print(python.index("Java")) #없을 때 에러리턴

print(python.count("n"))











#문자열 출력 ########################################################################
#방법1
print("나는 %d살입니다" %20) #퍼센트 퍼센트
print("나는 %s을 좋아해요." %"파이썬")
print("Apple은 %c로 시작해요" %"A")
print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

#방법2
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

#방법3
print("나는 {age}살이고 {color}색을 좋아해요".format(age=4,color="빨간"))
print("나는 {age}살이고 {color}색을 좋아해요".format(color="빨간",age=4))

#방법4(v3.6이상~)
age=10
color="검정"
print(f"나는 {age}살이고 {color}색을 좋아합니다.")










#탈출문자 ########################################################################
# print("안녕하세요
#       반갑습니다.") #오류

print("안녕하세요 \n반갑습니다.")

# 저는 "나도코딩" 입니다.
print("저는 \"나도코딩\" 입니다.")

# \\ : 문장내에서 \
print("C:\\Users\\NadoCoding\\Desktop\\PythonWorkSpace") 

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine ") #Pine Apple

# \b : 백스페이스
print("Redd\b Apple")    #Red Apple

# \t : 탭
print("Red \tApple")

url = "http:\\naver.com"
my_str=url.replace("http:\\","") #naver.com
my_str=my_str[:my_str.index(".")] #my_str[0:5] ->naver
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" #nav51!
print("{0}의 password는 {1}입니다.".format(url,password))












#리스트(순서가 있는 여러 자료형 들어가는 배열) ###########################################################################
li = [10,"hi",True]

subway=["유재석","조세호","김용만"]
#조세호씨는 몇번째에 위치해있는가?
print(subway.index("조세호")) #1

#하하씨가 다음 정류장에 탐
subway.append("하하") #유재석 조세호 김용만 하하

#정형돈을 1번에 집어넣음
subway.insert(1,"정형돈") #유재석 정형돈 조세호 김용만 하하

#지하철에 탄 사람을 뒤에서 하나 뺀다
print(subway.pop()) #유재석 정형돈 조세호 김용만
#같은 이름의 사람이 몇명인지 확인하기

subway.append("유재석") #유재석 정형돈 조세호 김용만 유재석
print(subway.count("유재석")) #2

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort() #[12345]
print(num_list)

#뒤집기도 가능
num_list.reverse() #[54321]
print(num_list)

#모두지우기
num_list.clear()
print(num_list) #[]

#서로 다른 두 리스트 확장하여 하나의 리스트로 합치기
num_list.append([1,2,3,4,5]) # [ [1,2,3,4,5] ]
print(num_list)
mix_list = [True,20,"love"]
num_list.extend(mix_list) #[ [1,2,3,4,5] ,true,20,"love"]
print(num_list)

#list.append(x)는 리스트 끝에 x 1개를 그대로 넣습니다.
#list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣습니다.













#딕셔너리(사전:정의 + 설명) (리스트(구조체) + 키&벨류) ###########################
#키는 중복될 수 없음
cabinet = {3:"유재석", 100:"김태호", 5:True, 6:4, '이름':"현배"}
print(cabinet[3])
print(cabinet.get(3))

#print(cabinet[50]) #에러나면서 종료됨
print(cabinet.get(50)) #None출력됨
print(cabinet.get(50,"사용 가능한 키"))

print(3 in cabinet) #true
print(50 in cabinet) #false

cabinet = {"A-3":"유재석", "B-100" : "김태호"}
print(cabinet["A-3"])

#새로운 손님
cabinet["c-20"] = "조세호"
print(cabinet)

#Value 업데이트
cabinet["A-3"] = "김종국"

#떠난 손님
del cabinet["A-3"]

#키 들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 둘 다 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()

















#튜플 ###########################################################################
#튜플은 픽스 된 리스트(배열)와 비슷하다 그러나 리스트와는 다르게 변경되지 않고, 속도가 더 빠름
menu = ("돈까스","치킨가스",4,True)
print(menu[0])

#메뉴에 생선가스 추가
#menu.add("생선가스") #불가 왜? 튜플은 수정할 수 없음

#튜플에 다른 쓰임
#name="김종국"
#age = 20
#print(name,age)
(name,age) = ("유재석",15)
print(name,age)















#세트 (집합) ###########################################################################
#중복을 허용하지 않고, 순서가 없음
my_set={1,2,3,3,3}
print(my_set)

java = {"유재석","박명수","하하"}
python = set(["유재석","김태호"])

#교집합 (java와 python을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

#합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (only java)
print(java - python)
print(java.difference(python))

#python을 박명수가 할 줄 알게됨
python.add("박명수")

#박명수가 java를 잊어버림
java.remove("박명수")








##자료구조의 변경 ##########################################################################################
menu = {"김밥","참치김밥"} #set
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu,type(menu))





#상품권
from random import *
#users=[1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20]
users=range(1,21)

print(type(users)) #range
users=list(users)

shuffle(users)
#무작위로 뽑되 중복 불가 -> 1개 뽑고 1개뽑고... 4개 뽑지말고 그냥 4개 한번에 뽑자
winners=sample(users,4)
print("---당첨입니다---")
print("치킨 당첨자는 : {0}".format(winners[0]))
#print("커피 당첨자는 : {1},{2},{3}".format(list(winners[1:3])))
print("커피 당첨자는 : {0}".format(winners[1:]))
print("---축하합니다---")


























