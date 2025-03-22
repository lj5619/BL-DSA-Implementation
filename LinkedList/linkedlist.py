class Node:

    def __init__(self,data):
        """
        Description:
            Constructor to initialize the node value and reference
        Parameters:
            self,data
        Return:
            None
        """
        self.data = data
        self.nextref = None

class LinkedList:

    def __init__(self):
        """
        Description:
            Constructor to initialize head value
        Parameters:
            self
        Return:
            None
        """
        self.head = None

    def insert_at_start(self,value):
        """
        Description:
            Function to insert node at start of linked list
        Parameters:
            self,value
        Return:
            None
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nextref = self.head
            self.head = new_node

    def insert_at_end(self,value):
        """
        Description:
            Function to insert node at end of linked list
        Parameters:
            self,value
        Return:
            None
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.nextref:
            current_node = current_node.nextref
        current_node.nextref = new_node

    def insert_at_location(self,target,value):
        """
        Description:
            Function to insert node at a specific location in linked list   
        Parameters:   
            self,target,value
        Return:
            None
        """ 

        if self.head is None:
            print("List is empty.")
            return
        position = input(f"{value} to be added to left or right of {target}?: ")        
        if position.lower() == 'left':
            if self.head.data == target:
                self.insert_at_start(value)
                return
            current_node = self.head
            while current_node.nextref:
                if current_node.nextref.data == target:
                    new_node = Node(value)
                    new_node.nextref = current_node.nextref
                    current_node.nextref = new_node
                    return
                current_node = current_node.nextref
        elif position.lower() == 'right':
            current_node = self.head
            while current_node:
                if current_node.data == target:
                    new_node = Node(value)
                    new_node.nextref = current_node.nextref
                    current_node.nextref = new_node
                    return
                current_node = current_node.nextref
            print(f"{target} is not in this list")
        else:
            print("Invalid position")
            return

    def delete_first(self):
        """
        Description:
            Function to delete node at start of linked list
        Parameters:
            self
        Return:
            None
        """
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.nextref

    def delete_last(self):
        """
        Description:
            Function to delete node at end of linked list
        Parameters:
            self
        Return:
            None
        """ 
        if self.head is None:
            print("List is empty")

        if self.head.nextref is None:
            self.head = None
            return
        
        current_node = self.head
        while current_node.nextref and current_node.nextref.nextref:
            current_node = current_node.nextref
        current_node.nextref = None

    def delete_value(self, value):
        """
        Description:
            Function to delete node with specific value in linked list
        Parameters:
            self,value
        Return:
            None
        """
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            self.head = self.head.nextref 
            return
        current_node = self.head
        while current_node.nextref:
            if current_node.nextref.data == value:
                current_node.nextref = current_node.nextref.nextref 
                return
            current_node = current_node.nextref
        print(f"Value {value} is not in this list")

    def get_first(self):
        """
        Description:
            Function to get first value of linked list
        Parameters:
            self
        Return:
            None
        """
        if self.head is None:
            print("List is empty")
        print(f'First Value is ->{self.head.data}')
        
    def get_last(self):
        """
        Description:
            Function to get last value of linked list
        Parameters:
            self
        Return:
            None
        """
        if self.head is None:
            print("List is empty")
        current_node = self.head
        while current_node.nextref is not None:
            current_node = current_node.nextref
        print(f'Last Value is ->{current_node.data}')

    def update_first(self, value):
        """
        Description:
            Function to update first value of linked list
        Parameters:
            self,value
        Return:
            None
        """
        if self.head is None:
            print("List is empty")
            return
        self.head.data = value

    def update_last(self, value):
        """
        Description:
            Function to update last value of linked list
        Parameters:
            self,value
        Return:
            None
        """
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node.nextref:
            current_node = current_node.nextref
        current_node.data = value

    def update_at_location(self, target, value):
        """
        Description:
            Function to update value at specific location in linked list
        Parameters:
            self,target,value
        Return:
            None
        """
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == target:
            self.head.data = value
            return
        current_node = self.head
        while current_node:
            if current_node.data == target:
                current_node.data = value
                return
            current_node = current_node.nextref
        print(f"{target} not found in this list")
        
    def isempty(self):
        """
        Description:
            Function to check if linked list is empty
        Parameters:
            self
        Return:
            None
        """
        if self.head is None:
            print('Linked List is empty')
        else:
            print('Linked List is not Empty')

    def total_elements(self):
        """
        Description:
            Function to get total number of elements in linked list
        Parameters:
            self
        Return:
            None
        """
        current_node = self.head
        count = 0
        while current_node:
            current_node=current_node.nextref
            count += 1
        print(f'The length of the Linked List is {count}')

    def display(self):
        """
        Description:
            Function to display linked list
        Parameters:
            self
        Return:
            None
        """
        if self.head is None:
            print("List is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.nextref
        print("None")

