#240
def 함수0(num) : # return이 있기 때문에 함수0(num)을 실행한 값을 돌려준다.
    return num * 2

def 함수1(num) :
    return 함수0(num + 2) # return이 있기때문에 함수0(num + 2)값을 실행한 후 돌려준다.

def 함수2(num) :
    num = num + 10 # num += 10으로도 표현 가능하다.
    return 함수1(num) # num+=10을 실행한 후에 return이 있기때문에 함수1(num)을 실행한 값을 돌려준다

c = 함수2(2) # 만약 위 함수중 return이 없다면 실행한 값을 c로 대입할 수 없다.
print(c) # 값은 함수1(2 + 10) = 함수0(12+2) = 14*2 = 28이다