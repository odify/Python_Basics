import numpy as np

two_d = np.array([[1,2,3,4], [5,6,7,8]]) # 2 x 4
one_d = np.array([[10]]) # 1
three_d = np.ones((3, 2)) # 3 x 2

print(np.add(two_d,one_d))

print(np.add(one_d, three_d))