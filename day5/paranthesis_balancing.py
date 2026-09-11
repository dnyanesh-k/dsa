class Stack:
    def __init__(self):
        self.arr = list()

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        return self.arr.pop()

    def peek(self):
        return self.arr[len(self.arr) - 1]

    def is_empty(self):
        return len(self.arr) == 0

def is_paranthesis_balanced(expr):
    s = Stack()
    open = "([{<"
    close = ")]}>"

    for i in range(len(expr)):
        symbol = expr[i]
        index = open.find(symbol)# find returns -1 on failure
        if index != -1:  # if opening paranthesis
            s.push(symbol)
        else:
            index = close.find(symbol)
            if index != -1: # if closing paranthesis
                if s.is_empty():
                    return False
                top = s.pop()
                if open.find(top) != index: # not balanced means opening != closing
                    return False
    if not s.is_empty():
        return False
    return True


def main():
    expr = "5+([9-4]*(8-{6/2}))"
    if is_paranthesis_balanced(expr):
        print("Paranthesis is balanced.")
    else: 
        print("Paranthesis is NOT balanced.")

if __name__ == "__main__":
    main()


