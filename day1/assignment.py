# linear serch to return last occurance 
def linear_search(key, nums):
    last_index = -1  # default if key not found

    for i in range(len(nums)):
        if(nums[i] == key):
            # update with latest found index
            last_index = i 
    return last_index

# print number of comaprisons done
def linear_search_comps(key, nums):
    comps = 0
    for index in range(len(nums)):
        comps += 1  # increment the comp for each check
        if (nums[index] == key):
            return index, comps   # returns the tuple of index and comps
    return index, comps  
    
# search employee by emp_id
def search_emp_by_id(target_id, emps):
    for emp in emps:
        # print(emp['name'])
        if (emp['emp_id'] == target_id):
            return emp
    
    return(f"emp not found with {target_id}")    

# search emp by salary 
def search_by_salary(emps, target_salary):
    for emp in emps:
        if (emp['salary'] == target_salary):
            return emp
        
    return(f"emp not found with {target_salary}")

# binary search if array is sorted in descending order
def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            right = mid - 1
        else:
            left = mid +1
    return -1      

def linear_search_nth(n, nums, target):
    count = 0
    for i in range(len(nums)):
        if nums[i] == target:
            count += 1
            if count == n:
                return n
    return -1        

def main():
    # nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    # nums = [99, 88, 77, 66, 55, 44, 33, 22, 11]
    nums = [1, 2, 3, 2, 4, 5, 4, 2]
    print(linear_search_nth(1, nums, 5))
    # print(binary_search(nums, 77))
    # index, comps = linear_search_comps(44, nums) # tuple unpacking
    # print(f"index = {index}, comps = {comps}")

    # emps = [
    #     {"name" : "soham", "emp_id" : "emp1", "salary": "70k"},
    #     {"name" : "om", "emp_id" : "emp2", "salary" : "80k"} 
    # ]
    # print(search_by_salary(target_salary = "80k", emps = emps))

if __name__ == '__main__':
    main()                