# node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#class of Queue
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self):
        data = int(input("Enter the data to enqueue into the queue: "))
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued {data} into queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued {dequeued_node.data} from queue.")
        return dequeued_node.data

    def peek(self):
        if self.is_empty():
            print("Queue empty. Nothing to peek.")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue empty.")
            return
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# MAIN
queue = Queue()
while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Peek\n4. Display\n5. Exit")
    choice = int(input("Enter your choiice: "))
    
    if choice == 1:
        queue.enqueue()
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        front = queue.peek()
        if front is not None:
            print(f"Front element is {front}")
    elif choice == 4:
        queue.display()
    elif choice == 5:
        print("Exit.")
        break
    else:
        print("invalid please try again.")
