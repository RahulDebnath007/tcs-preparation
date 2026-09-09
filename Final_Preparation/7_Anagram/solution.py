s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("Not Anagram")
else:
    freq = {}

    # Count characters in first string
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    # Subtract characters from second string
    for ch in s2:
        freq[ch] = freq.get(ch, 0) - 1

    is_anagram = True

    for value in freq.values():
        if value != 0:
            is_anagram = False
            break

    if is_anagram:
        print("Anagram")
    else:
        print("Not Anagram")