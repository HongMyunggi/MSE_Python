#150
list = ["가", "나", "다", "라"]

a = len(list) - 1 # len(list)는 4가 나온다. 그러나 list의 인덱스는 3까지이므로 list의 인덱스에 만족시키기 위해서는 -1을 해야한다

for i in range(len(list)): # list의 갯수만큼 range함수를 돌린다.
    print(list[-i+a]) # i는 range(0,4)를 받는다. 그러므로 0,1,2,3이다
					  # list의 끝에서부터 print하기 위해서 list[-i+a]를 실행한다. 실행하면 list[3],list[2],list[1],list[0]이다
					  # 더 쉽게 하는 방법에는 for i in list[::-1]하고 print(i)를 해주면 된다.