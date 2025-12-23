arr = list(map(int,input().split()))

k = int(input())

sum_index = {}

curr_sum = 0

max_len = 0


for i in range(len(arr)):
    curr_sum += arr[i]
    
    if curr_sum == k:
        max_len = i + 1
        
    if curr_sum - k in sum_index:
        max_len = max(max_len, i - sum_index[curr_sum - k])
    else:
        sum_index[curr_sum] = i
        
print(max_len)