import numpy as np


a = np.array((
    [
        [1, 4, 3],
        [5, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ],
    [
        [1, 2, 3],
        [5, 2, 3],
        [1, 2, 9],
        [1, 2, 3]
    ],
    [
        [1, 2, 3],
        [5, 2, 3],
        [1, 2, 9],
        [1, 2, 3]
    ],
    [[1, 2, 3],
        [5, 2, 3],
        [1, 2, 9],
        [1, 2, 3]],
    [[1, 2, 3],
        [5, 2, 3],
        [1, 2, 9],
        [1, 2, 3]],
    [[1, 2, 3],
        [10, 2, 3],
        [1, 7, 3],
        [1, 2, 3]]
))

x = np.argmax(a, axis=0)
# x = np.amax(a, axis=0)
print(
    # a,
    # np.argmax(a), # Returns index of max value, flatten array
    # np.argmax(a, axis=0), # Returns index of zero axis with the max value
    # np.argmax(a, axis=1), # Returns row index (first axis) with the max value, for every zero axis
    # Returns column index (second axis) with the max value, for every zero axis
    np.argmax(a, axis=2)
)
