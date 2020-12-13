#210
def message1(): # message1()를 입력하면 print("A")가 출력되게 함수를 만들었다
    print("A")

def message2(): #message2()를 입력하면 print("B")가 출력되게 함수를 만들었다.
    print("B")

def message3(): # message3를 입력하면 for문이 돌아가도록 함수를 만들었다.
    for i in range (3) : # range(3)을 했기때문에 0,1,2로 3변 돌아간다.
        message2() # for문에 의해서 3변 반복된다
        print("C") # for문에 의해서 3변 반복된다
    message1() # 들여쓰기가 되어있지 않기 때문에 for문에 포함되지않는다.

message3() # 결국 B C B C B C A 가 출력된다.