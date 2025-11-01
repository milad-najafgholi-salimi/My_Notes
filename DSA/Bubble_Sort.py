"""
It finds BIGGEST value in an array and insert it in the end of the array. In simple words it sorts from BIGGEST to LOWEST.
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