"""Masterchef finals
Chef has been working hard to compete in MasterChef.
He is ranked 
X
X out of all contestants. However, only 
10
10 contestants would be selected for the finals.

Check whether Chef made it to the top 
10
10 or not?

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of one integers 
X
X — the current rank of Chef.
Output Format
For each test case, output on a new line, YES, if Chef made it to the top 
10
10 and NO otherwise.

Each character of the output may be printed in either uppercase or lowercase. That is, the strings NO, no, nO, and No will be treated as equivalent."""

t = int(input())
for _ in range(t):
    x = int(input())
    if x > 10:
        print("NO")
    else:
        print("YES")