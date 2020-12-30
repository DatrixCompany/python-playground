import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])  # i1 -> i5 (not including)
print(arr[4:])  # i4 -> end
print(arr[-3:-1])  # i-3 (3 from the end) -> i-1
print(arr[1:5:2])  # i1 -> i5 step by 2 (default 1)
print(arr[::2])  # any other element (step by 2)

arr2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr2D[1:2, 1:4])
