import numpy as np


my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr = np.array(my_list)

print(arr)

print(type(arr.shape))
h, w = arr.shape[:2]

print(h, w)
