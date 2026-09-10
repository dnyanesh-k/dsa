from collections import deque

class StackUsingDeQue:
    def __init__(self):
        self.main = deque()
        self.temp = deque()

    def push(self, value):
        while self.main:
            self.temp.append(self.main.popleft())
        self.main.append(value)
        while self.temp:
            self.main.append(self.temp.popleft())

    def pop(self):
        return self.main.popleft()

    def is_empty(self):
        return len(self.main) == 0

def main():
    s = StackUsingDeQue()

    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.pop()
    print(s.is_empty())

if __name__ == "__main__":
    main()