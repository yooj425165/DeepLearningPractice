import numpy as np
a = np.array([1010, 1000, 990]) # 이런 값들이 e의 지수가 된다면 무한에 가까움(연산 불가능)
c = np.max(a) # numpy 배열 중 가장 큰 요소
a -= c   # 브로드 캐스팅에 의해 모든 배열의 요소에 1010이 빼짐
# a = [0, -10, -20]

y = np.exp(a) / np.sum(np.exp(a))
print(y)
