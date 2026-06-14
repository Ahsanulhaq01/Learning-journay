import numpy as np
import sys
import time
import math
# arr = np.array([[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]],dtype=np.int32)

# arr1 = np.array([1,2,3,4],dtype=np.float128)
# print(arr1.itemsize)
# print(arr1.dtype)
# arr1 = arr.copy()
# print(arr1)
# print(arr)
# print(type(arr))


# print(np.zeros((4,4)))
# print(np.ones((5,5)))

# print(np.identity(6))
# print(np.arange(4,51,2))

# print(np.linspace(10,20,10))

# print(arr.size)

# lst = range(1000000)

# print()

# lst_memory = sys.getsizeof(0) * len(lst)

# arr = np.arange(1000000)

# numpy_arrmemory = arr.itemsize * arr.size


# # differ = lst_memory - numpy_arrmemory
# differ = (numpy_arrmemory - lst_memory)* -1

# print(differ)


# a = range(100000)
# b = range(100000)
# start = time.time()
# lst = [a + b for a,b in zip(a,b)]
# end = time.time()
# print(f"Time execution is : {end - start}")
# arr1 = np.arange(100000)
# arr2 = np.arange(100000)
# start = time.time()
# c = arr1 + arr2
# end = time.time()
# print(f"The time difference is : {end - start}")

# arr = np.arange(24).reshape(6,4)
# print(arr)
# print()
# # print(arr[:1])

# print(arr[:,2:4]) 

# arr = np.arange(24).reshape(6,4)
# print(arr)

# np.median(arr)

# arr = np.arange(24).reshape(6,4)
# print(arr)
# print(arr.max(axis=0))
# print(arr.max(axis=1))
# print(arr.sum(axis=1))
# # print(np.sin(arr))

# arr1 = np.arange(24).reshape(6,4)

# print(np.transpose(arr1))

print(np.hstack((arr,arr1)))
# print(e)