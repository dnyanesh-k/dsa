def selection_sort(nums):
    for i in range(len(nums)):
        print(i)
        for j in range(len(nums)):
            if(nums[i]< nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
        print(nums)        

def bubble_sort(nums):
    pass_count = 0
    comps_count = 0
    for i in range(len(nums)-1):
        pass_count += 1
        for j in range(len(nums)-1):
            comps_count += 1
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
        # print(nums)   
    print(pass_count)
    print(comps_count) 
    
def bubble_sort_improved(nums): 
    pass_count = 0
    comps_count = 0  
    for i in range(len(nums)-1):
        swapped = False
        pass_count += 1
        for j in range(len(nums)-1 -i):
            comps_count += 1 
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break        
    
    print(pass_count)
    print(comps_count)                 
def main():
    nums = [5, 4, 2, 6, 3, 1]
    # selection_sort(nums)
    bubble_sort(nums)
    # bubble_sort_improved(nums)
    print(nums)

if __name__ == "__main__":
    main()
