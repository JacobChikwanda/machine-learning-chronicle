import numpy as np

# How to slice array
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Print 2, 3, 4, 5
print(np1[1:5])

# Print from 4 till end
print(np1[3:])

# Print using negatives start counting from end
print(np1[-3: -1])

# Print steps
print(np1[1:5:2])

# Print steps on everything stepping by 2
print(np1[::2])

# Slice a 2D
np2d = np.array([
    [1, 2, 3, 4], # Row 1
    [5, 6, 7, 8] # Row 2
])

# print something
print(np2d[1, 2])

# Slice
# The first part means start from row 0 up to row 1
# The second part means print elements from 0 to 3

print(np2d[0: 1, 0: 3]) # [[1, 2, 3]]
print(np2d[0: 2, 0: 3]) # [[1, 2, 3] [5, 6, 7]]