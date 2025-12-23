arr = list(map(int,input().split()))

k = int(input())

freq = {0: 1}

curr_sum = 0
count = 0


for num in range(len(arr)):
    curr_sum += num
    
    if curr_sum - k in freq:
        count += freq[curr_sum - k]
    freq[curr_sum] = freq.get(curr_sum, 0) + 1
    
print(count)