def move_zeros(nums):
    write = 0
    read = 0
    while read < len(nums):
        if (nums[read] != 0):
            nums[read], nums[write] = nums[write], nums[read]
            write += 1
        read += 1            

# nums = [0, 1, 0, 3, 0, 12]
# move_zeros(nums)
# print(nums)

def missinng_number(nums):
    n = len(nums)
    # sum_of_n = (n * (n + 1)) // 2
    # actual_sum = sum(nums)
    # diff = sum_of_n - actual_sum
    # return diff
    return ((n * (n + 1)) // 2) - sum(nums)

# nums = [0, 3, 1]
# print(missinng_number(nums))

def remove_duplicate_from_sorted_array(nums):
    left = 0
    right = 1
    count = 1
    while right <= len(nums)-1:
        if nums[left] != nums[right]:
            nums[left + 1] = nums[right]
            left += 1
            count += 1 
        right += 1
    return count

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# count = remove_duplicate_from_sorted_array(nums)        
# print(nums)
# print(count)

def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid +1
        else:
            right = mid +1
    return left        

# nums = [1,3,5,6,8]
# print(search_insert(nums, 9))

def find_first(nums, target):
    left = 0
    right = len(nums) -1
    first_seen = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            first_seen = mid
            right = mid -1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    return first_seen

def find_last(nums, target):
    left, right = 0, len(nums) -1           
    last_seen = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            last_seen = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last_seen        
         


def find_first_and_last_position(nums, target):
  first_seen = find_first(nums, target)      
  last_seen = find_last(nums, target)
  print(f"first seen = {first_seen}, last_seen = {last_seen}")

nums = [2, 2, 2, 2, 3]
find_first_and_last_position(nums, 2)