import numpy as np
import matplotlib.pylab as plt
def ReLU(x):
    return np.maximum(0, x) # .maximum : 파라미터 값 중 큰 것을 반환

x = np.arange(-5.0, 5.0, 0.1)
y = ReLU(x)

plt.plot(x, y)
plt.show()
