import numpy as np
import time
import random
import statistics


def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    This function sorts x by looking at each pair in x to see if the pair is
    ordered. It has O(n^2) complexity.

    If the pair is ordred incorrectly, the function swaps their position.

    The following are for a vector of 100 random integers:
        Conditionals: ~1000
        Assignments: ~10000
    The following is for a vector of 100-1000 random integers:
        Average time complexity: O(n^2)
    """

    limit = len(x)                  ## Find out how many pairs to check

    if limit <= 1:
        return x

    flag = True                    ## Set up flag to know if sequence has any misordered pairs
    while flag:
        flag = False
        for i in range(0, limit - 1):
            if x[i] > x[i+1]:
                flag = True             ## Flag True if a misordered pair is found
                dum = x[i]
                x[i] = x[i+1]
                x[i+1] = dum

    assert all([x[i] <= x[i+1] for i in range(0,len(x)-1)])
    return x

def quicksort(x):
    """
    I'm sorting X through recursion. I split the array on a pivot point, remove
    the pivot from the data, then sort each element of the remaining array into
    an over_array and under_array, based on comparison to the pivot.

    These new arrays then get sent back through quicksort until there is only 1
    element left per array. This resulting tree of arrays is in the correct order
    and gets combined.

    ** This implementation runs into space problems because of the propogating
    tree **

    The following are for a vector of 100 random integers:
        Conditionals: ~1000
        Assignments: ~900
    The following is for a vector of 100-1000 random integers:
        Average time complexity: O(n*log(n))
    """
    def partition(x):

        if len(x) <= 1:
            return x

        pivot = x[0]
        x = x[1:]

        over_array = []
        under_array = []

        for z in x:
            if z < pivot:
                under_array.append(z)
            else:
                over_array.append(z)

        return partition(under_array) + [pivot] + partition(over_array)

    x = partition(x)

    assert all([x[i] <= x[i+1] for i in range(0,len(x)-1)])
    return x


## Time complexity for bubblesort/quicksort
vect_length = 100
num_iters = 1
time_vector = []

for i in range(0, num_iters):
    test_vector = [random.randrange(1,100) for i in range(0,vect_length)]

    start = time.time()
    quicksort(test_vector)
    end = time.time()

    time_vector.append(end - start)

print(statistics.mean(time_vector))
