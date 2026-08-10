n = int(input())
arr = list(map(int, input().split()))

largest = float('-inf')
second_largest = float('-inf')
smallest = float('inf')
second_smallest = float('inf')

for num in arr:
    # find the second largest element
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    # find the second smallest element
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second largest:", second_largest)
print("Second smallest:", second_smallest)