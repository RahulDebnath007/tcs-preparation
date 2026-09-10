# 🔥 12. Array Transformation / Optimization

**Array Transformation / Optimization** is a high-priority TCS NQT-style category because the problem statement often sounds complicated:

> **"Transform the array using a series of operations to maximize/minimize a value."**

But underneath, the solution is usually about:

* Finding the right order of operations
* Avoiding unnecessary work
* Maintaining useful information while traversing
* Choosing the best possible option
* Sometimes combining **Sorting + Greedy**
* Sometimes using **Two Pointer, Prefix Sum, Simulation, or Dynamic Programming**

For this pattern, we use a representative problem:

# 🔥 Maximum Difference After Transformation

Given an array, find the maximum value of:

```text
arr[j] - arr[i]
```

where:

```text
j > i
```

In simple terms:

> Choose an earlier value and a later value such that their difference is maximum.

---

# 1. Problem Name

## 🔥 Maximum Difference in an Array

Given:

```text
arr = [7, 1, 5, 3, 6, 4]
```

Find the maximum value of:

```text
arr[j] - arr[i]
```

subject to:

```text
j > i
```

The best choice is:

```text
6 - 1 = 5
```

Therefore:

```text
Output:
5
```

---

# 2. Pattern Used

## 🧠 Pattern: Greedy + Single-Pass Optimization

The key idea is:

> While moving from left to right, keep the **smallest value seen so far**.

For every current value:

```text
current value - minimum seen so far
```

gives the best possible difference ending at the current position.

Therefore, we maintain:

```text
minimum
maximum_difference
```

The basic idea is:

```text
Current element
      ↓
Subtract smallest previous element
      ↓
Candidate difference
      ↓
Update maximum
```

---

# 3. How to Recognize the Pattern

Look for phrases such as:

* maximum difference
* maximum profit
* minimum cost
* maximize the result
* minimize the result
* best possible value
* optimal transformation
* choose two elements
* difference between two elements
* operation can be performed
* transform array to maximize/minimize
* best possible arrangement

Then ask:

> **"Can I maintain the best candidate so far instead of checking every possibility?"**

If yes, think:

# → Greedy / Running Minimum or Maximum

---

## Example

Question:

> Find the maximum difference between a later and an earlier element.

The expression is:

```text
arr[j] - arr[i]
```

where:

```text
j > i
```

For the current `arr[j]`, we want the smallest possible earlier `arr[i]`.

Therefore:

```text
Best previous value
        ↓
Minimum so far
```

So instead of checking every pair:

```text
for every i
    for every j
```

we maintain:

```text
minimum_so_far
```

This reduces the solution from:

```text
O(N²)
```

to:

```text
O(N)
```

---

# 4. Solve Approach

Given:

```text
[7, 1, 5, 3, 6, 4]
```

Start with:

```text
minimum = 7
maximum_difference = 0
```

Now move from left to right.

---

## Step 1 — `7`

Current:

```text
7
```

Initially:

```text
minimum = 7
```

---

## Step 2 — `1`

`1` is smaller than the current minimum.

Therefore:

```text
minimum = 1
```

---

## Step 3 — `5`

Calculate:

```text
5 - 1 = 4
```

Update:

```text
maximum_difference = 4
```

---

## Step 4 — `3`

Calculate:

```text
3 - 1 = 2
```

No improvement.

Maximum remains:

```text
4
```

---

## Step 5 — `6`

Calculate:

```text
6 - 1 = 5
```

Update:

```text
maximum_difference = 5
```

---

## Step 6 — `4`

Calculate:

```text
4 - 1 = 3
```

No improvement.

Final:

```text
5
```

---

# 5. Optimal Python Code — TCS NQT Style

```python
n = int(input())
arr = list(map(int, input().split()))

minimum = arr[0]
maximum_difference = 0

for i in range(1, n):
    difference = arr[i] - minimum

    if difference > maximum_difference:
        maximum_difference = difference

    if arr[i] < minimum:
        minimum = arr[i]

print(maximum_difference)
```

---

# 6. Why This Code Is Optimal

A brute-force solution would check every possible pair:

```text
i → every position
j → every later position
```

That requires:

```text
O(N²)
```

Instead, our solution remembers only the information that matters:

```text
Smallest value seen so far
```

Then for every new value:

```text
current - minimum
```

is the best possible difference using the current element as the later value.

Therefore:

```text
One traversal
     ↓
Running minimum
     ↓
Maximum difference
```

---

# 7. Examples

## Example 1 — Basic

### Input

```text
6
7 1 5 3 6 4
```

### Output

```text
5
```

Because:

```text
6 - 1 = 5
```

---

## Example 2 — Increasing Array

### Input

```text
5
1 2 3 4 5
```

### Output

```text
4
```

Best difference:

```text
5 - 1 = 4
```

---

## Example 3 — Decreasing Array

### Input

```text
5
5 4 3 2 1
```

There is no positive difference.

### Output

```text
0
```

---

## Example 4 — Mixed Values

### Input

```text
6
10 3 8 2 9 1
```

Possible best difference:

```text
9 - 2 = 7
```

### Output

```text
7
```

Notice that:

```text
9 - 1
```

cannot be used because `1` occurs **after** `9`.

This is why we cannot simply find:

```text
maximum - minimum
```

without considering their positions.

---

# 8. Why Position Matters

This is a very important concept.

Consider:

```text
arr = [8, 3, 5, 2]
```

The minimum is:

```text
2
```

The maximum is:

```text
8
```

But:

```text
8 - 2 = 6
```

is invalid because:

```text
8
```

comes **before**:

```text
2
```

The condition requires:

```text
j > i
```

Therefore, the earlier value must be the one being subtracted.

The valid maximum is:

```text
5 - 3 = 2
```

So:

> **Do not simply calculate `max(arr) - min(arr)` when order matters.**

---

# 9. Dry Run

Take:

```text
arr = [7, 1, 5, 3, 6, 4]
```

Initial:

```text
minimum = 7
maximum_difference = 0
```

| Current | Minimum So Far | Difference | Maximum |
| ------: | -------------: | ---------: | ------: |
|       7 |              7 |          — |       0 |
|       1 |              7 |         -6 |       0 |
|       5 |              1 |          4 |       4 |
|       3 |              1 |          2 |       4 |
|       6 |              1 |          5 |       5 |
|       4 |              1 |          3 |       5 |

Final:

```text
maximum_difference = 5
```

---

# 10. Time Complexity

We traverse the array exactly once.

Therefore:

```text
O(N)
```

### ⏱️ Time Complexity

```text
O(N)
```

Compare this with brute force:

```text
O(N²)
```

The single-pass solution is much more efficient.

---

# 11. Space Complexity

We only maintain:

```text
minimum
maximum_difference
difference
```

No additional data structure is required.

### 💾 Auxiliary Space

```text
O(1)
```

Therefore:

```text
Time  → O(N)
Space → O(1)
```

---

# 🧠 12. VERY IMPORTANT — "Array Transformation" Is a Category

This is one of the most important things to understand.

**Array Transformation / Optimization is NOT one exact algorithm.**

TCS can completely change the operation.

The word:

```text
Transform
```

does not automatically mean:

```text
Greedy
```

You must identify **what the transformation actually requires**.

---

# 🔥 13. Variation 1 — Replace Elements

Question:

> Replace every negative number with zero.

The pattern is:

```text
Traversal
+
Conditional Transformation
```

Code:

```python
for i in range(n):
    if arr[i] < 0:
        arr[i] = 0
```

Example:

```text
[-2, 5, -1, 8]
```

becomes:

```text
[0, 5, 0, 8]
```

---

# 🔥 14. Variation 2 — Move Elements

Question:

> Move all zeros to the end.

Pattern:

```text
Two Pointer
```

This is actually the pattern from:

```text
#2 Move All Zeros to the End
```

The key point is:

> Transformation problems can hide other patterns.

Do not force every transformation problem into Greedy.

---

# 🔥 15. Variation 3 — Rearrange to Maximize

Question:

> Rearrange the numbers to obtain the maximum possible value.

Think:

```text
Sorting
    +
Greedy
```

The exact solution depends on how the numbers must be arranged.

The important recognition is:

```text
Rearrangement
      ↓
Order matters
      ↓
Consider Sorting
```

---

# 🔥 16. Variation 4 — Minimum/Maximum After Operations

Question:

> Perform operations on array elements to maximize the final sum.

Think:

```text
Optimization
      ↓
What changes after each operation?
      ↓
What choice gives the best result?
      ↓
Greedy?
```

Sometimes the answer is Greedy.

Sometimes it may require:

```text
Dynamic Programming
```

or another technique.

Therefore, analyze the operation before choosing the algorithm.

---

# 🔥 17. Variation 5 — Prefix/Suffix Transformation

Question:

> Replace every element with the sum of elements to its left.

Think:

```text
Prefix Sum
```

Example:

```text
arr = [1, 2, 3, 4]
```

Result:

```text
[0, 1, 3, 6]
```

A possible implementation:

```python
prefix = 0

for i in range(n):
    current = arr[i]
    arr[i] = prefix
    prefix += current
```

Pattern:

```text
Left-side cumulative information
        ↓
Prefix
```

---

# 🔥 18. Variation 6 — Repeated Operations

Question:

> Continue performing an operation until the array becomes stable.

Think:

```text
Simulation
```

Typical structure:

```python
while condition:
    perform_operation()
```

Do not automatically search for a complex algorithm if straightforward simulation is sufficient.

---

# 🔥 19. Variation 7 — Maximum Contiguous Result

Question:

> Find the maximum sum of a contiguous subarray.

Think:

```text
Kadane's Algorithm
```

This connects directly to:

```text
#4 Maximum Subarray Sum
```

Recognition:

```text
Maximum
+
Contiguous
+
Subarray
+
Sum
        ↓
Kadane
```

---

# 🚨 20. The Biggest TCS Trick

The word:

```text
"Transform"
```

does **not** automatically identify the algorithm.

Instead ask:

> **What does the transformation actually require?**

---

## If it means...

### Move elements

```text
Two Pointer
```

---

### Reorder elements

```text
Sorting
```

---

### Calculate cumulative values

```text
Prefix Sum
```

---

### Find the best possible result

```text
Greedy / DP / Optimization
```

---

### Apply an operation repeatedly

```text
Simulation
```

---

### Find maximum contiguous result

```text
Kadane
```

---

### Count occurrences

```text
Frequency Hashing
```

---

# 🧠 21. NQT Pattern Recognition Framework

Whenever you get an unfamiliar array question, follow this process.

---

## Step 1 — Ignore the Story

Don't get distracted by:

```text
Bank
Shopping
Production
Finance
Customers
Operations
Transformation
```

These may simply be the story surrounding the problem.

---

## Step 2 — Identify the Operation

Ask:

```text
Search?
Count?
Move?
Rearrange?
Transform?
Maximize?
Minimize?
```

---

## Step 3 — Identify What Information You Need

Ask:

```text
Previous sum?
Minimum?
Maximum?
Frequency?
Seen values?
Position?
```

---

## Step 4 — Select the Pattern

For example:

> Maximum difference between a later and earlier value.

Break it down:

```text
arr[j] - arr[i]
      ↓
Need smallest earlier arr[i]
      ↓
Maintain minimum so far
      ↓
Greedy / Running Minimum
```

That is the real NQT skill.

---

# 🔥 22. Running Minimum Pattern

This pattern is extremely reusable.

Whenever you see:

```text
Current value - best previous value
```

ask:

> What is the best previous value?

If smaller is better:

```text
Running Minimum
```

If larger is better:

```text
Running Maximum
```

---

## Running Minimum

```python
minimum = arr[0]

for x in arr:
    minimum = min(minimum, x)
```

---

## Running Maximum

```python
maximum = arr[0]

for x in arr:
    maximum = max(maximum, x)
```

---

# 🎯 23. General Optimization Template

A very useful mental template is:

```python
best = initial_value

for x in arr:

    # calculate current candidate
    candidate = ...

    if candidate > best:
        best = candidate

    # update useful information
    ...
```

The exact variables change depending on the problem.

But the thought process is:

```text
Current element
      ↓
Calculate candidate answer
      ↓
Compare with best answer
      ↓
Update useful state
```

---

# 🚨 24. Common Mistakes

## Mistake 1 — Checking Every Pair

Using:

```text
for i
    for j
```

for a simple maximum-difference problem gives:

```text
O(N²)
```

Instead maintain:

```text
minimum so far
```

and achieve:

```text
O(N)
```

---

## Mistake 2 — Using `max - min`

This is wrong when the problem requires:

```text
j > i
```

because the minimum may occur after the maximum.

Example:

```text
[8, 3, 5, 2]
```

Global:

```text
max - min = 8 - 2 = 6
```

But that violates the required ordering.

---

## Mistake 3 — Updating Minimum Too Early

Consider:

```python
minimum = arr[0]

for i in range(1, n):
    difference = arr[i] - minimum

    if difference > maximum_difference:
        maximum_difference = difference

    if arr[i] < minimum:
        minimum = arr[i]
```

The order matters.

First calculate the difference using **previous elements**.

Then update the minimum for future elements.

This ensures:

```text
minimum
```

always represents a value that occurs **before** the current element.

---

## Mistake 4 — Assuming Every Optimization Is Greedy

Optimization problems can require:

```text
Greedy
Dynamic Programming
Sorting
Two Pointer
Binary Search
Prefix/Suffix
```

Do not choose Greedy just because the question says:

```text
maximum
```

You need to understand the structure of the problem.

---

# 🎯 25. Pattern Comparison

| Problem Requirement           | Likely Pattern                                   |
| ----------------------------- | ------------------------------------------------ |
| Maximum difference with order | Running Minimum / Greedy                         |
| Minimum difference            | Running Maximum / Sorting depending on condition |
| Move elements                 | Two Pointer                                      |
| Rearrange elements            | Sorting                                          |
| Cumulative transformation     | Prefix Sum                                       |
| Repeated operation            | Simulation                                       |
| Maximum contiguous sum        | Kadane                                           |
| Count occurrences             | Frequency Hashing                                |
| Best result after choices     | Greedy / DP                                      |
| Search after ordering         | Sorting + Binary Search                          |

---

# 🎯 26. What You Should Remember

For **#12**, the core idea is:

```text
Optimization Problem
        ↓
Can I avoid checking every possibility?
        ↓
Keep the best information seen so far
        ↓
Calculate the current candidate
        ↓
Update the answer
```

For maximum difference:

```text
Later value - Earlier value
          ↓
Need smallest earlier value
          ↓
Running Minimum
          ↓
Maximum Difference
```

---

# ⚡ 27. Quick Revision

### Running Minimum

```python
minimum = arr[0]

for x in arr:
    minimum = min(minimum, x)
```

### Running Maximum

```python
maximum = arr[0]

for x in arr:
    maximum = max(maximum, x)
```

### Maximum Difference

```python
minimum = arr[0]
maximum_difference = 0

for i in range(1, n):
    difference = arr[i] - minimum

    maximum_difference = max(
        maximum_difference,
        difference
    )

    minimum = min(minimum, arr[i])
```

---

# 🧠 28. Memory Trick

Remember:

```text
MAXIMUM DIFFERENCE
        ↓
LATER - EARLIER
        ↓
Need smallest earlier value
        ↓
RUNNING MINIMUM
        ↓
UPDATE MAXIMUM
```

The main formula:

```text
CURRENT - MINIMUM SO FAR
        ↓
CURRENT BEST DIFFERENCE
        ↓
UPDATE MAXIMUM
```

---

# 🚀 Final NQT Cheat Sheet

```text
Maximum difference with j > i
→ Running Minimum + Greedy

Need smallest previous value
→ Minimum so far

Need largest previous value
→ Maximum so far

Need move elements
→ Two Pointer

Need reorder elements
→ Sorting

Need cumulative values
→ Prefix Sum

Need repeated operations
→ Simulation

Need maximum contiguous sum
→ Kadane

Need frequency
→ Hashing
```

### 🔥 Final Pattern Recognition

```text
"Transform?"
"Optimize?"
"Maximize?"
"Minimize?"
"Best possible?"
"Maximum difference?"
        ↓
IGNORE THE STORY
        ↓
IDENTIFY THE OPERATION
        ↓
ASK WHAT INFORMATION
MUST BE REMEMBERED
        ↓
MIN / MAX / FREQUENCY /
POSITION / PREFIX / ETC.
        ↓
CHOOSE THE PATTERN
```

> **ARRAY OPTIMIZATION → AVOID CHECKING EVERY POSSIBILITY → MAINTAIN THE BEST USEFUL INFORMATION → BUILD THE ANSWER IN ONE PASS WHEN POSSIBLE**
