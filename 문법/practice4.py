print("C","C++","Java") #C C++ Java
print("C","C++","Java", sep =" vs ") #C vs C++ vs Java

print("C++","JavaScrpit",sep=" , ", end=" ? ") #자동개행 안함
print("무엇이 더 재밌을까요?")

import sys
print("C++","JavaScrpit", file=sys.stdout)
print("C++","JavaScrpit", file=sys.stderr)



#시험성적
scores = {"영어":80,"수학":50,"코딩":100}
for (subject,score) in scores.items():
    #print(subject,score)
    print(subject.ljust(8), str(score).rjust(4), sep=" : ")
    
    

#은행 대기 순번표
for i in range(1,21): #1~20
    #print("대기 순번표:{}".format(i))
    print("대기 순번표 : " +str(i).zfill(3))
    
    

#사용자 입력 형태로 받게 되면 항상 문자열로 저장된다
answer = input("값을 입력해주세요 ")
print("값은 " +answer+ "입니다.")