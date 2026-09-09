# 🔥 9. Two Sum

> One of the most important array problems in TCS NQT.
>
> **Two Sum is not just one question — it is a pattern.**
>
> TCS can disguise it as:
>
> * Find two numbers with a given sum
> * Find a pair whose sum is `K`
> * Find two elements that add to a target
> * Find two indices whose values add to a target
> * Find two coins whose values equal a target
> * Find a pair satisfying a target-sum condition
>
> The underlying idea is usually the same.

---

# 1. Problem Name

## Two Sum / Find Pair With Given Sum

Given an array of integers and a target value `K`, find **two different elements whose sum equals `K`**.

Return their indices.

If no such pair exists, print:

```text
-1
```

### Example

```text
Input:
5
2 7 11 15 3
9

Output:
0 1
```

Because:

```text
arr[0] + arr[1]
= 2 + 7
= 9
```

Therefore:

```text
Answer = 0 1
```

---

# 2. Pattern Used

## 🧠 Hashing — Dictionary

For an **unsorted array**, the optimal pattern is:

```text
Current number
      ↓
Target - Current
      ↓
Have I seen it before?
      ↓
YES → Pair found
NO  → Store current number
```

The key formula is:

```text
needed = target - current
```

Then:

```text
if needed in seen:
    pair found
```

### Complexity

```text
Time:  O(N)
Space: O(N)
```

---

# 3. How to Recognize the Pattern

Look for phrases such as:

* Two numbers
* Two elements
* Find a pair
* Pair with given sum
* Sum equals target
* Sum equals `K`
* Find two indices
* Target sum
* Two coins with total value `K`

The strongest clue is:

> **Find two elements whose sum equals X.**

Immediately think:

# **Two Sum**

Then ask one more question:

> **Is the array sorted?**

This determines the implementation.

```text
                TWO SUM
                   ↓
             Is array sorted?
              ↙           ↘
            YES            NO
             ↓              ↓
       Two Pointers       Hashing
```

---

# 4. Core Idea

Suppose:

```text
arr = [2, 7, 11, 15]
target = 9
```

We need:

```text
x + y = 9
```

Take the current value:

```text
2
```

What number do we need?

```text
needed = 9 - 2
       = 7
```

Instead of searching the whole array for `7`, store values we have already seen in a dictionary.

The dictionary stores:

```text
value → index
```

After processing `2`:

```text
2 → 0
```

When we reach `7`:

```text
needed = 9 - 7
       = 2
```

We check:

```text
2 in seen?
```

Yes.

Therefore:

```text
seen[2] = 0
```

and current index is:

```text
1
```

So:

```text
0 1
```

is the answer.

---

# 5. Why `target - current`?

This is the most important mathematical step.

We know:

```text
current + needed = target
```

Therefore:

```text
needed = target - current
```

For example:

```text
target = 10
current = 6
```

Then:

```text
needed = 10 - 6
       = 4
```

So instead of asking:

> Which two numbers should I try?

we ask:

> **What number do I need to complete the target?**

This is the central Two Sum idea.

---

# 6. Optimal Python Code — TCS NQT Style

```python
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
```

This is the version to remember for an **unsorted array**.

It is:

* `O(N)`
* Simple
* Easy to reproduce
* Works with duplicates
* Works with negative numbers
* Does not require sorting
* Preserves original indices

---

# 7. Understanding `seen`

We create:

```python
seen = {}
```

The dictionary stores:

```text
value → index
```

For:

```text
arr = [2, 7, 11]
```

after processing the first two elements:

```text
seen = {
    2: 0,
    7: 1
}
```

This lets us ask:

```python
if needed in seen:
```

in average `O(1)` time.

---

# 8. Example 1

### Input

```text
5
2 7 11 15 3
9
```

### Output

```text
0 1
```

Because:

```text
2 + 7 = 9
```

---

# 9. Dry Run

Array:

```text
[2, 7, 11, 15, 3]
```

Target:

```text
9
```

Initially:

```text
seen = {}
```

---

## Step 1 — Index 0

Current:

```text
arr[0] = 2
```

Calculate:

```text
needed = 9 - 2
       = 7
```

Check:

```text
7 in seen?
```

No.

Store:

```text
seen = {
    2: 0
}
```

---

## Step 2 — Index 1

Current:

```text
arr[1] = 7
```

Calculate:

```text
needed = 9 - 7
       = 2
```

Check:

```text
2 in seen?
```

Yes.

We have:

```text
seen[2] = 0
```

Current index:

```text
1
```

Therefore:

```text
0 1
```

Stop.

---

# 10. Dry Run Table

| Index | Current | Needed | `seen` Before | Action        |
| ----: | ------: | -----: | :------------ | :------------ |
|     0 |       2 |      7 | `{}`          | Store `2 → 0` |
|     1 |       7 |      2 | `{2: 0}`      | ✅ Found       |

Answer:

```text
0 1
```

---

# 11. Example 2 — No Pair

### Input

```text
4
1 2 3 4
20
```

No two elements add up to `20`.

Therefore:

```text
Output:
-1
```

The `for ... else` executes the `else` only if the loop finishes without finding a pair.

---

# 12. Example 3 — Duplicate Values

This is an important edge case.

### Input

```text
4
3 3 5 7
6
```

We need:

```text
3 + 3 = 6
```

### First `3`

```text
current = 3
needed = 6 - 3
       = 3
```

`3` is not in `seen`.

Store:

```text
seen = {
    3: 0
}
```

### Second `3`

```text
current = 3
needed = 6 - 3
       = 3
```

Now:

```text
3 in seen
```

Yes.

Therefore:

```text
0 1
```

### Output

```text
0 1
```

---

# 13. Why We Check Before Storing

This ordering is extremely important:

```python
if needed in seen:
    ...
seen[arr[i]] = i
```

We **check first** and **store second**.

Why?

Consider:

```text
arr = [5]
target = 10
```

If we stored `5` first and then checked for the needed value:

```text
needed = 10 - 5
       = 5
```

we might incorrectly use the same element twice.

But the correct rule is:

> **Two Sum requires two different indices.**

By checking before storing, the current element cannot match itself.

---

# 14. Example 4 — Negative Numbers

### Input

```text
5
-3 4 7 -2 8
5
```

We need:

```text
-3 + 8 = 5
```

At index `0`:

```text
current = -3
needed = 5 - (-3)
       = 8
```

Later, `8` is found.

Therefore:

```text
Output:
0 4
```

Negative values require no special handling.

---

# 15. Example 5 — Negative Target

### Input

```text
5
-5 -2 3 7 10
-7
```

We need:

```text
-5 + (-2) = -7
```

Therefore:

```text
Output:
0 1
```

The same formula works:

```text
needed = target - current
```

---

# 16. Example 6 — Pair Appears Later

Consider:

```text
arr = [10, 3, 8, 2]
target = 5
```

At index `0`:

```text
current = 10
needed = -5
```

Not found.

At index `1`:

```text
current = 3
needed = 2
```

Not found.

Store `3`.

At index `2`:

```text
current = 8
needed = -3
```

Not found.

At index `3`:

```text
current = 2
needed = 3
```

`3` is already stored.

Therefore:

```text
1 3
```

because:

```text
3 + 2 = 5
```

---

# 17. Why Not Use Nested Loops?

The obvious approach is:

```python
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print(i, j)
```

This works.

But the nested loops may compare almost every pair.

Therefore:

```text
Time = O(N²)
```

For large `N`, this becomes expensive.

---

# 18. Why Hashing Gives O(N)

Instead of searching the array again and again, we store previously seen values.

For every element:

```text
current
   ↓
target - current
   ↓
Dictionary lookup
```

Average dictionary lookup:

```text
O(1)
```

For `N` elements:

```text
N × O(1)
```

Therefore:

```text
O(N)
```

---

# 19. Brute Force vs Hashing

| Approach               |       Time |   Space | Recommended |
| ---------------------- | ---------: | ------: | :---------: |
| Nested Loops           |      O(N²) |    O(1) |      ❌      |
| Hashing                |       O(N) |    O(N) |      ✅      |
| Sorting + Two Pointers | O(N log N) | Depends |      ⚠️     |

For an **unsorted array where original indices matter**, hashing is usually the cleanest solution.

---

# 20. Hashing vs Two Pointers

This is one of the most important things to remember.

There are two major Two Sum patterns.

## Case 1 — Unsorted Array

Example:

```text
[2, 7, 11, 15]
```

Use:

```text
Hashing
```

Complexity:

```text
Time:  O(N)
Space: O(N)
```

---

## Case 2 — Sorted Array

Example:

```text
[1, 2, 3, 4, 6]
```

Target:

```text
6
```

Use:

```text
Two Pointers
```

Start:

```text
left = 0
right = n - 1
```

Calculate:

```text
sum = arr[left] + arr[right]
```

Then:

```text
sum < target
    ↓
left++

sum > target
    ↓
right--

sum == target
    ↓
FOUND
```

Complexity:

```text
Time:  O(N)
Space: O(1)
```

---

# 21. Two-Pointer Example

Consider:

```text
arr = [1, 2, 3, 4, 6]
target = 6
```

Initially:

```text
left = 0
right = 4
```

Values:

```text
1 + 6 = 7
```

Since:

```text
7 > 6
```

move `right`:

```text
right = 3
```

Now:

```text
1 + 4 = 5
```

Since:

```text
5 < 6
```

move `left`:

```text
left = 1
```

Now:

```text
2 + 4 = 6
```

Found.

---

# 22. Important Decision Rule

Memorize this:

```text
TWO SUM
   ↓
Is the array sorted?
   ↙           ↘
 YES           NO
  ↓             ↓
Two Pointer   Hashing
```

### But there is one important qualification:

If the array is unsorted **and you are allowed to sort while preserving original indices**, you can also use sorting + two pointers with `(value, original_index)` pairs.

However, for TCS NQT, if the question simply gives an unsorted array and asks for original indices, the dictionary solution is usually the most direct.

---

# 23. Why Not Sort Automatically?

Suppose:

```text
arr = [3, 2, 4]
target = 6
```

Correct original indices are:

```text
1 2
```

because:

```text
arr[1] + arr[2]
= 2 + 4
= 6
```

If we simply sort:

```text
[2, 3, 4]
```

the original indices are lost.

Therefore:

```text
Unsorted + Original Indices
        ↓
Hashing
```

is the safest pattern.

---

# 24. Important Variation — Return Values Instead of Indices

Sometimes the question asks:

> Print the two numbers instead of their indices.

Then the output logic changes.

For example:

```python
print(arr[seen[needed]], arr[i])
```

would print the values.

Or, depending on the implementation:

```python
print(needed, arr[i])
```

Always check whether the question asks for:

```text
Indices
```

or:

```text
Values
```

---

# 25. Important Variation — Count Number of Pairs

Suppose the question asks:

> How many pairs have sum `K`?

You cannot stop after finding the first pair.

You need a frequency map.

The general idea becomes:

```text
current
   ↓
needed = K - current
   ↓
How many times have I seen needed?
   ↓
Add that frequency to answer
```

This is a related hashing pattern.

---

# 26. Important Variation — Find All Pairs

If the question asks for **all** valid pairs, don't immediately `break`.

Instead, continue processing according to the exact requirement.

Be careful with:

* Duplicate values
* Duplicate pairs
* Index pairs
* Value pairs

The output specification determines the implementation.

---

# 27. Important Variation — Sorted Array

If the input is explicitly sorted:

```text
[1, 2, 3, 4, 6, 8]
```

use:

```text
left = 0
right = n - 1
```

Core code:

```python
left = 0
right = n - 1

while left < right:
    total = arr[left] + arr[right]

    if total == target:
        print(left, right)
        break
    elif total < target:
        left += 1
    else:
        right -= 1
else:
    print(-1)
```

This gives:

```text
Time:  O(N)
Space: O(1)
```

---

# 28. ⚠️ TCS Exam Trap — Same Element Twice

Consider:

```text
arr = [5]
target = 10
```

It is **not** valid to say:

```text
5 + 5 = 10
```

because there is only one element.

You need two different indices.

The hashing solution prevents this by checking before storing:

```python
if needed in seen:
```

and only afterward:

```python
seen[arr[i]] = i
```

---

# 29. ⚠️ TCS Exam Trap — Duplicate Values

Consider:

```text
arr = [3, 3]
target = 6
```

This **is valid**.

There are two different indices:

```text
0
1
```

Therefore:

```text
0 1
```

The fact that the values are equal does not matter.

What matters is that the indices are different.

---

# 30. ⚠️ TCS Exam Trap — Negative Numbers

Never assume:

```text
arr[i] > 0
```

Example:

```text
[-5, 2, 7]
```

Target:

```text
2
```

We have:

```text
-5 + 7 = 2
```

Hashing handles this automatically.

---

# 31. ⚠️ TCS Exam Trap — Index vs Value

The question may ask:

### Return indices

```text
0 1
```

or:

### Return values

```text
2 7
```

These are not the same output.

Always identify exactly what the question asks.

---

# 32. ⚠️ TCS Exam Trap — Multiple Valid Answers

Consider:

```text
arr = [1, 2, 3, 4, 5]
target = 6
```

There are multiple valid pairs:

```text
1 + 5 = 6
2 + 4 = 6
```

The problem may specify:

* Return any valid pair
* Return the first pair
* Return the pair with smallest indices
* Return all pairs

Do not assume the required output.

Follow the exact wording.

---

# 33. Pattern Recognition Shortcut

When you see:

```text
TWO ELEMENTS
      +
TARGET SUM
```

think:

# **TWO SUM**

Then ask:

```text
Is the array sorted?
```

Decision tree:

```text
             TWO SUM
                ↓
        Is array sorted?
          ↙          ↘
        YES           NO
         ↓             ↓
   Two Pointers      Hashing
         ↓             ↓
       O(N)          O(N)
       O(1)          O(N)
```

---

# 34. Core Hashing Code to Memorize

For an unsorted array:

```python
seen = {}

for i in range(n):
    needed = target - arr[i]

    if needed in seen:
        print(seen[needed], i)
        break

    seen[arr[i]] = i
```

The two most important lines are:

```python
needed = target - arr[i]
```

and:

```python
if needed in seen:
```

That's the heart of Two Sum.

---

# 35. General Complement Pattern

Two Sum teaches a broader hashing technique:

```text
Current
   ↓
What do I need?
   ↓
Complement
   ↓
Have I seen the complement?
```

Formula:

```text
complement = target - current
```

This idea appears in many other problems involving:

* Pair sums
* Difference conditions
* Target values
* Complement lookup
* Frequency-based pair counting

So don't memorize Two Sum as an isolated problem.

Learn the **complement lookup pattern**.

---

# 36. Pattern Family

```text
HASHING / COMPLEMENT
│
├── Two Sum
│
├── Count Pairs With Given Sum
│
├── Find Pair With Given Difference
│
├── Subarray Sum Problems
│
├── Frequency-Based Pair Problems
│
└── Complement Lookup Problems
```

Two Sum is one of the most important examples of this family.

---

# 37. Edge Cases

Always test:

### No pair

```text
[1, 2, 3]
target = 10
```

---

### Duplicate values

```text
[3, 3]
target = 6
```

---

### Negative values

```text
[-3, 4, 7, -2, 8]
target = 5
```

---

### Negative target

```text
[-5, -2, 3]
target = -7
```

---

### Single element

```text
[5]
target = 10
```

No valid pair.

---

### Multiple valid pairs

```text
[1, 2, 3, 4, 5]
target = 6
```

Read the exact output requirement.

---

### Zero

```text
[0, 4, 3, 0]
target = 0
```

The two zeros form a valid pair because they occur at different indices.

---

# 38. Quick Revision

Before the exam, remember:

```text
Problem:
Find two elements whose sum = target

Pattern:
Two Sum

Unsorted:
Hashing

Formula:
needed = target - current

Dictionary:
value → index

Check:
if needed in seen

Found:
previous index + current index

Sorted:
Two Pointers

Time:
O(N)

Space:
O(N) for hashing
O(1) for two pointers on sorted input
```

---

# 🧠 39. Final Memory Trick

Memorize:

```text
TWO SUM
   ↓
CURRENT
   ↓
TARGET - CURRENT
   ↓
NEEDED
   ↓
HAVE I SEEN IT?
   ↙          ↘
 YES          NO
  ↓            ↓
FOUND        STORE
```

### One-line exam rule:

> **`Two Sum → target - current → check HashMap`**

---

# 🚀 40. Final Takeaway

The real lesson of Two Sum is not simply:

```text
Find two numbers.
```

It is:

```text
CURRENT
   ↓
WHAT DO I NEED?
   ↓
TARGET - CURRENT
   ↓
HAVE I SEEN THAT VALUE?
   ↓
YES → PAIR FOUND
NO  → STORE CURRENT
```

And the most important TCS decision is:

```text
                 TWO SUM
                    ↓
             Is array sorted?
              ↙           ↘
            YES            NO
             ↓              ↓
       TWO POINTER       HASHING
             ↓              ↓
           O(N)           O(N)
           O(1)           O(N)
```

> ### 🔥 TCS NQT Memory Formula
>
> **`TWO SUM → COMPLEMENT = TARGET - CURRENT → HASHMAP LOOKUP`**
>
> **`UNSORTED → HASHING | SORTED → TWO POINTER`**
