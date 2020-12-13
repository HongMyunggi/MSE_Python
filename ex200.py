#200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

result = 0
for i in ohlc[:]: # ohlc의 1행에는 string값이 있다
    if type(i) == int: # string값은 빼기 연산자를 사용할수없기때문에 string행이 있을때는 result를 실행시키지않는다.
        result += (i[3] - i[0]) # 시가는 0으로 인덱싱되어있고 종가는 3으로 인덱싱되어있다.
								# 그러므로  ohlc에서 가지고온 행의 3번째값과 0번째값이다
            
print(result)