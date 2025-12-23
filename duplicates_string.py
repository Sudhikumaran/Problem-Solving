s = input()

seen = set()

freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0)+1

duplicates = ''

for ch in s:
    if freq[ch] > 1 and ch not in seen:
        duplicates += ch
        seen.add(ch)
        
print(duplicates)
        