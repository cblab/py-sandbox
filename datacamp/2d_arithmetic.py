'''
import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

print(np_mat * 2)

print(np_mat + np.array([10, 10]))

print(np_mat + np_mat)
'''

baseball = [[1, 2, 3],[3, 4, 5],[5, 6, 7]]
updated = [[76.09349925,  209.23890778,   26.19]]

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print (baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)