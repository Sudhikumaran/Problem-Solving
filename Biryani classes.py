"""Biryani classes
According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes for 
X
X weeks, and the cost of classes per week is 
Y
Y coins. What is the total amount of money that Chef will have to pay?

Input Format
The first line of input will contain an integer 
T
T — the number of test cases. The description of 
T
T test cases follows.
The first and only line of each test case contains two space-separated integers 
X
X and 
Y
Y, as described in the problem statement.
Output Format
For each test case, output on a new line the total amount of money that Chef will have to pay."""

t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    val = x * y
    print(val)