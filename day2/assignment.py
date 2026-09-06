def power(num, index):
    # base case : when index is 0 return 1
    if index == 0:
        return 1
    
    return num * power(num, index -1) # recursive call : pass num and index -1

# print(power(5, 3))

def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1

    a, b = 0, 1
    print(a, b, end=" ")
    for _ in range(2, n+1):
        current = a + b
        print(current, end=" ")
        a = b
        b = current

    # return b

# fibonacci(6)

def rec_fibonacci(current):
    # If looking for position 0 or 1, return the matching value
    if current == 0: return 0
    if current == 1: return 1

    # look up values at 2 previous positions and add them 
    return rec_fibonacci(current - 1) + rec_fibonacci(current - 2)

num = 6
for pos in range(num+1):
    print(rec_fibonacci(pos), end = ' ') # find the value present in fib series at position number 6