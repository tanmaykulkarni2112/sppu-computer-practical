deadline = [1, 2, 2, 1]
profit = [200, 20, 60, 150]
days = 4
total = 0

for i in range(len(profit)):
    maxP = i
    for j in range(i + 1, len(profit)):
        if profit[maxP] < profit[j]:
            maxP = j
    profit[maxP], profit[i] = profit[i], profit[maxP]
    deadline[maxP], deadline[i] = deadline[i], deadline[maxP]

calc = [-1] * days  
for i in range(len(deadline)):
    for j in range(deadline[i] - 1, -1, -1):  
        if calc[j] == -1:  
            calc[j] = 1  
            total += profit[i]  
            break 

print(total)
