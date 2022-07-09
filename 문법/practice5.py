#빈 자리는 빈공간으로 두고, 오른쪽 정렬하면서 총 10자리 공간을 확보
print("{0: >10}".format(500))

#같은 조건에 부호표시
print("{0: >+10}".format(+500))
print("{0: >+10}".format(-500))

#빈 자리는 _로 채우고, 왼쪽정렬하면서 총 10자리 공간 확보 밑 부호표시
print("{0:_<+10}".format(-3000))

#3자리마다 , 붙여주기
print("{0:,}".format(100000000000))

#3자리마다 , 붙여주기 밑 부호
print("{0:+,}".format(100000000000))

#3자리마다 , 붙이고 부호도 붙이고, 10자리수 확보하기 돈 많으면 행복하니 부호는 ^ 로 하기
print("{0:^<+30,}".format(1000000000000))

#소수점 출력
print("{0:f}".format(5/3))

#소수점 특정자리수 까지만
print("{0:.2f}".format(5/3))

#파일 입출력
score_file = open("score.txt","w",encoding="utf8") #utf8 is for 한국어
print("수학 : 0점",file = score_file)
print("영어 : 50점",file = score_file)
score_file.close()

score_file = open("score.txt","a",encoding="utf8") #utf8 is for 한국어
score_file.write("국어 : 10점")
score_file.write("\n코딩 : 100점")
score_file.close()

score_file = open("score.txt","r",encoding="utf8") #utf8 is for 한국어
print(score_file.readline()) #한줄만 읽고 커서는 다음줄로 이동
print(score_file.readline()) #한줄만 읽고 커서는 다음줄로 이동
print(score_file.readline()) #한줄만 읽고 커서는 다음줄로 이동
print(score_file.readline()) #한줄만 읽고 커서는 다음줄로 이동
print(score_file.read()) #전체읽기
score_file.close()

score_file = open("score.txt","r",encoding="utf8") #utf8 is for 한국어
while True:
    print("while문")
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()


score_file = open("score.txt","r",encoding="utf8") #utf8 is for 한국어
lines = score_file.readlines() #list형태로 저장
print("반복문")
for line in lines:
    print(line)
score_file.close()    




#pickle #프로그램상에서 데이터를 파일 형태로 저장. 그걸 누가 받아서 쓰면 마찬가지로 pickle을 이용해 읽어서 데이터를 뽑아서 코드에 사용
import pickle
profile_file=open("pickle.pickle","wb") #무조건 pickle은 바이너리로!
profile={"이름" : "이창민", "나이" : 30, "취미" : ["염탐하기","쳐먹기"]}
pickle.dump(profile,profile_file) #dump is pickle writing
profile_file.close()


profile_file=open("pickle.pickle","rb") #무조건 pickle은 바이너리로!
print("\npickle을 이용해 읽기")
profile=pickle.load(profile_file)
print(profile)
profile_file.close()





#with : 파일입출력, close해줄 필요 없음
import pickle
print("\nwith사용")
with open("pickle.pickle","rb") as profile_file :
    print(pickle.load(profile_file))
    
with open("study.txt","w") as study_file :
    study_file.write("파이선을 열심히 공부하고 있어요")

with open("study.txt","r") as study_file :
    print(study_file.read())
    
    
#quiz
for index in range(1,6):
    with open(str(index)+ "주차.txt","w",encoding="utf8") as report_file:
        report_file.write("{}주차 보고서".format(index))
    