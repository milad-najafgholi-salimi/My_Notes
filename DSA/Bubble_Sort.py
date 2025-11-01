"""
It does all the process in "Swap" form. Always swaps a pair of values till the end.

It looks at the two first values. Does the lowest value come first? If the answer is YES, then dosen't need to swap them. But if the answer is NO,
it will swap them and do this process two by two till the end and trys to put the biggest value at the end.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #Swap
    return arr

"""
It's simple and easy to understand. You just focus on an example like above and follow the process; Then you find out you
are understanding. It's just simple as that. 
Good job Milad joon.
"""


def bubble_sort_improved(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

"""
Imagine that an array almost sorted or completely sorted. So we can sort it in just one round so the extra process is not
necessary and will just repeat and slow our programm. So we can Improve it a little better like example above and is easy 
to understand it.
"""

"""
*Bubble Sort Time Complexity*

Big O Notation
O(n^2)
"""
# Example:

array = [5, 1, 4, 2, 8]
print(bubble_sort(array))
