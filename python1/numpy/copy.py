import numpy as np
arr = np.array([[1, 2, 3, 4, 5]])
x = arr.copy()
arr[0, 0] = 42

print(arr)
print(x)


def say_hello(name):
    print(f"Hello {name}")


say_hello('yazak')




