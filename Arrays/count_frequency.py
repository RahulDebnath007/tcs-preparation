n = int(input())
arr = list(map(int, input().split()))

frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] +=1
    else:
        frequency[num] = 1

for num in frequency:
    print(f"{num}:{frequency[num]}")            