import numpy as np

np1 = np.array([1, 2, 3])
np2 = np1.copy()

print(f"Original before change: {np1}")
print(f"Copy before change: {np2}")

new_value = int(input("Enter new value for first element: "))
print("\nUpdating original\n")
np1[0] = new_value

print(f"Original after change: {np1}")
print(f"Copy after change: {np2}\n-----------[END OF COPY]-----------\n\n")

view_np1 = np.array([10, 20, 30])
view_np2 = view_np1.view()

print(f"Original before change: {view_np1}")
print(f"View before change: {view_np2}")

new_value = int(input("Enter new value for orginal element at 0: "))
print("\nUpdating original\n")
view_np1[0] = new_value

print(f"Original after change: {view_np1}")
print(f"Copy after change: {view_np2}\n\n")

new_value = int(input("Enter new value for view element at 0: "))
print("\nUpdating original\n")
view_np2[0] = new_value

print(f"Original after change: {view_np1}")
print(f"Copy after change: {view_np2}")