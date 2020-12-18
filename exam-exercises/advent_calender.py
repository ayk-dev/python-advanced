def fix_calendar(nums):
    is_swap = True
    while is_swap:
        is_swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_swap = True
    return nums


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)