weights = [2,3,4,5]
values = [2,6,7,10]
capacity = 12

def knap(weights, values, capacity):
    memo = {}
    n = len(weights)

    def helper(i, remaining):
        if i < 0 or remaining <= 0:
            return 0
        
        if (i, remaining) in memo:
            return memo[(i, remaining)]
        
        notTaken = helper(i - 1 , remaining)
        taken = 0
        if remaining >= weights[i]:
            taken = values[i] + helper(i-1, remaining - weights[i])
        memo[(i, remaining)] = max(taken, notTaken)
        return memo[(i, remaining)]
    return helper(n-1, capacity)

print(knap(weights, values, capacity))