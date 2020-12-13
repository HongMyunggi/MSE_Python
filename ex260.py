# 260
class OMG : # OMG라는 클래스를 만들었다
    def print() : # 클래스 객체를 생성할 때 만들어진 객체가 method를 호출 할 때 객체가 인자로 들어가야한다.	
        print("Oh my god")
        
myStock = OMG() # OMG class를 가진 myStock이라는 객체를 지정한다.
myStock.print() # OMG.print(myStock)으로 출력하게된다. OMG class에서 print함수는 인자값이 없기때문에 오류가 나온다.
                # 그러므로 print(self)로 인자를 설정해주어야 오류가 나오지않는다.