class Stack:
    def __init__(self, size):
        self.arr = [0] * size
        self.top = -1

    def push(self, value):
        if not self.is_full():
            self.top = self.top + 1
            self.arr[self.top] = value
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            self.top = self.top - 1
        else:
            print("Stack is empty.")

    def peek(self):
        return self.arr[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.arr) -1

def main():
    st = Stack(3)

    st.push(1)
    st.push(2)
    st.push(3) 
    st.push(4)
    st.pop() 
    print(st.peek())

if __name__ == "__main__":
    main()    