def rec_binary_search(nums, left, right, target):

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            index = rec_binary_search(nums, mid + 1, right, target)
        else:
            index = rec_binary_search(nums,left, mid - 1, target)
        return index      

def main():
    nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    print(rec_binary_search(nums,0, len(nums)-1, 55))

if __name__ == '__main__':
    main()