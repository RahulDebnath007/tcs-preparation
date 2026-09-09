n = int(input())
arr = list(map(int, input().split()))
target = int(input())

seen = {}

for i in range(n):
    needed = target - arr[i]

    if needed in seen:
        print(seen[needed], i)
        break

    seen[arr[i]] = i

else:
    print(-1)