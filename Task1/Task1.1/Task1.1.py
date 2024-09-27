## Task 1: Data Structures & Algorithms
#  1.1 Implement a Custom Data Structure
# - Objective: Develop a custom data structure to understand the underlying mechanics of common data structures.
# - Instructions:
#   - Step 1: Create a class called `LinkedList`. Implement methods like `insert_at_beginning`, `insert_at_end`, `delete_node`, and `find_node`. Ensure that your linked list handles edge cases like inserting into an empty list or deleting the only node in the list.
#   - Step 2: Implement a `Stack` using a linked list or an array. Include methods like `push`, `pop`, and `peek`.
#   - Step 3: Implement a `Queue` using a linked list or an array. Include methods like `enqueue`, `dequeue`, and `peek`.
#   - Step 4: Extend your data structure by implementing additional functionality, such as reversing the linked list or sorting the stack.
# - Expected Output: A set of classes representing the data structures with full functionality and proper handling of edge cases.
# - Complexity Analysis: 
#   - For each operation in your data structure, analyze and document the time and space complexity (e.g., O(1), O(n)).

# creating parameters required for a linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):      # initiating head
        self.head = head
    
    # Time Complexity: O(n) because we traverse to the end of the list for each insertion.
    # Space Complexity: O(1) as we are only using a few extra variables for insertion.
    def add(self, data):                # to insert data into the linked list
        nodes = data.split()
        for node_data in nodes:
            new = Node(node_data)
            if self.head:
                temp = self.head
                while temp.next:
                    temp = temp.next    # Traverse to the last node
                temp.next = new
            else:
                self.head = new
        return data

    def display_list(self):             # to print the list
    # Time complexity: O(n), where 'n' is the number of nodes in the linked list (one traversal).
    # Space complexity: O(1), as no extra space is required, only a temporary pointer is used.
        temp = self.head
        if temp is None:
            print("The list is empty")
            return
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def insert_beginning(self, new=None):     
    # Time Complexity: O(1) as we only modify the head pointer.
    # Space Complexity: O(1) since we are only using a new node.
        newNode = Node(new)
        newNode.next = self.head
        self.head = newNode

    def insert_end(self, new_data):
    # Time Complexity: O(n) since we must traverse to the end of the list.
    # Space Complexity: O(1) because we only need one additional node.
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_afternode(self, data, x):         # insert after the given node
    # Time complexity: O(n) in the worst case (where 'n' is the number of nodes).
    # Space complexity: O(1) since no extra space is used except for the new node.
        temp = self.head
        newnode = Node(data)
        while temp:
            if temp.data == x:
                newnode.next = temp.next
                temp.next = newnode
                print(f"Node {data} inserted after {x}.")
                return
            temp = temp.next
        print(f"{x} not found in the list.")

    def delete_node(self, nodedata):
    # Time complexity: O(n) in the worst case (where 'n' is the number of nodes).
    # Space complexity: O(1) since only a constant amount of extra memory is used.

        prev = None
        temp = self.head
        if temp is not None and temp.data == nodedata:          # handling edge cases
            print("\nThe head node is being deleted")
            self.head = temp.next
            return
        while temp:
            if temp.data == nodedata:
                if prev:
                    prev.next = temp.next
                print(f"{temp.data} is deleted from the list")     # to check how thw loop iterates
                return
            prev = temp
            temp = temp.next
        print("\nNode not found for deletion")

    def search_node(self, find_value):
    # Time Complexity: O(n) because we may need to search through the entire list to find the node.
    # Space Complexity: O(1) as no additional space is required.
        temp = self.head
        found = False      # initiating a boolean value to print if the value is not found
        while temp:
            if temp.data == find_value:
                found = True
                print(f"{find_value} is found in the list")
                return
            temp = temp.next
        print("Search not found")
        
    def reverse(self):
    # Time Complexity: O(n) as we traverse through the list once.
    # Space Complexity: O(1) because no extra space is required except for a few variables.
        prev = None
        prev = None
        current = self.head
        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        self.head = prev


# Stack using LinkedList
class StackLinkedList:
    def __init__(self):
        self.top = None
    
    def push(self, data):
    # Time Complexity: O(1) for each push operation.
    # Space Complexity: O(1) for each new node being added.
        nodes = data.split()
        for node_data in nodes:
            newnode = Node(node_data)
            newnode.next = self.top
            self.top = newnode

    def display_stack(self):
        if self.top is None:
            return "No Node is present"
        else:
            temp = self.top
            print("Current stack:", end=" ")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def pop(self):
    # Time Complexity: O(1) because we only remove the top node.
    # Space Complexity: O(1) as no extra space is used.
        if self.top is None:
            print("Empty stack")
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.data

    def peek(self):
    # Time Complexity: O(1) because we only access the top node.
    # Space Complexity: O(1) as we don’t use additional space.
        if self.top is None:
            print("Empty stack")
            return None
        return self.top.data
    
    def sort(self):
    # Time Complexity: O(n log n) because we use Python’s built-in `sort()` which is Timsort (O(n log n)).
    # Space Complexity: O(n) as we store the stack elements in a list.
        if self.top is None or self.top.next is None:     # edge case when both 1 node / no node
            print("Sorting is not possible")
            return
        sort_list = []
        temp = self.top
        while temp:
            sort_list.append(temp.data)
            temp = temp.next
        sort_list.sort()

        self.top = None
        for data in reversed(sort_list):
            self.push(data)
        return self.display_stack()


# Queue using LinkedList
class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
    # Time Complexity: O(1) for each enqueue operation.
    # Space Complexity: O(1) for each new node being added.
        values = data.split()
        for value in values:
            newnode = Node(int(value)) 
            if self.rear is None:
                self.front = self.rear = newnode
            else:
                self.rear.next = newnode
                self.rear = newnode
    
    def displayqueue(self):
        if self.front is None:
            print("Empty Queue")
            return
        temp = self.front
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def dequeue(self):
    # Time Complexity: O(1) because we remove the front node.
    # Space Complexity: O(1) as no extra space is used.
        if self.front is None:
            print("Empty Queue")
            return None
        removing_node = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removing_node.data
    
    def peek(self):
    # Time Complexity: O(1) because we only access the front node.
    # Space Complexity: O(1) as no additional space is used.
        if self.front is None:
            print("Empty Queue")
            return None
        print(f"The peek is {self.front.data}") 


def menu():
    while True:
        print("\nChoose Data Structure:")
        print("1. Linked List")
        print("2. Stack")
        print("3. Queue")
        print("4. Exit")
        
        choice = int(input("Choose an option: "))

        if choice == 1:
            linked_list_menu()
        elif choice == 2:
            stack_menu()
        elif choice == 3:
            queue_menu()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

def linked_list_menu():
    ll = LinkedList()
    while True:
        print("\nLinked List Operations:")
        print("1. Add Node")
        print("2. Display List")
        print("3. Insert at Beginning")
        print("4. Insert at End")
        print("5. Insert After Node")
        print("6. Delete Node")
        print("7. Search Node")
        print("8. Reverse List")
        print("9. Back to Main Menu")
        
        choice = int(input("Choose an option: "))

        if choice == 1:
            data = input("Enter the node value to add: ")
            ll.add(data)
            print(f"{data} ")
        elif choice == 2:
            ll.display_list()
        elif choice == 3:
            new_data = input("Enter the node value to insert at beginning: ")
            ll.insert_beginning(new_data)
            print(f"Node {new_data} inserted at the beginning.")
        elif choice == 4:
            new_data = input("Enter the node value to insert at end: ")
            ll.insert_end(new_data)
            print(f"Node {new_data} inserted at the end.")
        elif choice == 5:
            new_data = input("Enter the node value to insert: ")
            x = input("Enter the value after which to insert: ")
            ll.insert_afternode(new_data, x)
        elif choice == 6:
            nodedata = input("Enter the node value to delete: ")
            ll.delete_node(nodedata)
        elif choice == 7:
            find_value = input("Enter the value to search: ")
            ll.search_node(find_value)
        elif choice == 8:
            ll.reverse()
            print("Linked List reversed.")
        elif choice == 9:
            break
        else:
            print("Invalid option. Please try again.")

def stack_menu():
    stack = StackLinkedList()
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Sort")
        print("5. Display Stack")
        print("6. Back to Main Menu")

        choice = int(input("Choose an option: "))

        if choice == 1:
            data = input("Enter the node value to push: ")
            stack.push(data)
            print(f"Node {data} pushed to stack.")
        elif choice == 2:
            popped_value = stack.pop()
            if popped_value is not None:
                print(f"Popped value: {popped_value}")
        elif choice == 3:
            peek_value = stack.peek()
            if peek_value is not None:
                print(f"The Peek is: {peek_value}")
        elif choice == 4:
            print("Sorting Stack...")
            stack.sort()
        elif choice == 5:
            stack.display_stack()
        elif choice == 6:
            break
        else:
            print("Invalid option. Please try again.")

def queue_menu():
    queue = QueueLinkedList()
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Back to Main Menu")
        
        choice = int(input("Choose an option: "))

        if choice == 1:
            data = input("Enter the value to enqueue: ")
            queue.enqueue(data)
            print(f" {data} ")
        elif choice == 2:
            dequeued_value = queue.dequeue()
            if dequeued_value is not None:
                print(f"Dequeued value: {dequeued_value}")
        elif choice == 3:
            queue.peek()
        elif choice == 4:
            queue.displayqueue()
        elif choice == 5:
            break
        else:
            print("Invalid option. Please try again.")

# Running the menu
menu()
