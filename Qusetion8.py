def minimumScore(nums, k):
    min_val = min(nums)
    max_val = max(nums)

    if k == 0:
        return max_val - min_val

    for i in range(len(nums)):
        if nums[i] - k > min_val:
            nums[i] -= k
        elif nums[i] + k < max_val:
            nums[i] += k

    return max(nums) - min(nums)


# Example usage
nums = [1]
k = 0
result = minimumScore(nums, k)
print("Output:", result)
