def maximumProduct(nums):
    nums.sort()
    n = len(nums)
    return max(nums[n-1] * nums[n-2] * nums[n-3], nums[0] * nums[1] * nums[n-1])

# Example usage
nums = [1, 2, 3]
result = maximumProduct(nums)
print("Output:", result)