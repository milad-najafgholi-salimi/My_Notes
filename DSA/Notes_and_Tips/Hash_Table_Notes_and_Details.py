"""
Choosing the modulus:
    If you know exactly the number of buckets, for example if you know you have 10 buckets, 
    then you should use "%10" unless you should use: 
        number_of_buckets = len(arr)
    Which means you should use: 
        " % len(arr) ".
"""


"""
Point: You can use the following code:
        hash_table = [[]] * 3
        
        output: [[], [], []]
        
        hash_table[0] = 1
        print(hash_table)
        
        output: [1, [], []]
    It still looks correct.
    
    but now look at this:
        hash_table = [[]] * 3
        print(hash_table)

        hash_table[0].append(7)
        print(hash_table)
        
        output: [[7], [7], [7]]
        
    Why multiplication (*) doesn't work:
        [*] * n copies references, not the objects themselves.
"""

def hash_sort(arr):
    n = len(arr)
    hash_table = []
    for i in range(n):
        hash_table.append([])
    
    for value in arr:
        index = value % n
        hash_table[index].append(value)
    
    # After above code, hash_table could be like this for example: hash_table = [[], [7, 17], [], [3], [], [22, 12]]
    result = []
    for bucket in hash_table:
        for value in sorted(bucket): # 'sorted()' is a built-in function. The sorted() function returns a sorted list of the specified iterable object.
            result.append(value)        # which means it iterate on every hash_table element and sort them into its new sorted list. So it's gathering all sorted buckets into a sorted list.
            # We take each value from sorted bucket and put it into the final list.
    return result

# Example:
arr = [22, 3, 5, 21, 19, 18, 1]
print(hash_sort(arr))

# Note: Hash Table isn't good for sorting. It's good for inserting, searching and deleting.