# =================================Insertion=Sort============================
""" The algorithm is efficient for sorting a small number of elements

Pseudocode:
for j = 2 to A.length // an array starts with 1 index
    key = A[j]
    // Insert A[j] into the sorted sequence A[1...j-1]
    i = j - 1
    while i>0 and A[i]>key
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key """

unsorted_list = [54, 421, 1, 4, 5, 653, 42]


# Implementation of Insertion sort algorithm in Python p.l.
def insertion_sorting(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


print(insertion_sorting(unsorted_list))



