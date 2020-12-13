#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))#zip(a,b)를 하면 a와 b를 합쳐준다.
# 그리고 zip앞에 dict,list,tuple,set중 하나를 선택해서 자료형을 결정해주어야한다
# zip은 합치는 두개의 리스트끼리 인덱스가 맞아야한다. 두 리스트에 맞지않는 인덱스는 출력되지않는다
print(close_table)
#리스트를 합치는 방법에는 +연산자를 사용하거나 a.extend(b)함수를 이용하는 방법도 있다.