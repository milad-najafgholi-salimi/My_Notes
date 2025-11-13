"""
The AVL Tree is a type of Binary Search Tree named after two Soviet inventors Georgy Adelson-Velsky and Evgenii Landis who 
invented the AVL Tree in 1962.

AVL trees are self-balancing, which means that the tree height is kept to a minimum so that a very fast runtime is 
guaranteed for searching, inserting and deleting nodes, with time complexity O(logn).
"""

"""
The only difference between a regular Binary Search Tree and an AVL Tree is that AVL Trees do rotation 
operations in addition, to keep the tree balance.

A Binary Search Tree is in balance when the difference in height between left and right subtrees is less than 2.

By keeping balance, the AVL Tree ensures a minimum tree height, which means that search, insert, and delete operations can be done really fast.
"""


"""
The "Balance Factor" (BF) for a node (X) is the difference in height between its right and left subtrees.
        BF(X) = height(right_subtree(X)) - height(left_subtree(X))

Balance factor values:
    * 0: The node is in balance.
    * more than 0: The node is "right heavy".
    * less than 0: The node is "left heavy".

If the balance factor is less than -1, or more than 1, for one or more nodes in the tree, the tree is considered not in 
balance, and a rotation operation is needed to restore balance.
"""



"""
The Four "out-of-balance" Cases

Left-Left (LL) --> The unbalanced node and its left child node are both left-heavy.   Rotation to Restore Balance: A single right rotation
Right-Right (RR) --> The unbalanced node and its right child node are both right-heavy.     A single left rotation
Left-Right (LR) -->  The unbalanced node is left heavy, and its left child node is right heavy.     First do a left rotation on the left child node, then do a right rotation on the unbalanced node.
Right-Left (RL) -->  The unbalanced node is right heavy, and its right child node is left heavy.    First do a right rotation on the right child node, then do a left rotation on the unbalanced node.
"""



"""
ALV Tree Implementation in Python
"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:  # node is false when it's empty or None. 
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0 
    return get_height(node.left) - get_height(node.right)

def right_rotate(y):
    print("Rotate right on node", y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def left_rotate(x):
    print("Rotate left on node", x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.left))
    return y

def insert(node, data):
    if not node:
        return TreeNode(data)
    
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
        
    # Update the balance factor and balance the tree
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)
    
    # Balancing the tree
    # Left Left
    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)
    
    # Left Right
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    
    # Right Right
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)
    
    # Right Left
    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    
    return node

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=", ")
    in_order_traversal(node.right)
    
# Inserting nodes
root = None
letters = ["C", "B", "E", "A", "D", "H", "G", "F"]
for letter in letters:
    root = insert(root, letter)
    
in_order_traversal(root)




"""
AVL Delete Node Implementation
"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        
def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert(node, data):
  if not node:
    return TreeNode(data)

  if data < node.data:
    node.left = insert(node.left, data)
  elif data > node.data:
    node.right = insert(node.right, data)

  # Update the balance factor and balance the tree
  node.height = 1 + max(get_height(node.left), get_height(node.right))
  balance = get_balance(node)

  # Balancing the tree
  # Left Left
  if balance > 1 and get_balance(node.left) >= 0:
    return right_rotate(node)

  # Left Right
  if balance > 1 and get_balance(node.left) < 0:
    node.left = left_rotate(node.left)
    return right_rotate(node)

  # Right Right
  if balance < -1 and get_balance(node.right) <= 0:
    return left_rotate(node)

  # Right Left
  if balance < -1 and get_balance(node.right) > 0:
    node.right = right_rotate(node.right)
    return left_rotate(node)

  return node

def in_order_traversal(node):
  if node is None:
    return
  in_order_traversal(node.left)
  print(node.data, end=", ")
  in_order_traversal(node.right)
    
def min_value_node(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

def min_value_node(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

def delete(node, data):
  if not node:
    return node

  if data < node.data:
    node.left = delete(node.left, data)
  elif data > node.data:
    node.right = delete(node.right, data)
  else:
    if node.left is None:
      temp = node.right
      node = None
      return temp
    elif node.right is None:
      temp = node.left
      node = None
      return temp

    temp = min_value_node(node.right)
    node.data = temp.data
    node.right = delete(node.right, temp.data)

  if node is None:
    return node

  # Update the balance factor and balance the tree
  node.height = 1 + max(get_height(node.left), get_height(node.right))
  balance = get_balance(node)

  # Balancing the tree
  # Left Left
  if balance > 1 and get_balance(node.left) >= 0:
    return right_rotate(node)

  # Left Right
  if balance > 1 and get_balance(node.left) < 0:
    node.left = left_rotate(node.left)
    return right_rotate(node)

  # Right Right
  if balance < -1 and get_balance(node.right) <= 0:
    return left_rotate(node)

  # Right Left
  if balance < -1 and get_balance(node.right) > 0:
    node.right = right_rotate(node.right)
    return left_rotate(node)

  return node

# Inserting the letters
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
  root = insert(root, letter)

in_order_traversal(root)
print('\nDeleting A')
root = delete(root,'A')
in_order_traversal(root)




"""
The BST is not self-balancing. This means that a BST can be very unbalanced, almost like a long chain, where the height is 
nearly the same as the number of nodes. This makes operations like searching, deleting and inserting nodes slow, 
with time complexity O(h)=O(n).

The AVL Tree however is self-balancing. That means that the height of the tree is kept to a minimum so that operations like searching, 
deleting and inserting nodes are much faster, with time complexity O(h)=O(logn).
"""