# 🔥 Second Largest Element

> **Pattern:** Single Pass / Value Tracking
> **Difficulty:** Easy
> **Time Complexity:** O(N)
> **Space Complexity:** O(1)

---

## 📌 Problem

Given an array of `N` integers, find the **second largest distinct element**.

### Example

```
Input:
6
10 5 8 10 3 7

Output:
8
```

The largest element is `10`. The second largest **distinct** element is `8` — the duplicate `10` doesn't count.

---

## 🧠 Pattern

Instead of sorting, track two values while scanning the array once:

- `largest` — largest value seen so far
- `second_largest` — second largest **distinct** value seen so far

**Recognize this pattern when asked for:** largest, second largest, second smallest, third largest, top two values, Kth largest, max and second max — anything solvable by tracking a fixed number of values in one pass.

---

## 💡 Core Logic

Initialize both to `float('-inf')` (not `0` — fails on all-negative arrays).

For each element `x`:

| Condition | Action |
|---|---|
| `x > largest` | old `largest` becomes `second_largest`; `x` becomes new `largest` |
| `second_largest < x < largest` | `x` becomes new `second_largest` |
| `x == largest` | ignore (duplicate of the largest) |

```python
n = int(input())
arr = list(map(int, input().split()))

largest = float('-inf')
second_largest = float('-inf')

for x in arr:
    if x > largest:
        second_largest = largest
        largest = x
    elif x > second_largest and x != largest:
        second_largest = x

print(-1 if second_largest == float('-inf') else second_largest)
```

**Why this is a strong solution:** O(N) time, O(1) space, no sorting, handles duplicates and negative numbers, easy to reproduce under exam conditions.

---

## 🔬 Dry Run

Array: `[10, 5, 8, 10, 3, 7]`

| x | largest | second_largest | Action |
|---|---|---|---|
| 10 | 10 | -∞ | New largest |
| 5 | 10 | 5 | New second largest |
| 8 | 10 | 8 | Update second largest |
| 10 | 10 | 8 | Duplicate → ignore |
| 3 | 10 | 8 | No change |
| 7 | 10 | 8 | No change |

**Answer: `8`**

---

## 🧪 More Examples

| Input | Output | Note |
|---|---|---|
| `-10 -5 -20 -3 -8` | `-5` | Works with all negatives |
| `10 10 10 8 5` | `8` | All copies of largest ignored |
| `7 7 7 7` | `-1` | Only one distinct value exists |
| `5 5 2 2 5 2` | `2` | Two distinct values |
| `10` | `-1` | Single element, no second value |

---

## ⚠️ Common Mistakes

**1. Initializing with `largest = 0`**
Fails on arrays with all negative numbers (e.g. `[-10, -5, -20, -3]`) since no element beats `0`. Always use `float('-inf')`.

**2. Sorting and taking `arr[-2]`**
```python
arr.sort()
print(arr[-2])   # WRONG when duplicates exist
```
`[10, 10, 8, 5]` sorted is `[5, 8, 10, 10]`, so `arr[-2]` gives `10` — but the correct answer is `8`.

**3. Ignoring the word "distinct" in the problem statement**
"Second largest element" and "second largest **distinct** element" can give different answers. For `[5, 5, 4]`: with duplicates allowed the answer is `5`; requiring distinctness the answer is `4`. Always check the wording before coding.

---

## 📊 Complexity Comparison

| Approach | Time | Space |
|---|---|---|
| Sort | O(N log N) | O(1)–O(N) |
| Set + Sort | O(N log N) | O(N) |
| **Single Pass (recommended)** | **O(N)** | **O(1)** |

---

## 🧩 Pattern Family

Part of the **Single Pass / Value Tracking** family:

- Find Maximum
- Find Minimum
- Find Second Largest
- Find Second Smallest
- Find Top Two
- Track Multiple Extremes

General strategy: **Scan → Compare → Update tracked values.**

---

## 🎯 Quick Revision

```
Initialization:
  largest = float('-inf')
  second_largest = float('-inf')

New largest:
  if x > largest:
      second_largest = largest
      largest = x

New second largest:
  elif x > second_largest and x != largest:
      second_largest = x

No valid answer → -1
```

**Memory trick:**
- New biggest? → old biggest becomes second, new number becomes biggest
- Between biggest and second? → new number becomes second
- Equal to biggest? → ignore