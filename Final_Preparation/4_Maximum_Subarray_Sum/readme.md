# 🔥 Maximum Subarray Sum

> **Pattern:** Kadane's Algorithm
> **Difficulty:** Medium
> **Time Complexity:** O(N)
> **Space Complexity:** O(1)

---

## 📌 Problem Name

### Maximum Subarray Sum

---

## 📝 Problem Statement

Given an array of integers, find the **maximum possible sum of a contiguous subarray**.

### Example

```
Input:
9
-2 1 -3 4 -1 2 1 -5 4

Output:
6
```

The subarray producing the maximum sum is:

```
4 + (-1) + 2 + 1 = 6
```

Therefore:

```
Maximum Subarray Sum = 6
```

---

## 🧠 1. Pattern Used

**Kadane's Algorithm**

Kadane's Algorithm is used to solve:

> Maximum sum of a contiguous subarray

It solves the problem in:

```
Time  → O(N)
Space → O(1)
```

This is one of the most important array patterns to recognize for TCS NQT.

---

## 🔍 2. How to Recognize the Pattern

This is the most important part for the exam.

If you see:

- Maximum subarray sum
- Maximum sum of contiguous elements
- Largest sum of consecutive elements
- Find the contiguous portion having maximum sum
- Maximum possible sum from consecutive elements

Think immediately: **🧠 Kadane's Algorithm**

### Recognition Formula

```
MAXIMUM
   +
SUBARRAY / CONTIGUOUS / CONSECUTIVE
   +
SUM
   ↓
KADANE'S ALGORITHM
```

---

## 💡 3. Core Idea

We maintain two variables:

- `current_sum`
- `maximum_sum`

**`current_sum`** represents:
> The maximum sum of a subarray ending at the current position.

**`maximum_sum`** represents:
> The maximum subarray sum found anywhere so far.

For every element `x`, we have two choices:

- **Choice 1 — Start a New Subarray:** `x`
- **Choice 2 — Continue the Previous Subarray:** `current_sum + x`

Therefore:

```python
current_sum = max(x, current_sum + x)
```

Then update the best answer:

```python
maximum_sum = max(maximum_sum, current_sum)
```

---

## 🧮 4. The Core Formula

This is the most important part to remember:

```python
current_sum = max(arr[i], current_sum + arr[i])
maximum_sum = max(maximum_sum, current_sum)
```

That's the core of Kadane's Algorithm.

---

## ⚙️ 5. Step-by-Step Algorithm

**Step 1 — Initialize** (start with the first element):

```python
current_sum = arr[0]
maximum_sum = arr[0]
```

**Step 2 — Traverse the remaining elements:**

```python
for i in range(1, n):
```

**Step 3 — Decide whether to continue or restart:**

```python
current_sum = max(
    arr[i],
    current_sum + arr[i]
)
```

This asks: *Should I start a new subarray here, or continue the previous one?*

**Step 4 — Update the global maximum:**

```python
maximum_sum = max(
    maximum_sum,
    current_sum
)
```

**Step 5 — Print the answer:**

```python
print(maximum_sum)
```

---

## 🐍 6. Optimal Python Code — TCS NQT Style

```python
n = int(input())
arr = list(map(int, input().split()))

current_sum = arr[0]
maximum_sum = arr[0]

for i in range(1, n):
    current_sum = max(arr[i], current_sum + arr[i])
    maximum_sum = max(maximum_sum, current_sum)

print(maximum_sum)
```

This is the standard version you should know for TCS NQT. It is:

- O(N)
- O(1) extra space
- Simple
- Easy to remember
- Handles negative numbers correctly
- Does not require an additional array

---

## ⚠️ 7. Why Initialize With `arr[0]`?

Do not blindly write:

```python
maximum_sum = 0
```

This can fail when all numbers are negative.

Example: `[-5, -2, -8]`

The correct answer is `-2`, **not** `0`.

Therefore initialize using the first array element:

```python
current_sum = arr[0]
maximum_sum = arr[0]
```

This allows Kadane's Algorithm to correctly handle:

- Positive numbers
- Negative numbers
- Zero
- Mixed values

---

## 🧪 8. Example 1

**Input**
```
9
-2 1 -3 4 -1 2 1 -5 4
```

**Output**
```
6
```

The maximum-sum subarray is `[4, -1, 2, 1]`, with sum `4 + (-1) + 2 + 1 = 6`.

---

## 🔬 9. Dry Run

Given: `arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

Initially: `current_sum = -2`, `maximum_sum = -2`

| Step | x  | Compare                | current_sum | maximum_sum |
|------|----|-------------------------|--------------|---------------|
| 1    | 1  | 1 vs (-2+1=-1)          | 1            | 1             |
| 2    | -3 | -3 vs (1-3=-2)          | -2           | 1             |
| 3    | 4  | 4 vs (-2+4=2)           | 4            | 4             |
| 4    | -1 | -1 vs (4-1=3)           | 3            | 4             |
| 5    | 2  | 2 vs (3+2=5)            | 5            | 5             |
| 6    | 1  | 1 vs (5+1=6)            | 6            | 6             |
| 7    | -5 | -5 vs (6-5=1)           | 1            | 6             |
| 8    | 4  | 4 vs (1+4=5)            | 5            | 6             |

---

## 📊 10. Complete Dry Run Table

| Index | Element | current_sum | maximum_sum |
|-------|---------|--------------|---------------|
| 0     | -2      | -2           | -2            |
| 1     | 1       | 1            | 1             |
| 2     | -3      | -2           | 1             |
| 3     | 4       | 4            | 4             |
| 4     | -1      | 3            | 4             |
| 5     | 2       | 5            | 5             |
| 6     | 1       | 6            | 6             |
| 7     | -5      | 1            | 6             |
| 8     | 4       | 5            | 6             |

**Final: `maximum_sum = 6`**

---

## 🧪 11. Example 2 — All Negative Numbers

This is an important edge case.

**Input**
```
5
-8 -3 -6 -2 -5
```

The maximum subarray is `[-2]`.

**Output**
```
-2
```

The algorithm correctly returns `-2`.

---

## 🧪 12. Example 3 — All Positive Numbers

**Input**
```
5
1 2 3 4 5
```

The maximum subarray is the entire array: `1 + 2 + 3 + 4 + 5 = 15`

**Output**
```
15
```

---

## 🧪 13. Example 4 — Single Element

**Input**
```
1
-7
```

The only possible subarray is `[-7]`.

**Output**
```
-7
```

This is another reason why initializing from `arr[0]` is correct.

---

## 🧪 14. Example 5 — Maximum Appears in the Middle

**Input**
```
7
-5 -2 4 6 -1 -8 3
```

The maximum subarray is `[4, 6, -1]`, sum = `4 + 6 - 1 = 9`

**Output**
```
9
```

---

## 🚫 15. Why Not Use Brute Force?

A beginner approach might check every possible subarray:

```python
maximum = float('-inf')

for i in range(n):
    total = 0
    for j in range(i, n):
        total += arr[j]
        maximum = max(maximum, total)
```

This works, but it checks many subarrays.

```
Time  → O(N²)
Space → O(1)
```

For large input sizes, this can become too slow.

---

## 🚀 16. Why Kadane Is Better

Kadane's Algorithm does not generate every possible subarray. Instead, at every element it asks:

> Should I continue the current subarray or start a new one here?

The decision is:

```python
current_sum = max(arr[i], current_sum + arr[i])
```

This reduces the solution to `O(N)` time and `O(1)` space.

---

## 🧠 17. Understanding `current_sum`

This is the part that many beginners misunderstand.

`current_sum` does **not** mean: *Sum of everything seen so far.*

It means: **Maximum sum of a subarray that ends exactly at the current index.**

Example: `arr = [-2, 1, -3, 4]`

At `4`: `current_sum = 4`, because the best subarray ending at `4` is `[4]`. The previous negative sum is not worth carrying forward.

This is why we compare `arr[i]` against `current_sum + arr[i]`.

---

## 🔥 18. The Key Decision

```
current element
      ↓
Can previous subarray help?
      ↓
 ┌────┴────┐
 ↓         ↓
 YES       NO
 ↓         ↓
continue  restart
```

Mathematically:

```python
current_sum = max(
    arr[i],
    current_sum + arr[i]
)
```

This single decision is the heart of Kadane's Algorithm.

---

## 🎯 19. Pattern Recognition Example

Suppose TCS gives:

> A company records its daily profit and loss. Find the maximum total profit obtainable over a continuous sequence of days.

Don't focus on the story. Convert it into:

```
Daily values + Continuous sequence + Maximum sum
        ↓
Kadane's Algorithm
```

This is the type of pattern recognition you should develop for TCS NQT.

---

## ⚠️ 20. Important TCS Variations

The standard problem can be modified.

**Variation 1 — Find Maximum Sum**
Pattern: Kadane's Algorithm

**Variation 2 — Find Starting and Ending Indices**
Find the start and end positions of the maximum-sum subarray.
Pattern: Kadane + Index Tracking (needs `start`, `end`, `temp_start`)

**Variation 3 — Print the Actual Subarray**
Instead of only returning `6`, you may need `4 -1 2 1`. Requires Kadane plus start/end index tracking.

**Variation 4 — Maximum Product Subarray**
⚠️ Not standard Kadane. Requires tracking `current_max` and `current_min`, because a negative number can turn a minimum product into a maximum product.

**Variation 5 — Maximum Circular Subarray**
Requires a modified Kadane approach. The standard `current_sum` / `maximum_sum` solution alone is not enough.

---

## 🧩 21. Pattern Family

Maximum Subarray Sum belongs to the Kadane / Dynamic Tracking family:

```
Kadane
│
├── Maximum Subarray Sum
│
├── Maximum Circular Subarray
│
├── Maximum Subarray With Indices
│
└── Maximum Subarray With Actual Elements
```

Related but different: **Maximum Product Subarray** — requires tracking both `current_max` and `current_min`.

---

## ⚠️ 22. Important Edge Cases

- **All negative:** `[-8, -3, -6, -2]` → `-2`
- **All positive:** `[1, 2, 3, 4]` → `10`
- **Single element:** `[-7]` → `-7`
- **Single zero:** `[0]` → `0`
- **Mixed values:** `[-2, 1, -3, 4, -1, 2, 1]` → `6`

---

## 📊 23. Complexity Comparison

| Approach            | Time  | Space |
|----------------------|-------|-------|
| Brute Force           | O(N²) | O(1)  |
| Kadane's Algorithm    | O(N)  | O(1)  |

The preferred solution is **Kadane's Algorithm**.

---

## 🎯 24. TCS NQT Quick Revision

- **Problem:** Find maximum sum of a contiguous subarray.
- **Pattern:** Kadane's Algorithm
- **Variables:** `current_sum`, `maximum_sum`
- **Initialization:**
  ```python
  current_sum = arr[0]
  maximum_sum = arr[0]
  ```
- **Core Formula:**
  ```python
  current_sum = max(arr[i], current_sum + arr[i])
  maximum_sum = max(maximum_sum, current_sum)
  ```
- **Complexity:** Time → O(N), Space → O(1)

---

## 🧠 25. Final Memory Trick

Don't memorize the entire program. Remember:

```
MAXIMUM + CONTIGUOUS SUBARRAY + SUM
              ↓
            KADANE
```

Then remember the two decisions:

1. Continue previous subarray?
2. Start a new subarray?

Which becomes:

```python
current_sum = max(arr[i], current_sum + arr[i])
maximum_sum = max(maximum_sum, current_sum)
```

---

## 🔥 Final Takeaway

```
                 Current Element
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
        Start New           Continue Old
        Subarray             Subarray
              ↓                 ↓
            arr[i]      current_sum + arr[i]
              └────────┬────────┘
                       ↓
                     MAX
                       ↓
                current_sum
                       ↓
                Update Global
                   Maximum
                       ↓
                maximum_sum
```

**The exam trigger is:**

```
MAXIMUM + SUBARRAY + CONTIGUOUS/CONSECUTIVE + SUM
                    ↓
            KADANE'S ALGORITHM
                    ↓
         O(N) TIME, O(1) SPACE
```

🔥 **Key rule:** `current_sum` means the best subarray sum ending at the current index, while `maximum_sum` means the best subarray sum found anywhere so far.