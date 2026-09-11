from paranthesis_balancing import Stack

def reverse_array_using_stack(arr):
    s = Stack()
    for num in arr:
        s.push(num)

    for i in range(len(arr)):
        num = s.pop()
        arr[i] = num

    return arr

def main():
    arr = [1, 2, 3, 4]
    print(reverse_array_using_stack(arr))

if __name__ == "__main__":
    main()