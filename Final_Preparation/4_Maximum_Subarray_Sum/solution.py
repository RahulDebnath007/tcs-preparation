n = int(input())
arr = list(map(int, input().split()))

current_sum = arr[0]
maximum_sum = arr[0]

for i in range(1, n):
    current_sum = max(arr[i], current_sum + arr[i])
    maximum_sum = max(maximum_sum, current_sum)

print(maximum_sum)