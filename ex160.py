#160 
list = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in list[:]: # 리스트 안에 있는 변수의 개수만큼 for문이 돌아간다. 이때 i는 list에 있는 값이다 
    if '.h' in i: # 확장자가 .h인 것을 구분하기 위해서 '.h'가 변수 i에 있는지 if문을 이용한다.
        print(i)# 만약 if문이 참이라면 그 변수를 출력한다.
    elif '.c' in i: # '.h'가 아니고  '.c'라면 그 변수를 출력한다. 만약 else:로 하게 된다면 run.py까지 출력된다
	# elif뒤에 조건이 붙어야한다.
        print(i)