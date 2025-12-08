str1 = input()
count_dict = {}

for ch in str1:
    if ch not in count_dict:
        count_dict[ch] = 1
    else:
        count_dict[ch] += 1

for ch, cnt in count_dict.items():
    print(ch, cnt)
