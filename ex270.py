#270
class Stock: # class를 생성한다
    def __init__(self, name, code, per, pdr, dividend): init이라는 객체안에 들어갈 값을 설정한다
        self.name = name # self라는 객체에 name을 넣는다
        self.code = code # self라는 객체에 code를 넣는다
        self.per = per # self라는 객체에 per을 넣는다
        self.pdr = pdr # self라는 객체에 per을 넣는다
        self.dividend = dividend # self라는 객체에 dividend를 넣는다
    


samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83) # samsung이라는 객체를 만들고 값을 넣어주었다
hyundai = Stock("현대차", "005380", 8.70, 0.35, 4.27) # hyundai라는 객체를 만들고 값을 넣어주었다
lg = Stock("LG전자", "066570", 317.34, 0.69, 1.37) # lg라는 객체를 만들고 값을 넣어주었다

list = [] # 비어있는 list를 만들어야 samsung과 hyundai과 lg를 append를 이용하여 한 곳에 넣을 수 있다

list.append(samsung) # list에 samsung이라는 객체를 넣어준다
list.append(hyundai) # list에 hyundai라는 객체를 넣어준다
list.append(lg) #list애 lg라는 객체를 넣어준다

for i in list: # 리스트에 있는 객체들을 i에 대입시키고 for문이 돌아간다
    print(i.code, i.per) # 첫번째 i는 samsung이므로 samsung.code와 samsung.per과 같다