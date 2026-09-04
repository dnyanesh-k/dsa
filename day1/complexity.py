def factorial(num):
    result = 1
    for index in range(1, num+1):
        result = result * index
    return result   
 
def matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end = ' ')
        print()

def decimal_to_binary(num):
    while num > 0:
        print(num % 2, end = " ")
        num = num // 2
    print()            

def print_table(num):
    for index in range(1, 10+1):
        print(index * num)


def main():
    num = int(input("enter a number : "))
    # print(factorial(num))
    # mat = [[1,2,3], [4,5,6], [7,8,9]]
    # matrix(mat)

    # decimal_to_binary(num)
    print_table(num)

if __name__ == "__main__":
    main()    
        