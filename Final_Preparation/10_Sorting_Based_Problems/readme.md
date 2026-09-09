# 🔥 10. Sorting-Based Problems

Sorting is **not one single problem** in TCS NQT.

It is a **problem-solving pattern** that appears in many different forms.

The key skill is not simply knowing:

```python
arr.sort()
```

The key skill is recognizing:

> **"The problem is asking me to establish an order. Can sorting simplify the solution?"**

A common TCS NQT-style problem is **sorting pairs of numbers** according to their values.

---

# 1. Problem Name

## 🔥 Sort Pairs of Numbers

You are given `N` pairs of integers.

Sort the pairs in **ascending order** according to these rules:

1. Compare the **first number**.
2. If the first numbers are equal, compare the **second number**.

### Example

Input:

```text
4
2 3
1 5
2 1
1 2
```

Output:

```text
1 2
1 5
2 1
2 3
```

---

# 2. Pattern Used

## 🧠 Pattern: Sorting

The general structure is:

```text
Input
   ↓
Store elements
   ↓
Define ordering rule
   ↓
Sort
   ↓
Process / Print
```

For pairs:

```text
(a, b)
```

Python can compare tuples automatically.

For example:

```python
(a1, b1) < (a2, b2)
```

Python compares them **lexicographically**:

```text
First value
    ↓
If equal
    ↓
Second value
```

Therefore:

```python
pairs.sort()
```

automatically sorts pairs by:

```text
first value → second value
```

in ascending order.

---

# 3. How to Recognize the Pattern

Whenever you see words such as:

### 🔑 Strong Sorting Signals

* sort
* arrange
* ascending order
* descending order
* increasing order
* decreasing order
* smallest first
* largest first
* rank
* order the elements
* arrange according to
* sort based on
* sort by first value
* sort by second value
* minimum/maximum after rearrangement

Think:

> **"Is the problem asking me to change or establish the order of the elements?"**

If yes, **consider sorting immediately.**

---

## Example 1 — Ascending Order

> Arrange the numbers in ascending order.

Think:

```text
SORT
```

Code:

```python
arr.sort()
```

---

## Example 2 — Descending Order

> Arrange the numbers from largest to smallest.

Think:

```text
SORT + REVERSE
```

Code:

```python
arr.sort(reverse=True)
```

---

## Example 3 — Sort Students by Marks

> Sort students according to their marks.

If:

```python
students = [
    ("Rahul", 85),
    ("Amit", 92),
    ("Sourav", 78)
]
```

Marks are at index `1`.

So:

```python
students.sort(key=lambda x: x[1])
```

---

## Example 4 — Sort Pairs by First Value

```python
pairs.sort(key=lambda x: x[0])
```

Here:

```text
x[0] → first value
```

---

## Example 5 — Sort Pairs by First, Then Second

If the requirement is:

> Sort pairs by first value. If equal, sort by second value.

Then:

```python
pairs.sort()
```

is enough.

---

# 4. Solve Approach

For the **Sort Pairs of Numbers** problem:

## Step 1 — Read `N`

```python
n = int(input())
```

---

## Step 2 — Store All Pairs

```python
pairs = []

for _ in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))
```

Each pair is stored as a tuple:

```text
(a, b)
```

---

## Step 3 — Sort

```python
pairs.sort()
```

Python automatically applies:

```text
First value
     ↓
If equal
     ↓
Second value
```

---

## Step 4 — Print

```python
for a, b in pairs:
    print(a, b)
```

---

# 5. Optimal Python Code — TCS NQT Style

```python
n = int(input())

pairs = []

for _ in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))

pairs.sort()

for a, b in pairs:
    print(a, b)
```

---

## Why This Code Is Good for TCS NQT

It is:

* Short
* Easy to remember
* Efficient
* Easy to debug
* Uses Python's built-in sorting
* Avoids unnecessary nested loops

### Important

You generally **do not need to manually implement Bubble Sort, Selection Sort, or Insertion Sort** unless the question specifically asks you to implement a sorting algorithm.

For a normal coding problem:

```python
arr.sort()
```

is usually the better choice.

---

# 6. Examples

## Example 1 — Basic

### Input

```text
4
2 3
1 5
2 1
1 2
```

### Output

```text
1 2
1 5
2 1
2 3
```

---

# Example 2 — Duplicate First Values

### Input

```text
5
3 8
1 9
3 2
1 4
2 7
```

### Output

```text
1 4
1 9
2 7
3 2
3 8
```

Notice:

```text
3 8
3 2
```

becomes:

```text
3 2
3 8
```

because the first values are equal:

```text
3 == 3
```

So Python compares the second values:

```text
2 < 8
```

Therefore:

```text
(3,2) comes before (3,8)
```

---

# Example 3 — Negative Numbers

### Input

```text
4
-2 5
1 3
-2 1
0 4
```

### Output

```text
-2 1
-2 5
0 4
1 3
```

Sorting works naturally with negative values.

---

# 7. Dry Run

Consider:

```text
4
2 3
1 5
2 1
1 2
```

Initially:

```python
pairs = [
    (2, 3),
    (1, 5),
    (2, 1),
    (1, 2)
]
```

Call:

```python
pairs.sort()
```

---

## Step 1 — Compare First Values

The first values are:

```text
2
1
2
1
```

Therefore, pairs beginning with `1` come first.

Conceptually:

```text
(1,5)
(1,2)
(2,3)
(2,1)
```

---

## Step 2 — Compare Equal First Values

For:

```text
(1,5)
(1,2)
```

the first values are equal:

```text
1 == 1
```

So Python compares:

```text
5 vs 2
```

Since:

```text
2 < 5
```

we get:

```text
(1,2)
(1,5)
```

---

Similarly:

```text
(2,3)
(2,1)
```

becomes:

```text
(2,1)
(2,3)
```

---

## Final Sorted List

```text
(1,2)
(1,5)
(2,1)
(2,3)
```

Output:

```text
1 2
1 5
2 1
2 3
```

---

# 8. How Python Tuple Sorting Works

This is extremely important for this problem.

Suppose:

```python
pairs = [
    (2, 3),
    (1, 5),
    (2, 1),
    (1, 2)
]
```

When you call:

```python
pairs.sort()
```

Python effectively follows:

```text
Compare first elements
        ↓
Are they different?
   ↙           ↘
 YES           NO
 ↓              ↓
Use first       Compare second
value            values
```

So:

```text
(1,2)
(1,5)
```

is ordered using:

```text
1 == 1
```

then:

```text
2 < 5
```

This is called **lexicographical ordering**.

---

# 9. Time Complexity

Python's `.sort()` uses **Timsort**.

For `N` elements:

### Time Complexity

```text
O(N log N)
```

Therefore:

> **Sorting N elements → O(N log N)**

---

# 10. Space Complexity

We store `N` pairs:

```text
O(N)
```

Python's sorting algorithm also uses additional internal memory.

For NQT purposes, remember:

```text
Time  → O(N log N)
Space → O(N)
```

---

# 🧠 11. Sorting Variations You Must Recognize

This is where TCS can change the wording without changing the underlying pattern.

---

## Variation 1 — Ascending Order

```python
arr.sort()
```

Example:

```python
arr = [5, 2, 8, 1]

arr.sort()

print(arr)
```

Output:

```text
[1, 2, 5, 8]
```

---

## Variation 2 — Descending Order

```python
arr.sort(reverse=True)
```

Example:

```python
arr = [5, 2, 8, 1]

arr.sort(reverse=True)

print(arr)
```

Output:

```text
[8, 5, 2, 1]
```

---

## Variation 3 — Sort by Second Value

Suppose:

```python
pairs = [
    (10, 5),
    (20, 2),
    (30, 8)
]
```

Sort according to the second value:

```python
pairs.sort(key=lambda x: x[1])
```

Result:

```text
(20,2)
(10,5)
(30,8)
```

Remember:

```text
x[0] → first value
x[1] → second value
```

---

## Variation 4 — Sort by Length

For strings:

```python
words.sort(key=len)
```

Example:

```python
words = ["apple", "cat", "banana", "dog"]

words.sort(key=len)
```

Result:

```text
cat
dog
apple
banana
```

Pattern:

```text
SORT BY PROPERTY
```

---

## Variation 5 — Sort by Absolute Value

```python
arr.sort(key=abs)
```

Example:

```python
arr = [-10, 3, -2, 7]

arr.sort(key=abs)
```

Result:

```text
[-2, 3, 7, -10]
```

Because the absolute values are:

```text
2, 3, 7, 10
```

---

## Variation 6 — Multiple Sorting Conditions

Suppose:

> Sort by first value, and if equal, sort by second value.

Use:

```python
arr.sort(key=lambda x: (x[0], x[1]))
```

For normal ascending tuple pairs:

```python
arr.sort()
```

already does this.

---

## Variation 7 — Descending by First Value

```python
arr.sort(key=lambda x: x[0], reverse=True)
```

Example:

```python
arr = [
    (2, 5),
    (5, 1),
    (3, 7)
]

arr.sort(key=lambda x: x[0], reverse=True)
```

Result:

```text
(5,1)
(3,7)
(2,5)
```

---

# 🚨 12. Important: `sort()` vs `sorted()`

You should know the difference.

## `sort()`

Changes the original list:

```python
arr.sort()
```

Example:

```python
arr = [3, 1, 2]

arr.sort()

print(arr)
```

Output:

```text
[1, 2, 3]
```

---

## `sorted()`

Creates and returns a new sorted list:

```python
arr = [3, 1, 2]

new_arr = sorted(arr)

print(new_arr)
```

Output:

```text
[1, 2, 3]
```

Original:

```python
arr
```

still remains:

```text
[3, 1, 2]
```

### NQT shortcut

If you do not need the original order:

```python
arr.sort()
```

is simple and convenient.

If you need both versions:

```python
new_arr = sorted(arr)
```

---

# ⚠️ 13. Common Mistakes

## Mistake 1 — Sorting only the first values

Incorrect thinking:

```text
Sort first values separately.
```

This can destroy the relationship between the pair elements.

A pair:

```text
(2, 10)
```

must remain together.

---

## Mistake 2 — Forgetting the second condition

If the problem says:

> Sort by first value, and if equal, sort by second value.

Do not only sort by:

```python
key=lambda x: x[0]
```

unless the problem does **not** specify the tie-breaking rule.

For the given problem:

```python
pairs.sort()
```

is enough.

---

## Mistake 3 — Using Nested Loops Unnecessarily

You might manually write:

```text
for i
    for j
        compare
        swap
```

This is unnecessary for a normal sorting problem.

Prefer:

```python
arr.sort()
```

unless manual sorting is explicitly required.

---

## Mistake 4 — Using a Set

A set is for uniqueness:

```python
set(arr)
```

Sorting is for ordering:

```python
sorted(arr)
```

Do not confuse:

```text
Remove duplicates → Set
Arrange elements → Sorting
```

---

# 🔥 14. Sorting vs Other Patterns

Sorting appears together with many other patterns.

The key is identifying **what the problem actually needs**.

---

## Pair Sum

> Find two numbers whose sum equals a target.

Think:

```text
Hashing / Two Pointer
```

Not automatically sorting.

---

## Maximum Contiguous Sum

> Find the maximum sum of a contiguous subarray.

Think:

```text
Kadane's Algorithm
```

---

## Rearrange Elements

> Arrange elements to satisfy a particular ordering condition.

Think:

```text
Sorting
```

Potentially combined with:

```text
Two Pointer
```

or another technique.

---

## Ranking

> Find the smallest, largest, rank, ordered position, etc.

Think:

```text
Sorting
```

But always check whether a more efficient direct method exists.

---

# 🧠 15. Pattern Recognition Shortcut

When you see:

> **"Arrange / order / rank / smallest / largest / according to..."**

ask:

```text
Does ORDER matter?
       ↓
      YES
       ↓
Can sorting simplify the problem?
       ↓
      YES
       ↓
SORTING PATTERN
```

---

# 🔥 16. Important Distinction

Do not memorize:

> **"Sorting problem = `arr.sort()`."**

Instead memorize:

> **"The problem requires a particular order. Check whether sorting can establish that order and simplify the remaining work."**

Sorting is a **tool/pattern**, not the entire solution.

Sometimes the final solution is:

```text
Sorting
   +
Two Pointer
```

or:

```text
Sorting
   +
Greedy
```

or:

```text
Sorting
   +
Binary Search
```

So after sorting, always ask:

> **"What does the sorted order allow me to do efficiently?"**

---

# 🎯 17. TCS NQT Recognition Table

| Problem Wording                 | Pattern                 |
| ------------------------------- | ----------------------- |
| Arrange in ascending order      | Sorting                 |
| Arrange in descending order     | Sorting                 |
| Find smallest elements in order | Sorting                 |
| Find largest elements in order  | Sorting                 |
| Rank elements                   | Sorting                 |
| Sort according to a property    | Sorting + `key=`        |
| Sort pairs                      | Tuple Sorting           |
| Sort by first value             | `key=lambda x: x[0]`    |
| Sort by second value            | `key=lambda x: x[1]`    |
| Sort by multiple conditions     | Tuple key               |
| Pair sum in sorted array        | Sorting + Two Pointer   |
| Search after sorting            | Sorting + Binary Search |

---

# 🎯 18. What to Remember for Your NQT Sheet

Master these **5 forms**:

| Type                 | Pattern                  |
| -------------------- | ------------------------ |
| Normal ascending     | `arr.sort()`             |
| Descending           | `arr.sort(reverse=True)` |
| Sort by one property | `key=`                   |
| Sort pairs           | `pairs.sort()`           |
| Multiple rules       | `key=lambda x: (...)`    |

---

# ⚡ 19. Quick Revision

### Basic Sorting

```python
arr.sort()
```

### Descending

```python
arr.sort(reverse=True)
```

### Sort by First Value

```python
arr.sort(key=lambda x: x[0])
```

### Sort by Second Value

```python
arr.sort(key=lambda x: x[1])
```

### Sort by Multiple Conditions

```python
arr.sort(key=lambda x: (x[0], x[1]))
```

### Sort by Length

```python
words.sort(key=len)
```

### Sort by Absolute Value

```python
arr.sort(key=abs)
```

---

# 🧠 20. Memory Trick

Remember:

```text
SORTING
   ↓
ORDER MATTERS
   ↓
ARRANGE / RANK / ASCENDING / DESCENDING
   ↓
SORT
```

For pairs:

```text
PAIR
 ↓
FIRST VALUE
 ↓
IF EQUAL
 ↓
SECOND VALUE
 ↓
TUPLE SORTING
```

The main formula:

```text
SORTING → ESTABLISH ORDER → SIMPLIFY THE NEXT STEP
```

---

# 🚀 Final NQT Cheat Sheet

```text
Normal ascending
→ arr.sort()

Descending
→ arr.sort(reverse=True)

Sort by property
→ arr.sort(key=...)

Sort pairs
→ pairs.sort()

Multiple conditions
→ arr.sort(key=lambda x: (...))

N elements
→ O(N log N)
```

### 🔥 Final Pattern Recognition

```text
"Arrange?"
"Sort?"
"Rank?"
"Ascending?"
"Descending?"
"According to?"
"Smallest first?"
"Largest first?"
        ↓
   THINK SORTING
        ↓
   CHECK THE RULE
        ↓
   CHOOSE sort() / key=
        ↓
   PROCESS THE SORTED DATA
```

> **SORTING → ORDER THE DATA → USE THE ORDER TO MAKE THE REST OF THE PROBLEM EASY**
