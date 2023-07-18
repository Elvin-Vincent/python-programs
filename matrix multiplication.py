import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

b = np.array([[1,2,3],[4,5,6],[7,8,9]])


m = np.add(a,b)
t=np.transpose(m)
s=np.subtract(a,b)
mul=np.dot(a,b)
print("addition")
print(m)
print("transpose")
print(t)
print("substraction")
print(s)
print("multiplication")
print(mul)

