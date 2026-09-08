import numpy as np
import matplotlib.pylab as plt
def ReLU(x):
    return np.maximum(0, x) # .maximum : 파라미터 값 중 큰 것을 반환

def ReLUmyver(x):
    if x <= 0:
        return 0
    else:
        return x

x = np.arange(-5.0, 5.0, 0.1)
y = ReLU(x)

x1 = np.arange(-5.0, 5.0, 0.1)
y1 = ReLUmyver(x1)

plt.plot(x, y)
plt.show()

