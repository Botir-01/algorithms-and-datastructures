2.1-2
Rewrite the INSERTION-SORT procedure to sort into non-increasing instead of non-
decreasing order.

item_list = [31, 41, 59, 26, 41, 58]

// The INSERTION-SORT procedure
""" for j = 2 to A.length
        key = A[j]
        i = j - 1
        while i > 0 and A[i] "<" key
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
"""

def insertion_sort(array):
    // Sorting into non-increasing order
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] < key:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key
    return array


print(insertion_sort(item_list))