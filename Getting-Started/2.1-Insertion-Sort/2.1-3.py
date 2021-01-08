"""
Consider the searching problem:
Input: A sequence of n numbers A = [1, 2, ... n] and a value v.
Output: An index i such that v = A[i] or the special value NIL if v does not
appear in A.
Write pseudocode for linear search, which scans through the sequence, looking
for v. Using a loop invariant, prove that your algorithm is correct. Make sure that
your loop invariant fulfills the three necessary properties.

Answer:
    for i=1 to length(A)
        if v == A[i]
            return 'v is in the array'
    return 'NIL - v is not in the array'
"""


# Implementation of the linear search in Python p.l.
def linear_search(arr, num):
    for i in arr:
        if i == num:
            return f"{num} is in the array"
    return f"NIL = {num} is not in the array"


print(linear_search([1, 2, 3, 4, 5], 3))
