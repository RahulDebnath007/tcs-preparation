# 🔥 Move All Zeros to the End

> **Pattern:** Two Pointer / In-Place Array Manipulation
> **Difficulty:** Easy
> **Time Complexity:** O(N)
> **Space Complexity:** O(1)

---

## 📌 Problem Name

### Move All Zeros to the End

---

## 📝 Problem Statement

Given an array, move all `0`s to the end while maintaining the **relative order of the non-zero elements**.

### Example

```
Input:
[4, 5, 0, 1, 9, 0, 5, 0]

Output:
[4, 5, 1, 9, 5, 0, 0, 0]
```

Notice that the non-zero elements:

```
4 → 5 → 1 → 9 → 5
```

remain in the same relative order.

---

## 🧠 1. Pattern Used

**Two Pointer / Position Pointer**

The main idea is to maintain a pointer: `pos`

- `pos` represents the position where the next non-zero element should be placed.
- We use another pointer `i` to scan the array.

So:

```
i   → scans the array
pos → tells us where the next non-zero element goes
```

---

## 🔍 2. How to Recognize the Pattern

When you see problems involving:

- Move all zeros to the end
- Move all zeros to the beginning
- Shift specific elements
- Rearrange an array
- Remove unwanted elements while preserving order
- Move negative/positive elements
- Move all occurrences of X
- Keep valid elements in their original order

Think: 🧠 **Two Pointer / Position Pointer**

Especially when the problem expects:
- O(N) time
- O(1) extra space

---

## 💡 3. Core Idea

Consider:

```
arr = [4, 5, 0, 1, 9, 0, 5, 0]
```

Start with `pos = 0`. Now scan the array from left to right.

Whenever we find a non-zero element:

```python
arr[pos] = arr[i]
pos += 1
```

We are effectively saying: *"This is a valid element. Put it at the next available position."*

After all non-zero elements are placed, every remaining position should contain 0.

---

## 🔢 4. Visual Explanation

Initial array:

```
4  5  0  1  9  0  5  0
↑
pos
```

**Process 4** — non-zero, place at pos:

```
4  _  _  _  _  _  _  _
   ↑
  pos
```

**Process 5** — non-zero, place at pos:

```
4  5  _  _  _  _  _  _
      ↑
     pos
```

**Process 0** — ignore, pos does not move:

```
4  5  _  _  _  _  _  _
      ↑
     pos
```

**Process 1** — place at pos:

```
4  5  1  _  _  _  _  _
         ↑
        pos
```

**Process 9**:

```
4  5  1  9  _  _  _  _
            ↑
           pos
```

**Process 5**:

```
4  5  1  9  5  _  _  _
               ↑
              pos
```

Finally, fill all remaining positions with 0:

```
4  5  1  9  5  0  0  0
```

---

## ⚙️ 5. Step-by-Step Algorithm

**Step 1 — Initialize pos**
```python
pos = 0
```
`pos` tells us where the next non-zero element should go.

**Step 2 — Traverse the array**
```python
for i in range(n):
```

**Step 3 — Check whether the element is non-zero**
```python
if arr[i] != 0:
```

**Step 4 — Place the non-zero element**
```python
arr[pos] = arr[i]
```

**Step 5 — Move pos**
```python
pos += 1
```

**Step 6 — Fill remaining positions with zeros**

After processing all elements:
```python
while pos < n:
    arr[pos] = 0
    pos += 1
```

---

## 🐍 6. Optimal Python Code — TCS NQT Style

```python
n = int(input())
arr = list(map(int, input().split()))

pos = 0

# Place all non-zero elements at the front
for i in range(n):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1

# Fill remaining positions with zeros
while pos < n:
    arr[pos] = 0
    pos += 1

print(*arr)
```

This is a good TCS NQT implementation because it is:

- Simple
- Easy to remember
- O(N)
- In-place
- O(1) extra space
- Free of unnecessary libraries

---

## 🧪 7. Example 1

**Input**
```
8
4 5 0 1 9 0 5 0
```

**Output**
```
4 5 1 9 5 0 0 0
```

**Explanation**

The non-zero elements are: `4 5 1 9 5`. They maintain their original relative order. The remaining three positions are filled with `0 0 0`.

---

## 🔬 8. Dry Run

Given:
```
arr = [4, 5, 0, 1, 9, 0, 5, 0]
```

Initially: `pos = 0`

| Iteration | i | arr[i] | Action | pos after |
|---|---|---|---|---|
| 1 | 0 | 4 | non-zero → `arr[0]=4` | 1 |
| 2 | 1 | 5 | non-zero → `arr[1]=5` | 2 |
| 3 | 2 | 0 | ignore | 2 |
| 4 | 3 | 1 | non-zero → `arr[2]=1` | 3 |
| 5 | 4 | 9 | non-zero → `arr[3]=9` | 4 |
| 6 | 5 | 0 | ignore | 4 |
| 7 | 6 | 5 | non-zero → `arr[4]=5` | 5 |
| 8 | 7 | 0 | ignore | 5 |

**Fill Remaining Positions**

Positions 5, 6, 7 are filled with zero.

**Final array:**
```
4 5 1 9 5 0 0 0
```

---

## 🧪 9. Example 2 — All Zeros

**Input**
```
5
0 0 0 0 0
```

There are no non-zero elements. Therefore:

**Output**
```
0 0 0 0 0
```

---

## 🧪 10. Example 3 — No Zeros

**Input**
```
5
1 2 3 4 5
```

Every element is already non-zero. Nothing needs to move.

**Output**
```
1 2 3 4 5
```

---

## 🧪 11. Example 4 — Zeros at the Beginning

**Input**
```
7
0 0 3 4 0 5 6
```

Non-zero elements: `3 4 5 6`

**Output**
```
3 4 5 6 0 0 0
```

---

## 🚫 12. Why Not Use Another Array?

A simpler solution could be:

```python
result = []

for x in arr:
    if x != 0:
        result.append(x)

while len(result) < n:
    result.append(0)
```

This works correctly. However, it uses O(N) extra space. Our solution modifies the original array directly, so Extra Space = O(1). This is preferable when the problem expects an in-place solution.

---

## 🚫 13. Why Not Repeatedly Remove Zeros?

Avoid approaches like:

```python
while 0 in arr:
    arr.remove(0)
    arr.append(0)
```

The problem is that operations such as `arr.remove(0)` can take O(N) time. Repeating them can lead to O(N²) time complexity. There is no reason to accept that when an O(N) solution exists.

---

## 📊 14. Complexity Analysis

**Optimal Solution**
```
Time Complexity  : O(N)
Space Complexity : O(1)
```

Why? The array is scanned once — O(N) — and the rearrangement is performed directly inside the same array. No additional array is required.

---

## 🧠 15. Pattern Recognition Shortcut

When you see:

```
ARRAY
+
MOVE / REARRANGE
+
PRESERVE ORDER
```

think: **Two Pointer / Position Pointer**

The core skeleton is:

```python
pos = 0

for i in range(n):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1

while pos < n:
    arr[pos] = 0
    pos += 1
```

---

## 🎯 16. The Most Important Concept

Don't memorize the entire code. Memorize what `pos` means:

> `pos` = the position where the next valid element should go.

For this problem, valid element = non-zero element. Therefore:

```
pos → next position for a non-zero element
```

---

## 🔥 17. TCS NQT Variations

TCS can modify this problem in several ways.

**Variation 1 — Move Zeros to Beginning**

Instead of `non-zero → zeros`, you may need `zeros → non-zero`.

**Variation 2 — Move Negative Numbers**

Example: `[1, -2, 3, -4, 5]` — Move negative numbers to one side. This can involve a two-pointer strategy.

**Variation 3 — Move Even Numbers**

Example: `[1, 2, 3, 4, 5, 6]` — Rearrange according to a condition while preserving order if required.

**Variation 4 — Remove a Particular Value**

Example: `arr = [2, 3, 2, 4, 2]` — Remove all occurrences of 2 while preserving the order of the remaining elements. The same position-pointer idea can be used.

**Variation 5 — Move All Occurrences of X**

Example: `arr = [4, 2, 5, 2, 7, 2]`, `X = 2` — Move all 2s to the end while preserving the relative order of other elements.

---

## 🧩 18. Pattern Family

This problem belongs to the Two Pointer / In-Place Rearrangement family:

```
Two Pointer
│
├── Move Zeros
│
├── Move Elements
│
├── Remove Duplicates
│
├── Remove Specific Value
│
├── Partition Array
│
├── Move Negatives
│
└── Rearrange Based on Condition
```

The exact implementation changes, but the underlying idea is:

> Scan → identify valid elements → place them using a pointer

---

## ⚠️ 19. Important Edge Cases

Always consider:

- Empty array: `[]`
- All zeros: `[0, 0, 0]`
- No zeros: `[1, 2, 3]`
- Zero at beginning: `[0, 1, 2]`
- Zero at end: `[1, 2, 0]`
- Multiple consecutive zeros: `[1, 0, 0, 0, 2]`
- Single element: `[0]` or `[5]`

The position-pointer approach handles all of these naturally.

---

## 📝 20. TCS NQT Quick Revision

| Item | Detail |
|---|---|
| **Problem** | Move all zeros to the end |
| **Requirement** | Preserve relative order of non-zero elements |
| **Pattern** | Two Pointer / Position Pointer |
| **Pointer** | `pos` = next available position for a valid element |
| **Valid Element** | `arr[i] != 0` |
| **Core Operation** | `arr[pos] = arr[i]; pos += 1` |
| **Final Step** | `while pos < n: arr[pos] = 0; pos += 1` |
| **Complexity** | Time → O(N), Space → O(1) |

---

## 🧠 Final Takeaway

The important thing is not memorizing the code. Understand this process:

```
                 Array
                   ↓
             Scan elements
                   ↓
          Is element non-zero?
              ↙          ↘
            YES           NO
             ↓             ↓
       Place at pos      Ignore
             ↓
        pos = pos + 1
             ↓
     Finished scanning?
             ↓
     Fill remaining slots
             ↓
          With zeros
```

The mental trigger for the exam is:

```
MOVE / REMOVE
+
PRESERVE ORDER
+
ARRAY
        ↓
POSITION POINTER
        ↓
O(N) TIME
O(1) SPACE
```

🔥 **Remember:** `pos` is not just a random variable. It represents the next position where a valid element belongs.