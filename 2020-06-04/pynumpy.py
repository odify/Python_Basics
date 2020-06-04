#Learn numpy...

import numpy as np

r = int(input())

lst = [float(x) for x in input().split()]

arr = np.array(lst)

newarr = arr.reshape(r, -1)

print(newarr)