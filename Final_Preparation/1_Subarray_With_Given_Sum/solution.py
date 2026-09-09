n = int(input())
arr = list(map(int, input().split()))
k = int(input())

prefix_sum = 0

# prefix_sum : index
seen = {0: -1}

for i in range(n):
    prefix_sum += arr[i]

    needed = prefix_sum - k

    if needed in seen:
        print(seen[needed] + 1, i)
        break

    if prefix_sum not in seen:
        seen[prefix_sum] = i

else:
    print(-1)