"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""

strs = input()
if not strs:
    print("")


prefix = strs[0]

for i in strs[1:]:
    while not i.startswith(prefix):
        prefix = prefix[:-1]
        if prefix == "":
            print("")
print(prefix)
