#290
class 부모: # 부모라는 class를 만든다
    def __init__(self): 
        print("부모생성") 

class 자식(부모): # 부모에 상속되어있는 자식이라는 class를 만든다.
    def __init__(self):
        print("자식생성") 
        super().__init__() # super().로 상위class로 간후 상위class에 있는 __init__()을 실행한다.

나 = 자식() # 자식 class에 객체를 만들어준다. 그리고 실행한다 
          # 그러므로 자식()을 하게 되면 print("자식생성")을 실행한후 class 부모에 있는 print("부모생성")을 실행한다.