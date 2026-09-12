class Node:
    def __init__(self, value= 0):
        self.data = value
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = new_node

    def display(self):
        trav = self.head
        # end tells print that dont add newline print on same line
        print("List: ", end='')
        while trav is not None:
            print(trav.data, end=", ")
            trav = trav.next
        print()

    def add_at_position(self, value, position):
        if position < 1:
            raise Exception(f"Invalid position: {position}")
        if self.head == None or position == 1:
            self.add_first(value)
        else:
            # create a new node
            new_node = Node(value)
            trav = self.head
            for i in range(1, position - 1):
                trav = trav.next
                if trav is None:
                    raise Exception(f"Invalid position:{position}")
            new_node.next = trav.next
            trav.next = new_node

def main():
    list = SinglyLinkedList()
    list.add_first(10)
    list.add_first(20)
    list.add_last(30)
    list.add_at_position(25,3)
    list.display()

if __name__ == "__main__":
    main()           
        