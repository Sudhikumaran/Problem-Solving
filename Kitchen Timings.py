"""Kitchen Timings
The working hours of Chef’s kitchen are from 
X
X pm to 
Y
Y pm 
(
1
≤
X
<
Y
≤
12
)
(1≤X<Y≤12).

Find the number of hours Chef works.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two space-separated integers 
X
X and 
Y
Y — the starting and ending time of working hours respectively.
Output Format
For each test case, output on a new line, the number of hours Chef works."""


t= int(input())

for _ in range(t):
    x,y = map(int,input().split())
    print(abs(x-y))