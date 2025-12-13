"""
    a
  a a a 
a a a a a
  a a a
    a
"""
n = int(input())
ch = input()

# upper part (including middle)
for i in range(n):
    print(ch * (2*i + 1))

# lower part (excluding middle)
for i in range(n - 2, -1, -1):
    print(ch * (2*i + 1))
