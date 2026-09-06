import numpy as np
import matplotlib.pylab as plt
def step_function(x): # x가 실수(부동소숫점)만 받아들이므로 넘파이 배열을 인수로 넣지 못함
    if x > 0:
        return 1
    else:
        return 0

def step_function(x):
    y = x > 0
    return y.astype(int) #y의 타입을 파라미터 값으로 바꾸는 numpy 함수

def step_function(x):
    return np.array(x>0, dtype=int) #지금 나온 배열을 정수(dtype=int)로 바꿈

x = np.array([0, 1, 1])
y = x > 0
print(y) # [False, True, True]

x = np.arange(-5.0, 5.0, 0.1) # -5.0에서 5.0까지 0.1씩 증가하며 요소를 넣은 배열
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

def sigmoid(x): # 시그모이드 함수는 x>0일때 1에 가까워지고, x<0일 때 0에 가까워지며, x=0이면 정확히 0.5이다.
    return 1/(1+np.exp(-x)) # .exp()는 자연상수 수식을 의미한다.(e^-x, numpy 함수)

x = np.array([1.0, -1.0, 2.0])
print(sigmoid(x))

x = np.arange(-5.0, 5.0, 0.1) # -5.0에서 5.0까지 0.1씩 증가하며 요소를 넣은 배열
y = sigmoid(x)
print(y)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()





