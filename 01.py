import numpy as np


def sort_dist(arr1,arr2):
    # sort both arrays
    arr1.sort()
    arr2.sort()

    # compute total distance ie norm 1 of arrays difference
    dist = np.linalg.norm(arr2-arr1, ord=1)

    return(dist)


# Solve with real inputs
inputs=np.loadtxt('input_01.txt')
arr1 = inputs[:, 0]
arr2 = inputs[:, 1]

print(sort_dist(arr1, arr2))