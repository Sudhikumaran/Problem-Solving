arr = list(map(int,input().split()))
n = len(arr)+1

expected_sum = n * (n+1)//2
actual_sum = sum(arr)

missing = expected_sum - actual_sum
print(missing)