s1 = input()
s2 = input()

if len(s1) != len(s2):
    print(False)
else:
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch,0)+1
    
    is_anagram = True
    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            is_anagram = False
            break
        freq[ch] -= 1
    print(is_anagram)
            