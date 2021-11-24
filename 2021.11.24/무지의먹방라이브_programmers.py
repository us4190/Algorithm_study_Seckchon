def solution(food_times, k):
    num_foods = len(food_times)

    sortedList = sorted(food_times)
    prev = 0 
    prefixSum = []
    for i in sortedList:
        if prefixSum:
            prefixSum.append(i+prefixSum[-1])
        else:
            prefixSum.append(i)
            
    prev_cal = 0
    prev_rest_foods = bound_val = rest_k = -1
    for i in range(num_foods):
        rest_foods = num_foods - (i+1)
        cal = prefixSum[i] + sortedList[i] * rest_foods
        if cal > k:
            if i < 1:
                bound_val = 0
            else:
                bound_val = sortedList[i-1]
            rest_k = k - prev_cal
            break
        prev_cal = cal
        prev_rest_foods = rest_foods
    
    if bound_val == -1:
        return -1
    
    if prev_rest_foods == -1:
        prev_rest_foods = num_foods

    if rest_k > prev_rest_foods:
        x = rest_k // prev_rest_foods
        rest_k %= prev_rest_foods
        bound_val += x
    
    idx = 0
    count = 0
    for i in range(len(food_times)):
        if food_times[i] > bound_val:
            count += 1
        if count == rest_k+1:
            idx = i
            break
            
    return idx+1