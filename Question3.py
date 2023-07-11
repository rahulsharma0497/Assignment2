def findLHS(nums):
    num_freq = {}

    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1

    max_length = 0

    for num in num_freq:
        if num + 1 in num_freq:
            curr_length = num_freq[num] + num_freq[num + 1]
            max_length = max(max_length, curr_length)

    return max_length


# Example usage
nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print("Output:", result)
