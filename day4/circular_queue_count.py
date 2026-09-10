class CircularQueue:
    def __init__(self, size):
        self.arr = [0] * size
        self.front = -1
        self.rear = -1
        self.count = 0

    def push(self, value):
        if not self.is_full():
            self.rear = (self.rear + 1) % len(self.arr)
            self.arr[self.rear] = value
            self.count = self.count + 1
        else:
            print("Q is full.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % (len(self.arr))
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            self.count = self.count - 1
        else:
            print("Q is Empty.")

    def peek(self):
        if not self.is_empty():
            return self.arr[self.front + 1]
        else:
            print("Q is Empty.")

    def is_full(self):
        return self.count == len(self.arr)

    def is_empty(self):
        return self.count == 0

def main():
    q = CircularQueue(3)
    q.push(1)
    q.push(2)
    q.push(3)
    # print(q.peek())
    q.pop()
    q.pop()
    q.pop()
    q.peek()

if __name__ == "__main__":
    main()    
        