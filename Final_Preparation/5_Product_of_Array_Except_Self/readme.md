# 🔥 5. Product of Array Except Self

> One of the most useful **Prefix/Suffix patterns** for TCS NQT.
>
> The key idea is to avoid the brute-force `O(N²)` approach by separating the product into **LEFT × RIGHT**.

---

# 1. Problem Name

## Product of Array Except Self

Given an array of `N` integers, create a new array such that:

```text
answer[i] = product of every element except arr[i]
```

### Example

```text
Input:
5
1 2 3 4 5

Output:
120 60 40 30 24
```

Because:

```text
answer[0] = 2 × 3 × 4 × 5 = 120

answer[1] = 1 × 3 × 4 × 5 = 60

answer[2] = 1 × 2 × 4 × 5 = 40

answer[3] = 1 × 2 × 3 × 5 = 30

answer[4] = 1 × 2 × 3 × 4 = 24
```

---

# 2. Pattern Used

## 🧠 Prefix Product + Suffix Product

For every index:

```text
answer[i]
=
product of everything on the LEFT
×
product of everything on the RIGHT
```

So the main idea is:

```text
LEFT PRODUCT × RIGHT PRODUCT
```

↓

```text
PREFIX + SUFFIX
```

---

# 3. How to Recognize the Pattern

Look for phrases such as:

* Product of all elements except the current element
* Product excluding itself
* For each index, multiply all other elements
* Product of array except self
* Return a product array
* Without using division

The strongest clue is:

> **Everything except the current element.**

Immediately think:

```text
Current element
      ↓
Exclude it
      ↓
LEFT + RIGHT
      ↓
Prefix + Suffix
```

### 🧠 Recognition Formula

```text
FOR EACH INDEX
        +
EVERYTHING EXCEPT CURRENT
        ↓
LEFT + RIGHT
        ↓
PREFIX × SUFFIX
```

---

# 4. Why the Obvious Approach Is Bad

The first solution that may come to mind is:

```python
for i in range(n):
    product = 1

    for j in range(n):
        if i != j:
            product *= arr[j]
```

This works logically.

But for every index, we scan the entire array again.

Therefore:

```text
Time Complexity = O(N²)
```

For large arrays, this is unnecessary.

We can solve the problem in:

```text
O(N)
```

using prefix and suffix products.

---

# 5. Core Idea

Consider:

```text
arr = [1, 2, 3, 4]
```

Suppose we are calculating the answer for index `2`.

The current element is:

```text
3
```

We need every element except `3`:

```text
1 × 2 × 4
```

Split the array around index `2`:

```text
LEFT:
1 × 2

CURRENT:
3

RIGHT:
4
```

Therefore:

```text
answer[2]
=
(1 × 2) × 4

= 8
```

So the general formula becomes:

```text
answer[i] = left_product × right_product
```

---

# 6. First Pass — Store Prefix Products

Instead of creating a separate prefix array, we can use the `answer` array itself.

Consider:

```text
arr = [1, 2, 3, 4]
```

Initially:

```text
answer = [1, 1, 1, 1]
```

Maintain:

```python
prefix = 1
```

The important rule is:

> Store the product of elements **before** the current index.

---

## i = 0

There is nothing to the left.

Therefore:

```text
answer[0] = 1
```

Then include `arr[0]` in the prefix:

```text
prefix = prefix × arr[0]
       = 1 × 1
       = 1
```

---

## i = 1

Elements to the left:

```text
1
```

Therefore:

```text
answer[1] = 1
```

Update prefix:

```text
prefix = 1 × 2
       = 2
```

---

## i = 2

Elements to the left:

```text
1 × 2
```

Therefore:

```text
answer[2] = 2
```

Update:

```text
prefix = 2 × 3
       = 6
```

---

## i = 3

Elements to the left:

```text
1 × 2 × 3
```

Therefore:

```text
answer[3] = 6
```

Update:

```text
prefix = 6 × 4
       = 24
```

After the first pass:

```text
answer = [1, 1, 2, 6]
```

These values represent the product of everything to the **left** of each index.

---

# 7. Second Pass — Multiply Suffix Products

Now traverse the array from:

```text
RIGHT → LEFT
```

Maintain:

```python
suffix = 1
```

For every index:

```python
answer[i] *= suffix
```

Then update:

```python
suffix *= arr[i]
```

The important rule is:

> `suffix` contains the product of elements **after** the current index.

---

# 8. Optimal Python Code — TCS NQT Style

```python
n = int(input())
arr = list(map(int, input().split()))

answer = [1] * n

# Store prefix products
prefix = 1

for i in range(n):
    answer[i] = prefix
    prefix *= arr[i]

# Multiply by suffix products
suffix = 1

for i in range(n - 1, -1, -1):
    answer[i] *= suffix
    suffix *= arr[i]

print(*answer)
```

---

# 9. Why This Solution Is Optimal

We make exactly two passes through the array:

```text
Pass 1 → Prefix
Pass 2 → Suffix
```

Therefore:

```text
Time Complexity = O(N)
```

The `answer` array itself requires `O(N)` space.

We do **not** create separate prefix and suffix arrays.

Therefore:

```text
Auxiliary Space = O(1)
Output Space     = O(N)
```

For TCS NQT, write:

```text
Time:  O(N)
Space: O(N) for output
```

---

# 10. Example

### Input

```text
4
1 2 3 4
```

### Output

```text
24 12 8 6
```

Verification:

```text
answer[0] = 2 × 3 × 4 = 24

answer[1] = 1 × 3 × 4 = 12

answer[2] = 1 × 2 × 4 = 8

answer[3] = 1 × 2 × 3 = 6
```

---

# 11. Dry Run — Prefix Pass

Array:

```text
[1, 2, 3, 4]
```

Initially:

```text
answer = [1, 1, 1, 1]
prefix = 1
```

### i = 0

```text
answer[0] = 1

prefix = 1 × 1
       = 1
```

---

### i = 1

```text
answer[1] = 1

prefix = 1 × 2
       = 2
```

---

### i = 2

```text
answer[2] = 2

prefix = 2 × 3
       = 6
```

---

### i = 3

```text
answer[3] = 6

prefix = 6 × 4
       = 24
```

After prefix pass:

```text
answer = [1, 1, 2, 6]
```

---

# 12. Dry Run — Suffix Pass

Start:

```text
suffix = 1
```

Traverse:

```text
3 → 2 → 1 → 0
```

---

### i = 3

Current:

```text
answer[3] = 6
```

Multiply by suffix:

```text
answer[3] = 6 × 1
          = 6
```

Update:

```text
suffix = 1 × 4
       = 4
```

---

### i = 2

```text
answer[2] = 2 × 4
          = 8
```

Update:

```text
suffix = 4 × 3
       = 12
```

---

### i = 1

```text
answer[1] = 1 × 12
          = 12
```

Update:

```text
suffix = 12 × 2
       = 24
```

---

### i = 0

```text
answer[0] = 1 × 24
          = 24
```

Update:

```text
suffix = 24 × 1
       = 24
```

Final:

```text
[24, 12, 8, 6]
```

---

# 13. Complete Dry Run Table

## Prefix Pass

| Index | `arr[i]` | `prefix` Before | `answer[i]` | `prefix` After |
| ----: | -------: | --------------: | ----------: | -------------: |
|     0 |        1 |               1 |           1 |              1 |
|     1 |        2 |               1 |           1 |              2 |
|     2 |        3 |               2 |           2 |              6 |
|     3 |        4 |               6 |           6 |             24 |

Result:

```text
answer = [1, 1, 2, 6]
```

## Suffix Pass

| Index | `arr[i]` | `suffix` Before | `answer[i]` After | `suffix` After |
| ----: | -------: | --------------: | ----------------: | -------------: |
|     3 |        4 |               1 |                 6 |              4 |
|     2 |        3 |               4 |                 8 |             12 |
|     1 |        2 |              12 |                12 |             24 |
|     0 |        1 |              24 |                24 |             24 |

Final:

```text
24 12 8 6
```

---

# 14. Example 2 — Array Contains Zero

This is one of the reasons the prefix/suffix method is powerful.

### Input

```text
4
1 2 0 4
```

### Output

```text
0 0 8 0
```

Verification:

```text
answer[0] = 2 × 0 × 4 = 0

answer[1] = 1 × 0 × 4 = 0

answer[2] = 1 × 2 × 4 = 8

answer[3] = 1 × 2 × 0 = 0
```

The algorithm handles zero automatically.

No special zero-count logic is required.

---

# 15. Example 3 — Two Zeros

### Input

```text
5
1 0 3 0 5
```

### Output

```text
0 0 0 0 0
```

Why?

For every position, there is at least one zero among the **other** elements.

Therefore every product becomes zero.

The prefix/suffix algorithm handles this naturally.

---

# 16. Example 4 — Single Element

Consider:

```text
arr = [7]
```

There are no other elements.

Depending on the exact problem specification, the mathematical empty product is usually treated as:

```text
1
```

So the algorithm produces:

```text
[1]
```

However, always check the TCS problem statement if it specifies a different expected output for `N = 1`.

---

# 17. Why Not Use Division?

A tempting approach is:

```python
total_product = 1

for x in arr:
    total_product *= x

for i in range(n):
    answer[i] = total_product // arr[i]
```

For an array without zero, this can work.

For example:

```text
arr = [1, 2, 3, 4]

total_product = 24
```

Then:

```text
24 / 1 = 24
24 / 2 = 12
24 / 3 = 8
24 / 4 = 6
```

But there are important problems.

### Problem 1 — Zero

For:

```text
[1, 2, 0, 4]
```

the total product is:

```text
0
```

and division by the current element fails when the current element is `0`.

### Problem 2 — Problem Restrictions

Many versions explicitly say:

> Do not use division.

Therefore, the safer interview/TCS pattern is:

```text
PREFIX × SUFFIX
```

---

# 18. Brute Force vs Optimal

## Brute Force

```python
for i in range(n):
    product = 1

    for j in range(n):
        if i != j:
            product *= arr[j]
```

Complexity:

```text
Time  = O(N²)
Space = O(N)
```

---

## Prefix + Suffix

```python
prefix = 1

for i in range(n):
    answer[i] = prefix
    prefix *= arr[i]

suffix = 1

for i in range(n - 1, -1, -1):
    answer[i] *= suffix
    suffix *= arr[i]
```

Complexity:

```text
Time  = O(N)
Space = O(N) including output
```

Therefore:

```text
O(N²)  ❌
O(N)   ✅
```

---

# 19. The Most Important Concept

The most important thing to understand is what `answer[i]` contains **between the two passes**.

After the prefix pass:

```text
answer[i]
=
product of everything LEFT of i
```

During the suffix pass:

```text
answer[i]
=
LEFT PRODUCT × RIGHT PRODUCT
```

Therefore:

```text
                 arr[i]
                   ↓
        ┌──────────┴──────────┐
        ↓                     ↓
   LEFT SIDE              RIGHT SIDE
        ↓                     ↓
 Prefix Product          Suffix Product
        └──────────┬──────────┘
                   ↓
             multiply them
                   ↓
               answer[i]
```

---

# 20. Pattern Recognition Shortcut

When you see:

```text
FOR EACH INDEX
+
EVERYTHING EXCEPT CURRENT
```

ask yourself:

> **Can I divide the array into LEFT and RIGHT?**

If yes:

```text
LEFT
 ↓
PREFIX

RIGHT
 ↓
SUFFIX

PREFIX × SUFFIX
 ↓
ANSWER
```

---

# 21. Core Skeleton to Memorize

```python
answer = [1] * n

prefix = 1

for i in range(n):
    answer[i] = prefix
    prefix *= arr[i]

suffix = 1

for i in range(n - 1, -1, -1):
    answer[i] *= suffix
    suffix *= arr[i]
```

### 🧠 One-Line Memory Trick

> **First remember LEFT, then multiply RIGHT.**

```text
LEFT  → Prefix
RIGHT → Suffix
```

---

# 22. TCS NQT Pattern Recognition

Use this decision process during the exam:

```text
Question
   ↓
"For every index..."
   ↓
"Product of everything except current"
   ↓
Can I split around current?
   ↓
LEFT + RIGHT
   ↓
Prefix + Suffix
   ↓
Two passes
   ↓
O(N)
```

---

# 23. Common Mistakes

### ❌ Mistake 1 — Including the current element

Wrong:

```text
answer[i] = prefix × suffix × arr[i]
```

The current element must be excluded.

Correct:

```text
answer[i] = prefix × suffix
```

---

### ❌ Mistake 2 — Updating prefix before storing it

Wrong:

```python
prefix *= arr[i]
answer[i] = prefix
```

This includes `arr[i]` in its own answer.

Correct:

```python
answer[i] = prefix
prefix *= arr[i]
```

---

### ❌ Mistake 3 — Updating suffix before multiplying

Wrong:

```python
suffix *= arr[i]
answer[i] *= suffix
```

This includes the current element.

Correct:

```python
answer[i] *= suffix
suffix *= arr[i]
```

---

### ❌ Mistake 4 — Using O(N²)

If the question asks for every index, don't immediately use a nested loop.

First ask:

```text
Can I reuse previous products?
```

Here the answer is yes.

---

### ❌ Mistake 5 — Using division without checking constraints

Division may fail because of:

```text
zero
```

or because the problem explicitly prohibits it.

---

# 24. Variations of the Pattern

### Variation 1 — Product Except Self

```text
Prefix × Suffix
```

---

### Variation 2 — Sum Except Self

Same general left/right idea can sometimes be used:

```text
Prefix Sum + Suffix Sum
```

---

### Variation 3 — Maximum Except Self

May require:

```text
Prefix Maximum + Suffix Maximum
```

depending on the exact problem.

---

### Variation 4 — Product of a Range

Prefix products can sometimes help, but zeros and integer overflow may require additional handling.

---

# 25. Pattern Family

```text
PREFIX / SUFFIX
│
├── Product Except Self
│
├── Sum Except Self
│
├── Left/Right Product
│
├── Left/Right Sum
│
├── Prefix Maximum
│
└── Suffix Maximum
```

The exact operation may change, but the central idea remains:

```text
PRECOMPUTE INFORMATION
FROM THE LEFT AND RIGHT
```

---

# 26. Edge Cases

Always test these:

### All positive

```text
[1, 2, 3, 4]
```

---

### Contains one zero

```text
[1, 2, 0, 4]
```

---

### Contains multiple zeros

```text
[1, 0, 3, 0, 5]
```

---

### Negative values

```text
[-1, 2, -3, 4]
```

The prefix/suffix method still works because multiplication naturally handles negative values.

---

### Single element

```text
[7]
```

Check the exact problem specification for the expected output.

---

# 27. Quick Revision

Before the exam, remember only this:

```text
Problem:
Product of every element except arr[i]

Pattern:
Prefix + Suffix

Idea:
LEFT × RIGHT

Pass 1:
Store LEFT product

Pass 2:
Multiply RIGHT product

Direction:
Left → Right
Right → Left

Time:
O(N)

Space:
O(N) including output
```

### Core Code

```python
answer = [1] * n

prefix = 1

for i in range(n):
    answer[i] = prefix
    prefix *= arr[i]

suffix = 1

for i in range(n - 1, -1, -1):
    answer[i] *= suffix
    suffix *= arr[i]
```

---

# 🧠 28. Final Memory Trick

Memorize:

```text
PRODUCT EXCEPT SELF
        ↓
EVERYTHING EXCEPT CURRENT
        ↓
LEFT + RIGHT
        ↓
PREFIX × SUFFIX
        ↓
TWO PASSES
        ↓
O(N)
```

### The question to ask yourself:

> **What is on the left? What is on the right?**

Then:

```text
LEFT  → Prefix
RIGHT → Suffix
```

And finally:

```text
answer[i] = LEFT × RIGHT
```

---

# 🔥 Final Takeaway

The real pattern is not just:

```text
Product Except Self
```

It is:

```text
FOR EACH INDEX
      ↓
EXCLUDE CURRENT
      ↓
SPLIT ARRAY
      ↓
LEFT + RIGHT
      ↓
PREFIX × SUFFIX
```

Once you recognize this structure, the problem becomes a straightforward **two-pass O(N) array problem**.

> ### 🔥 TCS NQT Memory Formula
>
> **`EVERYTHING EXCEPT CURRENT → LEFT × RIGHT → PREFIX × SUFFIX`**
