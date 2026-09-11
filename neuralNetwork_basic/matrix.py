import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(np.dot(A,B)) # A*B는 [[5,12],[21,32]](브로드 캐스팅)

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2],[3,4],[5,6]])

#(n*k) * (k*m) 행렬연산 이므로 (2*3) * (3*2)이면 3=3이므로 성립

print(np.dot(A,B))

C = np.array([[1,2],[3,4]])

print(np.dot(C,A)) # A, C는 오류