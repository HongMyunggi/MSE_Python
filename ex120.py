#120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

a = input() # 입력값을 조건문에 적용시키기위해 사용했다.

if a in fruit.values(): # a에 입력한 값이 fruit의 value값에 있는지 참거짓을 판별
    print('정답입니다.')
else: # 만약 a에 key값을 입력하게된다면 if의 조건이 value값에 대한 것이기 때문에 False가 된다
    print('오답입니다.')
	
# 만약 key값이 dict에 포함되어있는지 구분하고 싶다면 if a in fruit.keys():이용하면 된다.