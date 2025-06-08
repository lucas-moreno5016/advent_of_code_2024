import numpy as np

#  FIRST HALF OF THE PUZZLE

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

print('Answer to the first half of the puzzle:')
print(sort_dist(arr1, arr2))
print('  ')

# SECOND HALF OF THE PUZZLE


def similarity(arr1,arr2):
    # integers in arr1 ie arr1 without redundancies
    int1 = []
    for i in arr1:
        if i not in int1:
            int1.append(i)

    # for each integer in int1, get occurences in arr1 and arr2
    occ1 = np.array([ (arr1 == i).sum() for i in int1])
    occ2 = np.array([ (arr2 == i).sum() for i in int1])

    # print(int1)
    # print(occ1)
    # print(occ2)

    similarity = np.array(int1) @ (occ1 * occ2 )

    return(similarity)


print('Answer to the second half of the puzzle:')
print(similarity(arr1, arr2))
print('  ')