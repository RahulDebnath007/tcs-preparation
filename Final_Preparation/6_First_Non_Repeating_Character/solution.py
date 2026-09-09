s = input().strip()

freq = {}

# Count frequency of every character
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Find the first character with frequency 1
answer = -1

for ch in s:
    if freq[ch] == 1:
        answer = ch
        break

print(answer)