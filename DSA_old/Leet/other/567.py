cost = [10,15,20,30]
step1 = 0
step2 = 0
for i in range(len(cost)-1,0,-1 ):
    current = cost[i]+min(step1, step2)
    step1 =  step2
    step2 = current
    print(current, step1, step2)
print( min(step1,step2))


sum_pay = {0:cost[0], 1:cost[1]}

for i in range(2,len(cost)):

    sum_pay[i] = min(sum_pay[len(cost)-1], sum_pay[len(cost)-2]) + cost[i]

return min(sum[len(cost)-1], sum[len(cost)-2])