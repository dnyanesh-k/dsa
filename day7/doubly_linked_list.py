class Node:
    def __init__(self, value=0):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_first(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count = self.count + 1

    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = new_node
            new_node.prev = trav
            self.count = self.count + 1

    def display(self):
        temp = None
        # display forward
        print(f"Fwd List : ", end='')
        trav = self.head
        while trav is not None:
            print(trav.data, end=', ')
            temp = trav
            trav = trav.next
        print()
        # display reverse
        print(f"Rev List : ", end='')
        trav = temp
        while trav is not None:
            print(trav.data, end=', ')
            trav = trav.prev
        print()

    def add_at_position(self, value, position):

        if position < 1 or position > self.count + 1:
            raise Exception("Invalid position")
        elif self.head is None or position == 1:
            self.add_first(value)
        elif position == self.count + 1:
            self.add_last(value)
        else:
            new_node = Node(value)
            trav = self.head
            for i in range(1, position-1):
                trav = trav.next
            temp = trav.next
            new_node.next = temp
            new_node.prev = trav
            temp.prev = new_node
            trav.next = new_node
            self.count = self.count + 1

    def del_first(self):
        if self.head is None:
            raise Exception("List is empty.")

        if self.head.next is None:
            self.head = None
        else:    
            self.head = self.head.next
            self.head.prev = None
        self.count = self.count - 1

    def del_at_position(self, position):
        if position < 1 or position > self.count:
            raise Exception("Invalid position")
        elif self.head.next is None or position == 1:
            self.del_first()
        else:
            trav = self.head
            for i in range(1, position - 1):
                trav = trav.next

            trav.next = trav.next.next

            if trav.next is not None:
                trav.next.prev = trav
            self.count = self.count - 1

    def del_all(self):
        while self.head is not None:
            self.del_first()

    def count_nodes(self):
        count = 0
        trav = self.head
        while trav is not None:
            count = count + 1
            trav = trav.next
        return count

def main():
    l = DoublyLinkedList()
    l.add_first(10)
    l.add_last(30)
    l.add_at_position(25, 2)
    l.del_at_position(2)
    # l.del_at_position(2)
    l.display()
    print(f"count = {l.count_nodes()}")

if __name__ == '__main__':
    main()