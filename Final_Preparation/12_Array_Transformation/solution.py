n = int(input())
arr = list(map(int, input().split()))

minimum = arr[0]
maximum_difference = 0

for i in range(1, n):
    difference = arr[i] - minimum

    if difference > maximum_difference:
        maximum_difference = difference

    if arr[i] < minimum:
        minimum = arr[i]

print(maximum_difference)