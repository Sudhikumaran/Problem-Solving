str1 = input()
str2 = input()

if len(str1) != len(str2):
    print("Not Anagram")
else:
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:
        print("Anagram")
    else:
        print("Not Anagram")