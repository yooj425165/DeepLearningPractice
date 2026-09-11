import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dataset.mnist import load_mnist
import pickle
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(normalize = True, flatten=True, one_hot_label= False)
    return x_test, t_test

def init_network():
    file_path = os.path.join(os.path.dirname(__file__), "sample_weight.pkl")
    with open(file_path, 'rb') as f:
        network = pickle.load(f)

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    B1, B2, B3 = network['b1'], network['b2'], network['b3']

    A1 = np.dot(x, W1) + B1
    Z1 = sigmoid(A1)
    A2 = np.dot(Z1, W2) + B2
    Z2 = sigmoid(A2)
    A3 = np.dot(Z2, W3) + B3
    y = softmax(A3)

    return y

x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p==t[i]:
        accuracy_cnt += 1

print("Accuracy:"+str(float(accuracy_cnt)/len(x)))