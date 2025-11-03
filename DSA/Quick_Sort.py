"""
As the name suggests, Quicksort is one of the fastest sorting algorithms.
It's hard to explain for myself, but is kinda easy to understand. 
"""

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i] # swap
            
    array[i + 1], array[high] = array[high], array[i + 1] # swap
    return i + 1    # returns the ultimate pivot position


def quicksort(array, low = 0, high = None):
    if high is None:
        high = len(array) - 1
        
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

     
"""
It's tricky and hard for me to fully understand it. 
I try to get a little help from Chat-GPT to explain it for me in simple words.

It says:

1) First you need select a value number as the pivot. For example the last value in the array.

2) Then the algorithm divides the array into two partition base on selected pivot: 
   @ The values that are less than or equal ( '<=' ) to the pivot 
        and
   @ the values that are greater than ( '>' ) the pivot
   
After this process, the pivot will be in the correct position.

3) Now we repeat 2 previous process for each left and righ partition. After all the array will sort completely.


*Quick Sort Time Complexity*

Big O Notation
The worst case scenario for Quicksort is O(n^2). 
This is when the pivot element is either the highest or lowest value in every sub-array, which leads to a lot of recursive calls.
With our implementation above, this happens when the array is already sorted.

But on average, the time complexity for Quicksort is actually just O(n log n), which is a lot better than for the previous sorting algorithms.
That is why Quicksort is so popular.
""" 

     
# Example:
   
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)