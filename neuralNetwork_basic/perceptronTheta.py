def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    temp = w1*x1 + w2*x2
    if temp > theta:
        return 1
    elif temp <= theta:
        return 0

x1, x2 = map(int, input().split())
print(AND(x1, x2))