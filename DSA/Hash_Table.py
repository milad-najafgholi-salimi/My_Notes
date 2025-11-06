"""
A Hash Table is a data structure designed to be fast to work with.

The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because 
searching for, adding, and deleting data can be done really quickly, even for large amounts of data.


In a Linked List, finding a person "Bob" takes time because we would have to go from one node 
to the next, checking each node, until the node with "Bob" is found.

And finding "Bob" in an list/array could be fast if we knew the index, but when we only 
know the name "Bob", we need to compare each element and that takes time.

With a Hash Table however, finding "Bob" is done really fast because there is a way to go directly to 
where "Bob" is stored, using something called a hash function.
"""



"""
Building A Hash Table
"""
# Step 1 - Create an Empty List
my_list = [None, None, None, None, None, None, None, None, None, None]

"""Each of These elements is called a /bucket/ in a Hash Table"""

# Step 2 - Create a Hash Function
def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char) # ord() function is a built-in Python function that converts a Unicode character to its corresponding integer Unicode code point value.
                                  # It essentially performs the opposite operation of the chr() function, which converts an integer to its Unicode Character.
    return sum_of_chars % 10

print(f"\"Milad\" has hash code: {hash_function("Milad")}") 
"""
In this exmaple "Milad" has the following unicode numbers (ASCII):
* "M" -> 77
* "i" -> 105
* "l" -> 108
* "a" -> 97
* "d" -> 100

In this example we will sum all these values and modulus to 10:
77 + 105 + 108 + 97 + 100 = 487
487 % 10 = 7

So "Milad" should be sorted at index 7.

The number returned by the hash function is called the /hash code/.
"""


"""
Unicode number: Everything in our computers are stored as numbers, and the Unicode code number is a
unique number that exist for every character. For example, the character A has Unicode number 65.
"""

# Step 3 - Inserting an Element
def add(name):
    index = hash_function(name)
    my_list[index] = name

add("Milad")
print(my_list)



# Step 4 - Looking up a name
def contains(name):
    index = hash_function(name)
    return my_list[index] == name

print(f"\"Milad\" is in the Hash Table: {contains("Milad")}")

"""
Because we do not have to check element by element to find out if "Pete" is in there, we can just 
use the hash function to go straight to the right element!
"""



# Step 5 - Handling collisions
"""
Let's also add "Nadia" to our Hash Table.

We give "Nadia" to our hash function, which returns 3, meaning "Nadia" should be stored at index 3.

Trying to store "Nadia" in index 3, creates what is called a collision, because "Milad" is already stored at index 3.

To fix the collision, we can make room for more elements in the same bucket. Solving the collision problem
in this way is called chaining, and means giving room for more elements in the same bucket.

Start by creating a new list with the same size as the original list, but with empty buckets, then rewrite the add() function:
"""
my_list = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]


def add(name):
    index = hash_function(name)
    my_list[index].append(name)

add("Milad")
add("Nadia")
add("Faraz")
add("Mehrdad")
add("Jadi")
print(my_list)


"""
The most important reason why Hash Tables are great for these things is that Hash Tables are very fast 
compared Arrays and Linked Lists, especially for large sets. Arrays and Linked Lists have 
time complexity O(n) for search and delete, while Hash Tables have just O(1) on average.
"""