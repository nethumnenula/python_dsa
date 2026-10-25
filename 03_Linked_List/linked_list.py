from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    # TRAVERSAL
    def traversal(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            if temp.next is not None:
                print("->", end=" ")
            temp = temp.next
        print()

    # INSERT AT FRONT
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # INSERT AT END
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    # INSERT AT ANYWHERE
    def insert_at_anywhere(self, position, data):
        if position < 1:
            print("Enter a valid number")
            return

        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        current_position = 1
        while current_position < position - 1 and temp is not None:
            temp = temp.next
            current_position += 1

        if temp is None:
            print("Position out of range!")
            return
        new_node.next = temp.next
        temp.next = new_node

    #SEARCH
    def search(self, key):
        temp = self.head
        position = 1

        while temp is not None:
            if temp.data == key:
                print(f"{key} found at position {position}")
            temp = temp.next
            position += 1

        print(f"{key} not found!")

    # UPDATE
    def update(self, position, new_data):
        if position < 1:
            print("Invalid position")
            return

        temp = self.head
        current_position = 1
        while current_position < position and temp is not None:
            temp = temp.next
            current_position += 1

        if temp is None:
            print("Position out of bound")
            return
        temp.data = new_data


    # DELETE BY POSITION
    def delete_by_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position < 1:
            print("Enter a valid position")
            return

        if position == 1:
            print(f"{self.head.data} has been deleted!")
            self.head = self.head.next
            return

        temp = self.head
        current_position = 1
        while current_position < position - 1 and temp is not None:
            temp = temp.next
            current_position += 1

        if temp is None or temp.next is None:
            print("Position out of bound.")
            return

        deleted_data = temp.next.data
        temp.next = temp.next.next
        print(f"{deleted_data} has been deleted!")

    # DELETE BY VALUE
    def delete_by_value(self, key):
        if self.head is None:
            return

        if self.head.data == key:
            print(f"{self.head.data} has been deleted!")
            self.head = self.head.next
            return

        temp = self.head
        while temp.next is not None and not temp.next.data == key:
            temp = temp.next

        if temp.next is None:
            print("Value not found!")
            return
        deleted_value = temp.next.data
        temp.next = temp.next.next
        print(f"{deleted_value} has been deleted!")