def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum


# Example usage
nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
print("Output:", result)