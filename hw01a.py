import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr)
arr = np.append(arr, [5, 6, 7, 8])
print(arr)

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
w = [10, 10 , 10]
r = np.ones([3, 3])
z = np.dot(x, w)

out = x - r

w2 = np.load('model.npy')


