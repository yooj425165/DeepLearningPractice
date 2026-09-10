import numpy as np

a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
print(exp_a)

sumExp_a=np.sum(exp_a)
print(sumExp_a)

y = exp_a / sumExp_a
print(y)