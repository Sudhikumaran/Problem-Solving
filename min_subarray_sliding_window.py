arr = list(map(int,input().split()))

min_len = float('inf')
left = 0
curr_sum = 0

for right in range(len(arr)):
    curr_sum += arr[right]
    
    while curr_sum >= k:
        min_len = min(min_len,right-left + 1)
        curr_sum -= arr[left]
        left+=1
    
print(min_len if min_len != float('inf') else 0)
