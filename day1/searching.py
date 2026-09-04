def linear_search(key : int, nums : list) -> int:
    for i in range(len(nums)):
        if nums[i] == key:
            return i
    return -1    

def binary_search(key, nums):
    left = 0
    right = len(nums) -1
    while (left <= right):
        mid = int((left + right) /2 )
        print(f'mid = {mid}')
        if nums[mid] == key:
            return  mid
        elif (nums[mid] < key):
            left = mid + 1
        else:
            right = mid -1
    return -1
    
def main():
    nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]    
    
    key = int(input("enter number to be searched : "))
    # index = linear_search(key, nums)
    index = binary_search(key, nums)
    # print(f"index = {index}")
    if (index == -1):
        print(f"{key} is not present.")
    else:
        print(f"{key} is present at position {index + 1}")

if __name__ == "__main__":
    main()    