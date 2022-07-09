#사용자 정의 에러
from logging import exception


class bigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg
            

try:
    print("한 자리 숫자만 입력하세요!")
    num1 = int(input("한 자리 숫자 입력: "))
    num2 = int(input("한 자리 숫자 입력: "))
    if num1 >= 10 or num2 >= 10:
        #raise ValueError
        raise bigNumberError("입력 값: {} , {}" .format(num1,num2))
    print("{},{}가 입력되었습니다.".format(num1,num2))
except ValueError:
    print("값이 잘못 입력 되었습니다.")
    
except bigNumberError as err:
    print(err)
    
#무조건 실행되는 구문 finally
finally:
    print("계산기를 이용해주셔서 감사합니다.")
    

#Quiz
#사용자 정의 에러
class soldOutError(exception):
    pass
    
chicken = 10
waiting = 1 #홀 안은 만석, 대기번호는 1번부터
while(True):
    try:
        print("남은 치킨:{}".format(chicken))
        order = int(input("몇 마리 치킨을 주문하시겠습니까?"))
        if order > chicken:
            print("치킨 수가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("대기번호 {} 의 {}마리 치킨 주문이 완료되었습니다.".format(waiting,chicken))
            waiting +=1
            chicken -= order
            
        if chicken == 0:
            raise soldOutError
    except ValueError :
        print("잘못된 값을 입력하였습니다.")
    except soldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
        
        
        