#300
per = ["10.31", "", "8.00"]

for i in range(len(per)): # range(len(per))을 사용하면서 per의 개수만큼 for문을 돌린다
    try: # try를 사용했기때문에 밑에 조건에 충족하면 코드를 실행한다.
        print(float(per[i]))
    except: # try에서의 조건에 충족되지 않으면 except를 실행한다.
        print(str(per[i])) # string인 문자를 출력한다
        if type(per[i]) == str: # 
            print(per[i],"는 string입니다")
    else:
        print("float입니다")# try가 실행되면 else도 실행된다
    finally: # 조건에 상관없이 항상 발생한다
        if per[i] == per[-1]: # 리스트의 마지막에 프린트 된다 
            print("완료했습니다") 
        elif type(per[i]) == float: # per[i]의 값이 float이거나 str일때 다음으로 넘어간다를 출력한다
            print(per[i+1],"로 넘어갑니다")
        elif type(per[i]) == str: # 위의 elif문만 사용하면 str일경우에 출력할 수 없다 
            print(per[i+1],"로 넘어갑니다") 