"""
It's really easy to completely understand; It works on a sorted list (or array); It gets a value that you want to find and goes to the list
and check the mid number in the list is less than or greater than or equal to the target value. 
This algorithm is really fast.
"""

def binary_search(arr, target_value):
    left = 0 # First index
    right = len(arr) - 1 # Last index
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target_value:
            return mid
        
        if arr[mid] < target_value:
            left = mid + 1  # Go to the right part 
        else:
            right = mid - 1 # Go to the left part
    
    return -1

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
my_target = 15

result = binary_search(array, my_target)

if result != -1:
    print(f"Value {my_target} found at index {result}")
else:
    print("Not found")
    
    
"""
*Binary Search Time Complexity*

Big O Notation:
O(logn)

remember Binary Search log is on base 2.
"""