import numpy as np

arr = np.array([1, 2, 3, 4])
arr = arr.astype(float)
arr = arr.astype(np.float16)
print(arr.dtype)