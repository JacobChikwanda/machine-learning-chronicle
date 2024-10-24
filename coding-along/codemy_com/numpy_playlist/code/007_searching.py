import numpy as np

# 1d
np1 = np.array([9, 2, 4, 6, 1, 3, 5, 9])
res = np.where(np1 == 9)

# 2d
np_2d = np.array([["Job", "Alex"], ["Zebra", "Elephant"]])
res = np.where(np_2d == "Job")
print(res)