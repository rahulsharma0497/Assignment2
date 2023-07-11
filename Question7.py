def isMonotonic(nums):
    n = len(nums)
    increasing = True
    decreasing = True

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            decreasing = False
        if nums[i] < nums[i - 1]:
            increasing = False

    return increasing or decreasing


# Example usage
nums = [1, 2, 2, 3]
result = isMonotonic(nums)
print("Output:", result)
