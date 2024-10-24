import numpy as np

# How to create simple numpy arrays
manual_np_list = np.array([0, 1, 2, 3, 4])
auto_np_list = np.arange(5)

zeros_np_list = np.zeros(5) # Creates a numpy array list of zeros.
fives_np_list = np.full(5, 5) # Creates a numpy array list of fives 
stepped_np_list = np.arange(0, 5, 2) # Starts numpy list at 0 steps it up by 2 and stops at 5

# How to create multidimension arrays
zeros_np_list_2d = np.zeros((2, 5))
fives_np_list_2d = np.full((2, 5), 5)
stepped_np_list_2d = np.arange(0, 100, 2)
stepped_np_list_2d = stepped_np_list_2d.reshape(5, -1)

# How to get some information about the array
rows, columns = stepped_np_list_2d.shape

# How to convert list to numpy array
my_simple_list = [1, 2, 3, 4, 5]
my_2nd_simple_list = [{ "Name": "Jacob" }, { "Name": "Jacob" }]
my_medium_simple_list = [1, "2", 3]
my_uncovertable_list = [1, "hello", [{ "Name": "Jacob" }]] # try to convert this one it will throw an error with inhomogeneous shape

converted_python_list = None

try:
    converted_python_list = np.array(my_uncovertable_list)
except Exception as e:
    print(f"Cant convert list because: {e}")

# print above lists here
print(converted_python_list)

# How to access elements
for i in range(rows):
    single_array = stepped_np_list_2d[i]
    print(single_array)
    for element in single_array:
        print(f"\t{element}")
