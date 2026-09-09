# Subarray With Given Sum

**Pattern:** Prefix Sum + Hashing
**Difficulty:** Medium
**Time Complexity:** O(N)
**Space Complexity:** O(N)

---

## Problem Statement

Given an array of integers and a target sum `K`, find a **contiguous subarray** whose elements add up to `K`.

Return the **starting and ending indices** of the first such subarray. If no such subarray exists, print `-1`.

---

## Core Idea

```
Current Prefix Sum − Previous Prefix Sum = Subarray Sum

If subarray sum = K:
    current_sum − previous_sum = K
    previous_sum = current_sum − K
```

While traversing the array, check whether `current_sum - K` has already appeared as a prefix sum. If it has, a subarray with sum `K` has been found.

---

## Recognizing the Pattern

Trigger words in a problem statement:

- subarray / contiguous / continuous
- sum equals K
- given sum
- count subarrays with sum K
- longest subarray with sum K

```
SUBARRAY + SUM + TARGET K  →  PREFIX SUM + HASHING
```

---

## Example

```
Array = [1, 2, 3, 4, 5]
K = 9
```

Prefix sums: `1, 3, 6, 10, 15`

At index 3, `current_sum = 10`. We need `previous_sum = 10 - 9 = 1`, which occurred at index 0.

```
start = 0 + 1 = 1
end   = 3

arr[1:4] = [2, 3, 4] → 2 + 3 + 4 = 9
Answer: 1 3
```

---

## Algorithm

1. Initialize `prefix_sum = 0`
2. Initialize `seen = {0: -1}` (handles subarrays starting at index 0)
3. Traverse the array, adding each element to `prefix_sum`
4. Compute `needed = prefix_sum - k`
5. If `needed` is in `seen`, a subarray is found: `start = seen[needed] + 1`, `end = i`
6. Otherwise, store `prefix_sum` in `seen` (only if not already present)

---

## Python Solution

```python
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

prefix_sum = 0
seen = {0: -1}  # prefix_sum : index

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
```

---

## Why `seen = {0: -1}`?

Consider `arr = [2, 3]`, `K = 5`. At index 1, `prefix_sum = 5`, so `needed = 0`.

We need to know prefix sum `0` existed *before* the array started — that's what `seen = {0: -1}` represents. Then `seen[0] + 1 = 0`, the correct starting index.

---

## Examples

**Example 1**
```
Input:
5
1 2 3 4 5
9

Output:
1 3
```

**Example 2 — subarray starts at index 0**
```
Input:
4
2 3 5 1
5

Output:
0 1
```

**Example 3 — no subarray**
```
Input:
5
1 2 3 4 5
20

Output:
-1
```

---

## Complexity Comparison

| Approach              | Time  | Space |
|-----------------------|-------|-------|
| Brute Force (nested loops) | O(N²) | O(1)  |
| Prefix Sum + Hashing   | O(N)  | O(N)  |

Brute force checks every subarray and can cause a **Time Limit Exceeded (TLE)** on large inputs. Prefix Sum + Hashing traverses the array once with O(1) average dictionary lookups.

---

## Pattern to Memorize

```python
prefix_sum = 0
seen = {0: -1}

for i in range(n):
    prefix_sum += arr[i]
    needed = prefix_sum - k

    if needed in seen:
        # answer found

    if prefix_sum not in seen:
        seen[prefix_sum] = i
```

Key line: `needed = prefix_sum - k`

---

## Decision Flow

```
Find a subarray
      ↓
Is it contiguous?      → YES
      ↓
Is there a sum condition? → YES
      ↓
Is there a target K?   → YES
      ↓
Prefix Sum + Hashing
```

---

## Common Variations

| Variation | Pattern |
|---|---|
| Find one subarray with sum K | Prefix Sum + Hashing |
| Count subarrays with sum K | Prefix Sum + Frequency Hash Map |
| Longest subarray with sum K | Prefix Sum + Hashing (store *first* occurrence) |
| Print the subarray itself | Same pattern, print `arr[start:end+1]` |
| Array contains negative numbers | Prefix Sum + Hashing (sliding window doesn't work here) |

---

## Related Problem Family

```
Prefix Sum
├── Subarray Sum = K
├── Count Subarrays With Sum K
├── Longest Subarray With Sum K
├── Subarray With Zero Sum
├── Equal Number of 0s and 1s
└── Range Sum Queries
```

---

## Quick Revision

- **Problem:** Find a contiguous subarray with sum K
- **Pattern:** Prefix Sum + Hashing
- **Formula:** `needed = current_prefix_sum - K`
- **Hash Map init:** `seen = {0: -1}`
- **Complexity:** O(N) time, O(N) space
- **Keywords:** subarray, contiguous, sum, target K, given sum, longest subarray, count subarrays

---

## Final Takeaway

```
Subarray Sum
     ↓
Prefix Sum
     ↓
Current Prefix − Previous Prefix
     ↓
Need Previous Prefix = Current Prefix − K
     ↓
Store Prefix Sums in Hash Map
     ↓
O(N) Solution
```