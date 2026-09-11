from paranthesis_balancing import Stack

def remove_adjacent_duplicates(input_str):
    s = Stack()
    for ch in input_str:
        if not s.is_empty() and s.peek() == ch:
           s.pop()
        else:
            s.push(ch)
        
    new_str = ''
    while not s.is_empty():
        top = s.peek()
        s.pop()
        new_str += top

    return new_str[::-1]
    
def main():
    input_str = "abbacaba"
    print(remove_adjacent_duplicates(input_str))

if __name__ == "__main__":
    main()    