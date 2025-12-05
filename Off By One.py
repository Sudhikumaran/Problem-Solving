"""Off By One
You just bought a new calculator, but it seems to have a small problem: all its results have an extra 
1
1 appended to the end.
For example, if you ask it for 3 + 5, it'll print 81, and 4 + 12 will result in 161.

Given 
A
A and 
B
B, can you predict what the calculator will print when you ask it for 
A
+
B
A+B?

Input Format
The first and only line of input will contain two space-separated integers 
A
A and 
B
B.
Output Format
Print a single integer: the calculator's output when you enter 
A
+
B
A+B into it."""

a,b = map(int,input().split())
add = a+b
print(str(add)+"1")