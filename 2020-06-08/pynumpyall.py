# # Collection of useful numPy snippets...

# #1)

# import numpy as np

# x = np.array([[1,2,3,4], [5,6,7,8]])
# y = np.array([[9,10,11,12], [13,14,15,16]])

# print(x.sum(axis=0)) # np.sum(x) for the entire array
# print(np.min(x)) # or x.min()
# print(x.max(axis=1))
# print(np.cumsum(y))
# print(np.corrcoef(y))
# print(y.std())

# #2)

# import numpy as np

# two_d = np.array([[1,2,3,4], [5,6,7,8]]) # 2 x 4
# one_d = np.array([[10]]) # 1
# three_d = np.ones((3, 2)) # 3 x 2

# print(np.add(two_d,one_d))

# print(np.add(one_d, three_d))

# #3)

# import numpy as np

# x = np.arange(8) # 0 1 2 3 4 5 6 7

# y = x[0:4] # no step
# print(y)

# z = x[6: ] # from element 6 on
# print(z)
# print(x[ :5])  # from 0 to element 5

# z[1] = 100
# print(x)

# # a = np.array([[10, 11, 12, 13],[20, 22, 23, 25]])
# # print(a[0:1, 1])
# # print(a[..., 1])
# # print(a[ : , 3])

# #4)

# # heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

# # ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

# # heights_and_ages = heights + ages
# # heights_and_ages_arr = np.array(heights_and_ages)
# # heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))

# # new_record = np.array([[180, 183, 190], [54, 50, 69]])
# # heights_and_ages_arr[:, 42:] = new_record
# # print(heights_and_ages_arr)

#FINAL

import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))

new_record = np.array([[180, 183, 190], [54, 50, 69]])
heights_and_ages_arr[:, 42:] = new_record
print(heights_and_ages_arr)


#END