#import 뒤에는 .py(모듈)나, 패키지만,, 클래스나 함수쓰려면 from과 같이 나와야한다
#from뒤에는 .py
#모듈
import p_module
p_module.price()
p_module.price_solder()

import p_module as practice_module
practice_module.price()
practice_module.price_solder()

from p_module import *
price()
price_solder()

from p_module import price_solder as price
price() #price_solder()임!


#패키지
import package.korea
trip_to = package.korea.koreaPkg
trip_to.detail()

from package.korea import koreaPkg
trip_to = koreaPkg
trip_to.detail()

from package import korea
trip_to = korea.koreaPkg
trip_to.detail()

from package import *
trip_to = korea.koreaPkg
trip_to.detail()
#init.py의 all에 tailand들어감 그래서 되는것

import inspect
import random
print(inspect.getfile(random))

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())