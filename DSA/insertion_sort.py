"""
It separates an array into two parts. Sorted part and Unsorted part. It takes the very first value and puts it into the sorted part. Then
continues and selects another value from Unsorted part and compare the value with values in the sorted part and insert it in the correct
sort. It works simply as that.
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n): # Starts from second value because we assume that the first value is sorted.
        insert_index = i
        current_value = arr.pop(i)
        for j in range(i - 1, -1, -1): # range(start[included], end[Not included], step[reduce])
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value) # arr.insert(the position we want to insert, the value we want to insert in the specific position)

"""
It's a little tricky to understand but it's not hard.
"""

def insertion_sort_improved(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i # we assume the value is in the correct position.
        current_value = arr[i] 
        for j in range(i - 1, -1, -1): # Now we start from the end and try to figure out where it should be.
            if arr[j] > current_value: # if the previous value "arr[j]" is greater than the current value:
                arr[j + 1] = arr[j]  # Here we make a place for it.
                insert_index = j
            else:
                break # will stops the inner loop. The outer loop will continue working.
        arr[insert_index] = current_value


"""
Like 'selection sort' algorithm, We have shifting problem here too. So we need to improve it and it's easy to do that like we did in 'selection sort' algorithm.
It's really easy but if you confused, just try to solve it with an example, and you easily will find out (the tricky part is i and j;
If you understand them, you understand all of it.) .



*Insertion Sort Time Complexity*

Big O Notation
O(n^2)
"""

# Example:
array = [64, 34, 25, 12, 22, 11, 90, 5]
insertion_sort_improved(array)