# numpy.linalg.LinAlgError: Singular matrix

import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])


# [[-2.   1. ]
#  [ 1.5 -0.5]]
print(np.linalg.inv(arr))

print('-' * 50)

# -2.0000000000000004
print(np.linalg.det(arr))