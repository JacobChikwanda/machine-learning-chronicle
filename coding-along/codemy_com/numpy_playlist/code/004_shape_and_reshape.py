import numpy as np

np1 = np.array([1, 2, 3, 4, 5, 6])

# How to make 2d
np1 = np1.reshape(3, 2)
# print(np1)

# How to make 3d
np1 = np1.reshape(1, 3, 2)
# print(np1)

# Flatten
np1 = np1.reshape(-1)
print(np1)