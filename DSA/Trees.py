"""
I wrote very complete about Trees and their priorities in my 'DSA' Notebook.
"""

"""
Binary Trees: Each node has up to two children, the left child node and the right child node. 
This structure is the foundation for more complex tree types like Binay Search Trees and AVL Trees.

Binary Search Trees (BSTs): A type of Binary Tree where for each node, the left child node has a 
lower value, and the right child node has a higher value.

AVL Trees: A type of Binary Search Tree that self-balances so that for every node, the difference in height between the left
and right subtrees is at most one. This balance is maintained through rotations when nodes are inserted or deleted.




Benefits of Trees over Arrays and Linked Lists:


Arrays are fast when you want to access an element directly, like element number 700 in an array of 1000 elements for example. 
But inserting and deleting elements require other elements to shift in memory to make place for the new element, or to
take the deleted elements place, and that is time consuming.

Linked Lists are fast when inserting or deleting nodes, no memory shifting needed, but to access an element inside the list, the
list must be traversed, and that takes time.

Trees, such as Binary Trees, Binary Search Trees and AVL Trees, are great compared to Arrays and Linked Lists because they
are BOTH fast at accessing a node, AND fast when it comes to deleting or inserting a node, with no shifts in memory needed.
"""