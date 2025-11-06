"""
A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.

Basic operations we can do on a queue are:

* /Enqueue/ - Adds a new element to the queue.
* /Dequeue/ - Removes and returns the first (front) element from the queue.
* /Peek/ - Returns the first element in the queue.
* /isEmpty/ - Checks if the queue is empty.
* /Size/ - Finds the number of elements in the queue.


Queues can be implemented by using arrays or linked lists.
"""

# Using a Python list as a queue:


queue = []

#Enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print(f"Queue: {queue}")

#Peek
front_element = queue[0]
print(f"Peek: {front_element}")

#Dequeue
popped_element =queue.pop(0)
print(f"Dequeue: {popped_element}")

print(f"Queue after Dequeue: {queue}")

#isEmpty
isEmpty = not bool(queue)
print(f"isEmpty: {isEmpty}")

#Size
print(f"Size: {len(queue)}")




# Using a Python class as a queue:
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Create a queue

my_queue = Queue()

my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")

print(f"Queue: {my_queue.queue}")
print(f"Peek: {my_queue.peek()}")
print(f"Dequeue: {my_queue.dequeue}")
print(f"Queue after Dequeue: {my_queue.queue}")
print(f"isEmpty: {my_queue.isEmpty()}")
print(f"Size: {my_queue.size()}")




"""
Creating a Queue using a Linked List:
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def print_queue(self):
        temp = self.front
        while temp:
            print(temp.data, end = " -> ") 
            temp = temp.next
        print()


# Create a queue
my_queue = Queue()

my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")

print("Queue: ", end="")
my_queue.print_queue()
print("Peek: ", my_queue.peek())
print("Dequeue: ", my_queue.dequeue())
print("Queue after Dequeue: ", end="")
my_queue.printQueue()
print("isEmpty: ", my_queue.isEmpty())
print("Size: ", my_queue.size())