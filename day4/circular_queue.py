# in LQ if rear is at last index & initial few locations are empty in Q, still we'll not able to use those empty locations.
# this leads to poor memory utilization 
# aks false fullness

# SOLUTION : CIRCULAR QUEUE

class CircularQueue:

    def __init__(self, size):
        self.arr = [0] * size
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
            self.front +=1
        else:
            print("Q is empty.")

    def peek(self):
        if not self.is_empty():
            return self.arr[self.front + 1]
        else:
            print("Q is empty.")
    
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return self.rear == len(self.arr) - 1

def main():

   q = CircularQueue(3)

   q.push(2)
   q.push(3)
   q.push(3)
   q.push(4)
   q.pop()
   q.pop()
   q.pop()
   print(q.is_empty())
   print(q.push(5)) # false fullness
   
   print(q.peek())
   print(q.is_empty())
   print(q.is_full())

if __name__ == "__main__":
    main()   

        

        