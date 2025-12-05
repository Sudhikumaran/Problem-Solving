"""
Docstring for Donation Drive
Donation Drive
A blood drive aims to collect 
N
N number of blood donations.
The drive has collected 
X
X donations so far. Find the remaining number of donations needed to reach the target.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case contains two space-separated integers 
N
N and 
X
X — the number of required donations and the number of collected donations, respectively.
Output Format
For each test case, output on a new line, the remaining number of donations needed to reach the target.
"""

n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    print(x-y)