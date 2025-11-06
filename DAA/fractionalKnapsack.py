weights = [2,3,4,7,8]
values = [1,2,3,4,5]
capacity = 5


def knap(weights ,values,capacity):
    result = 0
    w =[]

    for i in range(len(weights)):
        # value per gm
        w.append(values[i] / weights[i])

    for i in range(len(w)):
        maxIdx = i
        for j in range(i + 1, len(w)):
            if w[maxIdx] < w[j]:
                maxIdx = j
        weights[maxIdx], weights[i] = weights[i], weights[maxIdx]
        values[maxIdx], values[i] = values[i], values[maxIdx]

    for i in range(len(weights)):
        if capacity <= weights[i]:
            result += capacity * (values[i]/weights[i])
            break
        capacity -= weights[i]
        result += values[i]
    return result

print(knap(weights ,values,capacity))