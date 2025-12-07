n = int(input())

sump= 0 

for i in range(1,n):
    if n % i == 0:
        sump += i
    if sump == n:
        print("Perfect Number")
        break
else:
    print("Not a Perfect Number")