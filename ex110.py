#110
if True : # if 문은 if뒤의 조건이 True일때 실행된다. if True이기때문에 항상 실행된다.
    if False: # False이기때문에 실행되지않는다
        print("1")
        print("2")
    else: # if False이므로 else가 실행된다.
        print("3")
else : # if True이므로 else는 진행되지않는다.
    print("4")
print("5") # 들여쓰기가 되어있지 않기때문에 if문의 영향을 받지않는다.