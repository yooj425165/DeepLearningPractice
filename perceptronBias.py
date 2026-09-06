import numpy as np
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.6

    tmp = np.sum(w*x)+b

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.6

    tmp = np.sum(w*x)+b

    if tmp > 0:
        return 1
    elif tmp <= 0:
        return 0
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2

    temp = np.sum(x*w) + b

    if temp > 0:
        return 1
    elif temp <= 0:
        return 0

def XOR(x1, x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    return AND(s1, s2)

x1, x2 = map(int,input().split())
print(AND(x1, x2))
print(NAND(x1, x2))
print(OR(x1, x2))
print(XOR(x1, x2))