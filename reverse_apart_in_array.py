t = int(input())

for _ in range(t):
	n, m = map(int,input().split())
	arr = list(map(int,input().split()))

	reversed_arr = []
	for i in range(m+1,n):
		reversed_arr.append(arr[i])
	reversed_arr.reverse()
	normal_arr = []
	for i in range(m+1):
		normal_arr.append(arr[i])
	
	final_arr = normal_arr + reversed_arr

	print(final_arr)

