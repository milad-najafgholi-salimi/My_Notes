"""
Goes through the array, one value at a time. Finds the LOWEST value and inserts it at the beginning. Next time skips the
first value that found as the lowest value, and do the same work with other values till there aren't any value left to check.
"""
# Do code here
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)



"""
It's pretty easy and obvious. You should focus and look carefully and you will learn completely and will find it really easy.
I promise you.
"""


def selection_sort_improved(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] #swap


"""
In "Selection Sort" we need to remove the LOWEST value and insert it at the beginning of the array. So we have shifting
problems here and these shifting will slow our program. So we can improve our selection sort program a little more. We just
need to swap the values instead of deleting and inserting.

I really recommend the second one, which is "selection_sort_improved". It's really easier and better.



*Selection Sort Time Complexity*

Big O Notation
O(n^2)
"""


# Example:

array = [64, 25, 12, 22, 11]
selection_sort(array)