n = int(input())
arr = list(map(int, input().split()))

arr.sort()
mid = n//2
increasing = arr[:mid]
decreasing = arr[mid:]

decreasing.reverse()

result = increasing + decreasing
print(*result)