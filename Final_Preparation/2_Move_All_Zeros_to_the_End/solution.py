n = int(input())
arr = list(map(int, input().split()))

pos = 0

# Place all non-zero elements at the front
for i in range(n):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1

# Fill remaining positions with zeros
while pos < n:
    arr[pos] = 0
    pos += 1

print(*arr)