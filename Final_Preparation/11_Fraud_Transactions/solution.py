n = int(input())
arr = list(map(int, input().split()))

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

for x in freq:
    if freq[x] > 1:
        print(x, end=" ")