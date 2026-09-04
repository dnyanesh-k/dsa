def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i -1
        temp = nums[i]
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = temp
        
def main():
    nums = [5, 4, 2, 6, 3, 1]
    insertion_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()