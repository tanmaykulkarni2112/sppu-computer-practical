def knapsack_dp(weights, values, W):
    n = len(weights)
    memo = {}

    def helper(i, remaining_weight):
        # Base case
        if i < 0 or remaining_weight <= 0:
            return 0

        if (i, remaining_weight) in memo:
            return memo[(i, remaining_weight)]

        # Skip current item
        not_take = helper(i - 1, remaining_weight)

        # Take current item (if it fits)
        take = 0
        if weights[i] <= remaining_weight:
            take = values[i] + helper(i - 1, remaining_weight - weights[i])

        memo[(i, remaining_weight)] = max(take, not_take)
        return memo[(i, remaining_weight)]

    return helper(n - 1, W)


# Example
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack_dp(weights, values, capacity))  # Output: 7
