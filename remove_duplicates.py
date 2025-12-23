arr = list(map(int,input().split()))

seen = set()
f_arr = []
for num in arr:
    if num not in seen:
        f_arr.append(num)
        seen.add(num)
print(f_arr)
        