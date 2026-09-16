import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dataset.mnist import load_mnist
import numpy as np
(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False, one_hot_label=True)

train_size = x_train.shape[0]
batch = 10
batch_mask = np.random.choice(train_size, batch)

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch = y.shape[0]
    return -np.sum(t*np.log(y+1e-7)) / batch


t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(cross_entropy_error(np.array(y), np.array(t)))