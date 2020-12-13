#250
import numpy as np # numpy의 arange함수를 사용하기위해서 import numpy as np를 사용해야한다
				   # import numpy as np를 사용하면 numpy를 np로 대신 사용할 수 있다
for i in np.arange(0,5,0.1): # arange함수는 range함수와 기능이 동일하다. 
							   # 그러나 range함수에는 실수 단위로 증가하는 것이 불가능하다.
    print(i)