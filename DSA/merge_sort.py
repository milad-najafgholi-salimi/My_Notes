"""
1) Divide: We split array in half as we can.
2) Conquer (مرتب سازی): Sort Every single half.
3) Merge (ادغام): Add two sorted parts together until we have a sorted array again.

We divide array until have single element into array. Now we know that a single element in an array is sorted
because there isn't any other value to compare.
Then merge and sort one-by-one elements from each seperated half branch.
"""

def merge_sort(arr):
    if len(arr) <= 1: # if array's lengh is equals to or less than 1, no need to sorting.
        return arr
    
    mid = len(arr) // 2
    left_half = arr[ : mid]
    right_half = arr[mid : ]
    
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i : ])
    result.extend(right[j : ])
    
    return result




"""
I don't understand all of it very well. I have issues in some part of it.


*Merge Sort Time Complexity*

Big O Notation:
O(n*logn)
"""

# Merge Sort Without Recursion

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i : ])
    result.extend(right[j : ])
    
    return result
def merge_sort_2(arr):
    step = 1  # starting with sub-arrays of length 1
    length = len(arr)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i : i + step]
            right = arr[i + step : i + 2 * step]
            
            merged = merge(left, right)
            
            # place the merged array back into the original array
            for j, val in enumerate(merged):
                arr[i + j] = val
        
        step *= 2  # Double the sub-array length for the next iteration
    
    return arr


# Example:

unsorted_array = [3, 7, 6, -10, 15, 23.5, 55, -13]

sorted_array = merge_sort(unsorted_array)

sorted_array_2 = merge_sort_2(unsorted_array)