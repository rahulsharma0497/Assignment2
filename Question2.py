def distributeCandies(candyType):
    unique_candies = set(candyType)  # Get the unique candy types using a set
    max_candies = len(candyType) // 2

    return min(len(unique_candies), max_candies)


# Example usage
candyType = [1, 1, 2, 2, 3, 3]
result = distributeCandies(candyType)
print("Output:", result)