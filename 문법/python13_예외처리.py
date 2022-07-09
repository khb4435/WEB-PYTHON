try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{} / {} = {}입니다.".format(num1,num2,int(num1/num2)))
except ValueError:
    print("값을 잘못 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err1:
    print("알 수 없는 오류 발생")
    print(err1)