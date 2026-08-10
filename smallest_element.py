n = int(input())

arr = list(map(int, input().split()))

smallest = arr[0]

for i in range(1, n):
    if arr[i] < smallest:
        smallest = arr[i]

print(smallest)