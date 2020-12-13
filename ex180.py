#180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = [] # 빈 리스트를 지정해줘야 append함수를 사용할 수 있다.

for i in range(len(low_prices)): # range(len(low_prices))는 low_prices의 개수를 이용한다.
		# low_prices가 갯수가 적기때문에 range(5)를 이용해도 되지만 갯수가 셀수없을때는 len을 사용해야한다.
    volatility.append(-low_prices[i] + high_prices[i]) #a.append(b)는 a에 b를 추가한다는 함수이다.
	# 고가와 저가의 차를 구해야하기때문에 low_prices[i]와 high_prices[i]를 이용하여 for문에서 나온 i의 값을 도출할수있다. 
        
print(volatility) # 들여쓰기를 한다면 volatility에 추가되는 값을 볼수있다.