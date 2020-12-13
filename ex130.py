#130
import requests #비트코인 사이트에서 정보를 dict로 가지고온다. requests라는 모듈을 가지고온다.
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

diff = float(btc['max_price']) - float(btc['min_price']) # type(btc['max_price'])를 먼저 실행시킨후 float인지 string인지 구분해야한다
opening = float(btc['opening_price'])#type(btc['opening_price'])의 결과는 string이 나오기때문에 float으로 변환해주어야한다.
high = float(btc['max_price'])

if (opening-diff) > high: print("상승장") # 시가와 변동폭이 고가보다 크면 상승장을 출력한다.
else: print("하락장") # if문의 조건을 만족하지않는다면 하락장을 출력한다