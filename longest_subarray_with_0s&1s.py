arr = list(map(int,input().split()))

curr_sum = 0
max_len = 0
sum_index = {}

for i in range(len(arr)):
    if arr[i] == 0:
        curr_sum += -1
    else:
        curr_sum += 1
        
    
    if curr_sum == 0:
        max_len = i + 1
    
    if curr_sum in sum_index:
        max_len = max(max_len, i - sum_index[curr_sum])
    else:
        sum_index[curr_sum] = i
        
print(max_len)