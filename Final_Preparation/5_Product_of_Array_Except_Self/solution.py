n = int(input())
arr = list(map(int, input().split()))

answer = [1] * n

# Store prefix products
prefix = 1

for i in range(n):
    answer[i] = prefix
    prefix *= arr[i]

# Multiply by suffix products
suffix = 1

for i in range(n - 1, -1, -1):
    answer[i] *= suffix
    suffix *= arr[i]

print(*answer)