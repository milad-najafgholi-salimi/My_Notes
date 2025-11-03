"""
In this algorithm, it dosn't compare values together; It's a non-comparison algorithm.
It reviews digit by digit a number, and try to put every digit in a specific group.
Radix (or base) is based on 10; Means works with numbers from 0 to 9.
It starts with units, tens, then hundreds an so on on digits in every number.
Usually uses algorithms like counting sort for sorting in every step because it's stable.
If we don't use stable sort, it could return wrong output.

Radix Sort can actually be implemented together with any other sorting algorithm as long as it is stable. 
This means that when it comes down to sorting on a specific digit, any stable sorting algorithm will work, such as
counting sort or bubble sort.
"""

# Radix sort using Counting sort as a subroutine:

def counting_sort(arr, exp): # exp = short for 'exponent'
    n = len(arr)
    output = [0] * n   # output array
    count = [0] * 10   # Digits 0-9
    
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    for i in range(n):
        arr[i] = output[i]
    
    
    
def radix_sort(arr):
    max_num = max(arr)
    # Apply counting sort for each digit
    exp = 1 # 1, 10, 100, ...
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


"""
*Radix Sort Time Complexity*

Big O Notation
O(n.k) --> This means that Radix Sort depends both on the values that need to be sorted n, and the number of digits in the highest value k.

A best case scenario for Radix Sort is if there are lots of values to sort, but the values have few digits. 
For example if there are more than a million values to sort, and the highest value is 999, with just three digits. 
In such a case the time complexity O(n⋅k) can be simplified to just O(n).

A worst case scenario for Radix Sort would be if there are as many digits in the highest value as there are values to sort. 
This is perhaps not a common scenario, but the time complexity would be O(n^2)in this case.

The most average or common case is perhaps if the number of digits k is something like k(n)=logn. If so, Radix Sort gets
time complexity O(n⋅logn). An example of such a case would be if there are 1_000_000 values to sort, and the values have 6 digits.
"""


# Example:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"Before sorting {arr}")
radix_sort(arr)
print(f"After sorting {arr}")