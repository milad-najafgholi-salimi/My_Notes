"""
It's really simple and doesn't need extra explain.
"""

def linear_search(arr, target_value):
    for i in range(len(arr)):
        if arr[i] == target_value:
            return i
    return -1

"""
*Linear Search Time Complexity*

Big O Notation:
O(n)
"""


# Example:

array = [3, 7, 2, 9, 5]
target_value = 9

result = linear_search(array, target_value)

if result != -1:
    print(result)
else:

    print("Not found")
