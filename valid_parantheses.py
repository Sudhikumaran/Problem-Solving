"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

s = input()

stack = []
mapping = {')':'(','}':'{',']':'['}

for ch in s:
    if ch in mapping:
        if not stack or stack.pop() != mapping[ch]:
            print("False")
        else:
            stack.append(ch)
print(stack)