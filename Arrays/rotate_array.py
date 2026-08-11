n = int(input())
arr = list(map(int, input().split()))
k = int(input())


def reverse_section(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate(arr, k):
    n = len(arr)
    k = k % n

    if k == 0:
        return

    reverse_section(arr, 0, k - 1)
    reverse_section(arr, k, n - 1)
    reverse_section(arr, 0, n - 1)


left_rotate(arr, k)

print(*arr)