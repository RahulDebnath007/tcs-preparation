n = int(input())

pairs = []

for _ in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))

pairs.sort()

for a, b in pairs:
    print(a, b)