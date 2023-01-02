def majority_element(nums):
    half_len = int(len(nums) / 2)
    nums = sorted(nums)
    index_of_swap = 0
    current_num = nums[0]

    for i in range(1,len(nums)):
        if (nums[i] != current_num):
            index_of_swap = i
            current_num = nums[i]
        
        if (i - index_of_swap + 1 > half_len):
            return current_num
    return "Something went wrong"

print(majority_element([2,2,1,1,1,2,2]))