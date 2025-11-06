weights = [2,3,4,5,6,7,8]
values = [2,5,6,20,60,8,12]
capacity = 10


# create an array to find the value per gm
def knap(weights, values, capacity):
    w = []
    for i in range(len(weights)):
        w.append(values[i] / weights[i])

    for i in range(len(w)):
        max_idx = i
        for j in range(i + 1, len(w)):
            if w[max_idx] < w[j]:
                max_idx = j
        w[i] , w[max_idx] = w[max_idx], w[i]
        weights[i] , weights[max_idx] = weights[max_idx], weights[i]
        values[i] , values[max_idx] = values[max_idx], values[i]

    # we want to add if the weight is in capacity
    result = 0
    for i in range(len(weights)):
        if weights[i] <= capacity:
            capacity -= weights[i]
            result += values[i]
        elif capacity == 0:
            return result
        else:
            return result + capacity * (values[i]/weights[i])
        
print(knap(weights, values, capacity))