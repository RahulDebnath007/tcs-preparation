n = int(input())

arr = list(map(float, input().split()))

total = 0.0

for num in arr:
    total += num

average = total / n

print(average)