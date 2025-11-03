"""
In this sorting algorithm, we need to create another array for counting how many there are of each value, beside of our main array.
Then we start counting and for exmaple if the first element is 2, so we must insert that element at index 2 as the value is but in the
counting array (not in main array) - At index 2, we should count, here we should add 1 at index 2 because we counted 2 once.

After counting a value, we can remove it, and count the next value. 

We continue like this untill all values are counted and the main array is empty.

Now we will recreate the elements from the initial array (counted array), and we will do it so that the elements are
ordered lowest to highest.

We do the reverse process (insert values from counting array base on the quantity on main array) on the counting array untill
all elements become 0.
"""

def counting_sort(arr):
    if not arr:  # if the array (or list) is empty, don't need to do anything and just return the array (or list).
        return arr                                                                         # print(bool([])) output will be: False
    
    max_val = max(arr)
    count = [0] * (max_val + 1)  # create a new array with 0 elements with lengh 'max_val + 1'
                                                    # test this to understand what's happend: print([0] * 5) output will be: [0, 0, 0, 0, 0]
    for num in arr:
        count[num] += 1
    arr[:] = []  # empty the main array
        
    for num, freq in enumerate(count):  # enumerate is a built-in function that works on an array (or list) and in every single step returns
                                                                                                            # index and value.
        arr.extend([num] * freq)  # extend method will add the values at the end of the array.
        
    return arr


"""
This algorithm is useful for arrays that have manay repeated values (The values must not be negetive) and we want to sort them.
It's easy to understand.



*Counting Sort Time Complexity*

Big O Notation

In general, time complexity for counting sort if O(n + k).

In a best case scenario, the range of possible different values k is very small compared to the number
of values n and counting sort has time complexity O(n).

But in a worst case scenario, the range of possible different values k is very big compared to the number of values n and
counting sort can have time complexity O(n^2) or even worse.
"""



# Example:

unsorted_arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sorted_arr = counting_sort(unsorted_arr)