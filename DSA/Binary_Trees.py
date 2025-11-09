"""
A Binary Tree is a type of tree data structure where each node can have a maximum of two child nodes, a left child node and a right child node.

Hey Milad. Check your DSA notebook. You wrote about these things there completely.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG


# Example:
print(f"root.right.left.data: {root.right.left.data}")
"""
root.right.left.data ---> root.right = nodeB , nodeB.left = nodeE , nodeE.data = E [From: nodeE = TreeNode("E")]
"""




"""
Types of Binary Trees:

* A balanced Binary Tree has at most 1 in difference between its left and right subtree heights, for each node in the tree.

* A complete Binary Tree has all levels full of nodes, except the last level, which is can also be full, or filled from left to right. The properties of a complete Binary Tree means it is also balanced.

* A full Binary Tree is a kind of tree where each node has either 0 or 2 child nodes.

* A perfect Binary Tree has all leaf nodes on the same level, which means that all levels are full of nodes, and all internal nodes have two child nodes.The properties of a perfect Binary Tree means it is also full, balanced, and complete.
"""




"""
Binary Tree Traversal:

Going through a Tree by visiting every node, one node at a time, is called traversal.
Since Arrays and Linked Lists are linear data structures, there is only one obvious way to traverse these: start at the first element, or node, and continue to visit the next until you have visited them all.
But since a Tree can branch out in different directions (non-linear), there are different ways of traversing Trees.



There are two main categories of Tree traversal methods:

* Breadth First Search (BFS) is when the nodes on the same level are visited before going to the next level in the tree. This means that the tree is explored in a more sideways direction.

* Depth First Search (DFS) is when the traversal moves down the tree all the way to the leaf nodes, exploring the tree branch by branch in a downwards direction.


There are three different type of DFS traversals:
* Pre-order
* in-order
* post-order
"""




"""
Pre-order Traversal of Binary Trees:

Pre-order Traversal is a type of Depth First Search, where each node is visited in a certain order.

Pre-order Traversal is done by visiting the root node first, then recursively do a pre-order traversal of the left subtree, followed by a recursive pre-order traversal of the right subtree.

This traversal is "pre" order because the node is visited "before" the recursive pre-order traversal of the left and right subtrees.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node is None:
        return 
    print(node.data, end=", ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
pre_order_traversal(root)




"""
In-order Traversal of Binary Trees:

In-order Traversal is a type of Depth First Search, where each node is visited in a certain order.

In-order Traversal does a recursive In-order Traversal of the left subtree, visits the root node, and finally, does 
a recursive In-order Traversal of the right subtree. This traversal is mainly used for Binary Search Trees where it 
returns values in ascending order.

What makes this traversal "in" order, is that the node is visited in between the recursive function calls. The node 
is visited after the In-order Traversal of the left subtree, and before the In-order Traversal of the right subtree.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=", ")
    in_order_traversal(node.right)
    
root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
in_order_traversal(root)





"""
Post-order Traversal of Binary Trees:

Post-order Traversal is a type of Depth First Search, where each node is visited in a certain order.

Post-order Traversal works by recursively doing a Post-order Traversal of the left subtree and the right subtree, followed 
by a visit to the root node. It is used for deleting a tree, post-fix notation of an expression tree, etc.

What makes this traversal "post" is that visiting a node is done "after" the left and right child nodes are called recursively.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def post_order_traversal(node):
    if node is None:
        return 
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end=", ")
    
root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
post_order_traversal(root)