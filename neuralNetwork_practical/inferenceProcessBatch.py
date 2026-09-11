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
        load_mnist(normalize = True, flatten=True, one_hot_label= False) #Flatten : 데이터 전처리
    return x_test, t_test

def init_network():
    file_path = os.path.join(os.path.dirname(__file__), "sample_weight.pkl")
    with open(file_path, 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    B1, B2, B3 = network['b1'], network['b2'], network['b3'] #/sample_weight.pkl 상 key값이 Wn, bn

    A1 = np.dot(x, W1) + B1
    Z1 = sigmoid(A1)
    A2 = np.dot(Z1, W2) + B2
    Z2 = sigmoid(A2)
    A3 = np.dot(Z2, W3) + B3
    y = softmax(A3)

    return y

x, t = get_data()
network = init_network()
batch = 100
accuracy_cnt = 0
for i in range(0, len(x), batch):
    x = x[i:i+batch]
    y = predict(network, x)
    p = np.argmax(y, axis=1) # 각 행마다 가장 확률이 높은 인덱스 (axis=0(기본값)은 각 열마다 가장 확률이 높은 인덱스)
    accuracy_cnt += np.sum(p==t[i:i+batch]) # bool 형 배열 생성, np.sum()을 실행하면 True만 모두 더함

print("Accuracy:"+str(float(accuracy_cnt)/len(x)))
