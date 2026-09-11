import numpy as np
def softmax(x):
    exp_x = np.exp(x)
    sum_exp = np.sum(exp_x)
    y = exp_x/sum_exp
    return y

a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
print(exp_a)

sumExp_a=np.sum(exp_a)
print(sumExp_a)

y = exp_a / sumExp_a
print(y)

print(softmax(np.array([0.3, 2.9, 4.0])))