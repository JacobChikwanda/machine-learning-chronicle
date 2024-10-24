import numpy as np

# 3d array
np_3d = np.array([[[1, 2],[3,4]]])
print(np_3d)
for item in np.nditer(np_3d):
    print(item)