# node clas
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class
class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self):
        data = int(input("Enter the data to push onto the stack: "))
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Pushed {data} onto stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_node = self.head
        self.head = self.head.next
        print(f"Popped {popped_node.data} from stack.")
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print("Stack empty. Nothing to peek.")
            return None
        return self.head.data

    def display(self):
        if self.is_empty():
            print("Stack empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# MAIN
stack = Stack()
while True:
    print("\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        stack.push()
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        top = stack.peek()
        if top is not None:
            print(f"Top element is {top}")
    elif choice == 4:
        stack.display()
    elif choice == 5:
        print("Exit.")
        break
    else:
        print("Invalid please try again.")
