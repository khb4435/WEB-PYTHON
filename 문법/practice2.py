# if문 ####################################################################################
weather = "맑아요"
if weather == "비" or weather =="눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요없어요")
    
#temp = int(input("기온이 몇도에요?"))                   #input은 항상 str 형식으로 받기 때문에 정수로 저장하기 위해
temp = 25
if temp >= 30:
    print("너무 더워요")
elif 0<temp<30: #elif 0<temp and temp<30
    print("살만해요")
else:
    print("너무 추워요")    
    
    
    
    






# for문 ####################################################################################
for waiting_num in [0,1,2,3,4]:
    print("대기번호 : {}".format(waiting_num))
    
for waiting_num in range(1,6): #1,2,3,4,5
    print("대기번호 : {}".format(waiting_num))
    
starbucks=["아이언맨","토르"]
for customer in starbucks:
    print("{}, 커피가 준비 되었습니다.".format(customer))
    














# while 문 ####################################################################################
customer = "토르"
index = 5
while(index >=1) :
    print("{0}, 커피가 준비 되었어요. {1}번 남았습니다.".format(customer,index))
    index -= 1
    if index == 0:
        print("커피는 폐기처리되었습니다.")
















# continue,break문 ####################################################################################
absent=[2,5] #결석
#no_book=7 하면 에러나네?
no_book=[7]
for students in range(1,11): #1,2,3,4,5,6,7,8,9,10
    if students in absent:
        continue#를 만나면 다음 문장을 실행하지 않고 다시 반복문으로 간다
    elif students in no_book:
        print("오늘 수업 끝. {}아 넌 교무실로 따라와".format(students))
        break #를 만나면 반복문 탈출
    print("{}아, 책을 읽어봐".format(students))
    
    
    
    








# 한줄 for문 ####################################################################################
#1,2,3,4,5 -> 101,102,103,104,105
students=[1,2,3,4,5]
students=[i+100 for i in students]
print(students)

#학생이름을 길이로 전환
students = ["Iron man","torr","이창민"]
students = [len(i) for i in students]
print(students)

#학생이름을 대문자로 변환
students = ["Iron man","torr","이창민"]
students = [i.upper() for i in students]
print(students)















# QUIZ ###########################################################################################
from random import *
count = 0
for i in range(1,51): #1~50
    time=randint(5,51) #5~50
    if time >=5 and time <=15:
        print("[0]{0}번째 손님 소요시간 {1}분입니다.".format(i,time))
        count += 1
    else:
        print("[ ]{0}번째 손님 소요시간 {1}분입니다.".format(i,time))
print("총 탑승 수 = {}".format(count))
        






