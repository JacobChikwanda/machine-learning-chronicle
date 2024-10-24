import numpy as np

# 1d
np1 = np.array([9, 2, 4, 6, 1, 3, 5, 9])
filter_1 = np1 % 2 == 0
filter_2 = np1 > 5
print(np1[filter_2])