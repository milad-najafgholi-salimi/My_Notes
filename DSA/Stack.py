"""
A stack is a linear data structure that follows the /Last-In-First-Out (LIFO)/ principle.


Basic operation we can do on a stack are:

* /Push/ - Adds a new element on the stack
* /Pop/ - Removes and returns the top element from the stack.
* /Peek/ - Returns the top (last) element on the stack.
* /isEmpty/ - Checks if the stack is empty.
* /Size/ - Finds the number of elements in the stack.


Stacks can be implemented by using arrays or linked lists.

Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in
graphs, or for backtracking.
"""

# Simple stack code using lists

stack = []

# Push
stack.append("A")
stack.append("B")
stack.append("C")
print(f"Stack: {stack}")


# Peek
top_element = stack[-1]
print(f"Peek: {top_element}")


# Pop
popped_element = stack.pop()
print(f"Pop: {popped_element}")


# Stack after Pop
print(f"Stack after Pop: {stack}")


# isEmpty
is_empty = not bool(stack)
print(f"isEmpty: {is_empty}")


# Size
print(f"Size: {len(stack)}")




"""
While Python lists can be used as stacks, creating a dedicated "Stack class" provides better encapsulation and additional functionality:
"""

# Better stack code using classes (still using lists)

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
# Create a stack
my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")

print(f"Stack: {my_stack.stack}")
print(f"Pop: {my_stack.pop()}")
print(f"Stack after pop: {my_stack.stack}")
print(f"Peek: {my_stack.peek()}")
print(f"isEmpty: {my_stack.isEmpty()}")
print(f"Size: {my_stack.size()}")





"""
*Stack Implementation using Linkded Lists*
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # next is a built-in function (that uses iterator)
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def stack_size(self):
        return self.size
    
    def traverse_and_print(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print()

my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")

print(f"Linked List: ", end="")
my_stack.traverse_and_print()

print(f"Peek: {my_stack.peek()}")
print(f"Pop: {my_stack.pop()}")
print(f"Linked List after Pop: ", end="")
my_stack.traverse_and_print()
print(f"isEmpty: {my_stack.isEmpty()}")
print(f"Size: {my_stack.stack_size()}")