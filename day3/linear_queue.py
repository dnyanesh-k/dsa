# linear data structure which has 2 ends 1. front and 2. rear
# data is inserted from rear end and removed from front end 
# Q works on FIFO(first in first out)/LILO(last in last out) principle
# operations
#  - insert/enqueue/push/offer 
#  - remove/dequeue/pop/poll
#  - read value from the front end
# all ops are performed in O(1)

class LinearQueue:

    def __init__(self, size):
        # initialize array of input size with zeros
        self.arr = [0] * size
        # initialize front and rear with -1
        self.front = -1
        self.rear = -1

    def push(self, value):
        if not self.is_full():
            self.rear += 1
            self.arr[self.rear] = value
        else:
            print("Q is full.")    

    def pop(self):
        if not self.is_empty():
            self.front = self.front + 1
        else:
            print("Q is empty")    

    def peek(self):
        if not self.is_empty():
            return self.arr[self.front + 1]
        else:
            print("Q is Empty")

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return self.rear == len(self.arr) - 1

def main():
    lq = LinearQueue(6)
    lq.push(11)
    lq.push(22)
    # lq.push(33)
    # lq.push(44)
    # lq.push(55)
    # lq.push(66)
    # lq.push(77)
    # print(lq.peek())
    lq.pop()
    lq.pop()
    # lq.pop()
    print(lq.peek())

    # while not lq.is_empty():
    #     val = lq.peek()
    #     lq.pop()
    #     print(val, end = ' ')

if __name__ == "__main__":
    main()

    



    
