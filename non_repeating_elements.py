s = input()

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0)+1


ans = ''

for ch in s:
    if freq[ch] == 1:
        ans += ch
print(ans)