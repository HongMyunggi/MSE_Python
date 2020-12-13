import random # 계좌번호를 임의로 생성하기 위해 random을 import해준다.


class Account: # Account 라는 class만든다.
    # class variable
    account_count = 0 # 계좌를 얼마나 생성했는지 알기위해 초기 count값을 0으로 설정한다
    deposit_log = [] # 출금했을 때 마다 값을 list에 저장하기 위해 비어있는 list 생성한다
    withdraw_log = [] # 입금했을 때 마다 값을 list에 저장하기 위해 비어있는 list 생성한다.
    
    def __init__(self, name, balance): # name,balance에 값이 들어간다.
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name # 이름의 변수을 name으로 설정한다
        self.balance = balance # 초기 값의 변수를 balance로 설정
        self.bank = "SC은행" #은행명은 sc은행으로 설정한다. 그러므로 항상 변하지않는다.

        # 3-2-6
        num1 = random.randint(0, 999) #random.randint(a,b)는 a부터 b까지의 값중 무작위로 값을 가지고온다
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999) # import random을 이용하여 임의으 3자리-2자리-6자리 계좌번호를 만든다.

        num1 = str(num1).zfill(3) #zfill() 이용하면 문자열 앞을 0으로 채울수 있다. 괄호에 3이 들어갔으므로 만약 num1이 23이라면 023으로 출력한다. 
        num2 = str(num2).zfill(2) # zfill()이용하여 어떤상황에서라도 3자리 - 2자리 - 6자리의 계좌번호를 만든다
        num3 = str(num3).zfill(6)  
        self.account_number = num1 + '-' + num2 + '-' + num3  # -와 num을 이용하여 계좌번호 생성
        Account.account_count += 1 # 생성 되었을 시 count에 1을 더하여 count한다
        
    @classmethod # @classmethod를 이용하여 class의 어떤 속성에도 접근 가능하다
    def get_account_num(cls): # 생성된 계좌의 개수를 출력하는 함수를 만든다
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount): # 입금을 하는 함수를 만든다
        if amount >= 1: # 1원 이상일때 라는 조건을 입력한다. 음수나 0이 입력될 수 있기때문이다.
             
            self.balance += amount # 초기값 balance에 amount 더하기
            
            self.deposit_count += 1 # 예금 횟수를 count한다
            
            self.deposit_log.append(amount) # 클래스 변수 deposit_log(list)에 금액 저장
             
            
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지급
                self.balance = (self.balance * 1.01) # 이쟈율이 1%이다.
            

        else : # 0원 혹은 음수 입력하였을 시 잘못입력되었다는 것을 알려주기 위해서이다
            print("잘못된 값(0혹은 변수)를 입력하였습니다.")
       
        
    def withdraw(self, amount):
        if self.balance >= amount: # 가지고 있는 값보다 출금하려는 값이 적을 경우이다
            self.withdraw_log.append(amount) 
            self.balance -= amount # 가지고 있는 값에서 출금하려는 값 뺀다
            
            
        else : # 만약 가지고 있는 값보다 출금하려는 값이 클 경우 돈을 출금할 수 없다. 그러므로 아래 print를 출력한다
            print("출금하려는 액수가 잔액보다 많습니다.")
        
        

    def display_info(self): # 사용자의 정보(은행이름, 예금주, 계좌번호, 잔고) 출력하는 함수를 만든다
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self): # 출금 내역 출력하는 함수를 만든다
        B = 1 # 임의의 변수
        print('<출금 내역 출력>') 
        for i in self.withdraw_log : # 반복문을 통하여 withdraw_log list에 저장된 값들을 순서대로 출력하는 for문을 만든다
            print(B,'번째 출금 금액은 ',i,'원 입니다')
            B += 1 # B번째를 출력해야하기때문에 B+=1을 이용한다
            
    def deposit_history(self): # 입금 내역 출력하는 함수를 만든다
        A = 1
        print('<예금 내역 출력>')
        for i in self.deposit_log : # 반복문을 통하여 withdraw_log 리스트에 저장된 값들을 차례로 출력하는 for문을 만든다
            print(A,'번째 입금 금액은 ',i,'원 입니다')
            A += 1 # A번째를 출력해야하므로 A+=1을 이용한다.
            
       
            
