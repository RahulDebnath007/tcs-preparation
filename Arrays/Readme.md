# 1.🔢 Find the Smallest Element in an Array

A simple and fundamental **array traversal problem** commonly used in coding assessments such as **TCS NQT**.

The objective is to find the **minimum/smallest element** present in a given array **without using Python's built-in `min()` function**.

---

## 📌 Problem Statement

Given an array of `N` integers, find and print the **smallest element** in the array.

### Input Format

* The first line contains an integer `N`, representing the number of elements.
* The second line contains `N` space-separated integers representing the array.

### Output Format

Print the smallest element present in the array.

---

## 🧪 Example

### Input

```text
5
8 3 12 1 6
```

### Output

```text
1
```

### Explanation

The given array is:

```text
8 3 12 1 6
```

We compare each element with the current smallest value:

```text
8 → smallest = 8
3 → smallest = 3
12 → no change
1 → smallest = 1
6 → no change
```

Therefore, the smallest element is:

```text
1
```

---

# 💡 Approach

We can solve this problem using **linear traversal** of the array.

### Step 1: Initialize the Minimum

Assume that the first element of the array is the smallest:

```python
smallest = arr[0]
```

### Step 2: Traverse the Remaining Elements

Start from the second element and compare every element with `smallest`.

```python
for i in range(1, n):
```

### Step 3: Update the Minimum

If the current element is smaller than `smallest`, update the value:

```python
if arr[i] < smallest:
    smallest = arr[i]
```

### Step 4: Print the Result

After checking all elements:

```python
print(smallest)
```

The final value stored in `smallest` is the minimum element of the array.

---

# 🧠 Algorithm

1. Read the number of elements `N`.
2. Read the array.
3. Set `smallest = arr[0]`.
4. Traverse the array from index `1` to `N - 1`.
5. For every element:

   * Compare the current element with `smallest`.
   * If it is smaller, update `smallest`.
6. Print `smallest`.

---

# 💻 Python Code

```python
n = int(input())

arr = list(map(int, input().split()))

smallest = arr[0]

for i in range(1, n):
    if arr[i] < smallest:
        smallest = arr[i]

print(smallest)
```

---

# 🔍 Code Explanation

## 1. Read the Size of the Array

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

For example:

```text
5
```

becomes:

```python
n = 5
```

---

## 2. Read the Array

```python
arr = list(map(int, input().split()))
```

This line performs three operations.

### `input()`

Reads the complete line:

```text
8 3 12 1 6
```

### `.split()`

Splits the input into individual strings:

```python
["8", "3", "12", "1", "6"]
```

### `map(int, ...)`

Converts each string into an integer:

```python
[8, 3, 12, 1, 6]
```

Finally, `list()` creates the Python list.

So:

```python
arr = [8, 3, 12, 1, 6]
```

---

## 3. Assume the First Element Is the Smallest

```python
smallest = arr[0]
```

Initially:

```text
smallest = 8
```

We don't initialize `smallest` with `0` or another fixed value because the array may contain negative numbers.

For example:

```text
-10 -5 -20
```

The correct minimum is:

```text
-20
```

---

## 4. Traverse the Array

```python
for i in range(1, n):
```

The loop starts from index `1` because the element at index `0` has already been stored in `smallest`.

For:

```python
arr = [8, 3, 12, 1, 6]
```

the loop checks:

```text
3
12
1
6
```

---

## 5. Compare the Current Element

```python
if arr[i] < smallest:
```

If the current element is smaller than the current minimum, we update it.

For example:

```text
smallest = 8
current = 3
```

Since:

```text
3 < 8
```

we update:

```text
smallest = 3
```

---

## 6. Update the Minimum

```python
smallest = arr[i]
```

This stores the newly discovered minimum value.

---

## 7. Print the Answer

```python
print(smallest)
```

After the complete traversal, `smallest` contains the minimum element.

---

# 📊 Dry Run

Consider:

```text
N = 5
Array = [8, 3, 12, 1, 6]
```

| Step    | Current Element | Smallest Before | Comparison | Smallest After |
| ------- | --------------- | --------------- | ---------- | -------------- |
| Initial | 8               | —               | —          | 8              |
| 1       | 3               | 8               | 3 < 8 ✅    | 3              |
| 2       | 12              | 3               | 12 < 3 ❌   | 3              |
| 3       | 1               | 3               | 1 < 3 ✅    | 1              |
| 4       | 6               | 1               | 6 < 1 ❌    | 1              |

### Final Answer

```text
1
```

---

# ⏱️ Complexity Analysis

## Time Complexity

```text
O(N)
```

We traverse the array once.

If there are `N` elements, each element is checked at most once.

Therefore:

```text
Time Complexity = O(N)
```

## Space Complexity

```text
O(1)
```

Apart from the input array, the algorithm only uses one additional variable:

```python
smallest
```

Therefore, the **auxiliary space complexity** is:

```text
O(1)
```

> **Note:** The input array itself requires `O(N)` memory. `O(1)` refers to the extra/auxiliary space used by the algorithm.

---

# 🧪 Test Cases

## Test Case 1 — Normal Case

### Input

```text
5
8 3 12 1 6
```

### Output

```text
1
```

---

## Test Case 2 — Negative Numbers

### Input

```text
5
-4 -10 3 -2 7
```

### Output

```text
-10
```

---

## Test Case 3 — All Elements Are Equal

### Input

```text
4
5 5 5 5
```

### Output

```text
5
```

---

## Test Case 4 — Smallest Element at the Beginning

### Input

```text
5
1 8 12 6 9
```

### Output

```text
1
```

---

## Test Case 5 — Smallest Element at the End

### Input

```text
5
8 12 6 9 2
```

### Output

```text
2
```

---

# 🚫 Why Not Use `min()`?

Python provides a built-in function:

```python
print(min(arr))
```

This works and also has `O(N)` time complexity.

However, for **DSA preparation and coding assessments**, implementing the traversal manually is better practice.

The same technique can be extended to problems such as:

* Finding the largest element
* Finding the second largest element
* Finding the second smallest element
* Counting elements
* Calculating the sum
* Finding element frequency
* Searching for an element
* Finding maximum/minimum values under conditions
* Other array traversal problems

The objective is not simply to obtain the answer, but to understand the **underlying algorithmic pattern**.

---

# 🎯 Key DSA Pattern

This problem teaches the:

## **Linear Traversal / Running Minimum Pattern**

The general idea is:

```text
Initialize an answer
       ↓
Traverse the array
       ↓
Compare current element with answer
       ↓
Update answer if necessary
       ↓
Return final answer
```

This pattern is one of the most important basic techniques for array-based coding problems.

---

# 📚 What You Learn From This Problem

By solving this problem, you practice:

* Array input handling
* Python lists
* `input()`
* `split()`
* `map()`
* Integer conversion
* `for` loops
* Conditional statements
* Array indexing
* Running minimum technique
* Linear traversal
* Time complexity analysis
* Space complexity analysis

---

# 🚀 TCS NQT Relevance

This is a **basic-level array problem** and is useful for building the fundamentals required for coding assessments such as **TCS NQT**.

Although the problem itself is simple, the underlying pattern is important because more difficult problems often use the same **single-pass traversal + running value** technique.

### Recommended thought process during an exam

When you see a problem asking for a minimum:

```text
1. What is the initial minimum?
        ↓
2. Can I scan the array once?
        ↓
3. What condition updates the minimum?
        ↓
4. What is the final complexity?
```

For this problem:

```text
Initial minimum → arr[0]
Traversal       → O(N)
Update          → if arr[i] < smallest
Answer          → smallest
```

---

# 📌 Summary

| Property              | Value                              |
| --------------------- | ---------------------------------- |
| Problem               | Find Smallest Element              |
| Technique             | Linear Traversal                   |
| Pattern               | Running Minimum                    |
| Time Complexity       | `O(N)`                             |
| Auxiliary Space       | `O(1)`                             |
| Built-in `min()` Used | ❌ No                               |
| Difficulty            | Easy                               |
| Language              | Python                             |
| Suitable For          | DSA / Coding Assessments / TCS NQT |

---

## ⭐ Key Takeaway

> **Initialize the answer with the first element, traverse the remaining elements, and update the answer whenever a smaller value is found.**

This simple pattern is a foundation for solving many array problems efficiently.

# 2. 🔢 Find the Largest Element in an Array

A simple and fundamental **array traversal problem** commonly used in coding assessments such as **TCS NQT**.

The objective is to find the **maximum/largest element** present in a given array **without using Python's built-in `max()` function**.

---

## 📌 Problem Statement

Given an array of `N` integers, find and print the **largest element** in the array.

### Input Format

* The first line contains an integer `N`, representing the number of elements.
* The second line contains `N` space-separated integers representing the array.

### Output Format

Print the largest element present in the array.

---

## 🧪 Example

### Input

```text
5
8 3 12 1 6
```

### Output

```text
12
```

### Explanation

The given array is:

```text
8 3 12 1 6
```

We compare each element with the current largest value:

```text
8  → largest = 8
3  → no change
12 → largest = 12
1  → no change
6  → no change
```

Therefore, the largest element is:

```text
12
```

---

# 💡 Approach

We can solve this problem using **linear traversal** of the array.

The idea is simple:

1. Assume the first element is the largest.
2. Traverse the remaining elements.
3. Compare each element with the current largest value.
4. If a larger element is found, update `largest`.
5. After traversing the entire array, `largest` contains the answer.

---

## Step 1: Initialize the Maximum

Assume that the first element of the array is the largest:

```python
largest = arr[0]
```

---

## Step 2: Traverse the Remaining Elements

Start from the second element and compare every element with `largest`.

```python
for i in range(1, n):
```

---

## Step 3: Update the Maximum

If the current element is greater than `largest`, update the value:

```python
if arr[i] > largest:
    largest = arr[i]
```

---

## Step 4: Print the Result

After checking all elements:

```python
print(largest)
```

The final value stored in `largest` is the maximum element of the array.

---

# 🧠 Algorithm

1. Read the number of elements `N`.
2. Read the array.
3. Set `largest = arr[0]`.
4. Traverse the array from index `1` to `N - 1`.
5. For every element:

   * Compare the current element with `largest`.
   * If it is greater, update `largest`.
6. Print `largest`.

---

# 💻 Python Code

```python
n = int(input())

arr = list(map(int, input().split()))

largest = arr[0]

for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

print(largest)
```

---

# 🔍 Code Explanation

## 1. Read the Size of the Array

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

For example:

```text
5
```

becomes:

```python
n = 5
```

---

## 2. Read the Array

```python
arr = list(map(int, input().split()))
```

This line performs three operations.

### `input()`

Reads the complete line:

```text
8 3 12 1 6
```

### `.split()`

Splits the input into individual strings:

```python
["8", "3", "12", "1", "6"]
```

### `map(int, ...)`

Converts each string into an integer:

```python
[8, 3, 12, 1, 6]
```

Finally, `list()` creates the Python list.

So:

```python
arr = [8, 3, 12, 1, 6]
```

---

## 3. Assume the First Element Is the Largest

```python
largest = arr[0]
```

Initially:

```text
largest = 8
```

We don't initialize `largest` with `0` or another fixed value because the array may contain negative numbers.

For example:

```text
-10 -5 -20
```

The correct largest value is:

```text
-5
```

If we initialized:

```python
largest = 0
```

the answer would incorrectly remain `0`.

Therefore, using:

```python
largest = arr[0]
```

is the correct approach.

---

## 4. Traverse the Array

```python
for i in range(1, n):
```

The loop starts from index `1` because the element at index `0` has already been stored in `largest`.

For:

```python
arr = [8, 3, 12, 1, 6]
```

the loop checks:

```text
3
12
1
6
```

---

## 5. Compare the Current Element

```python
if arr[i] > largest:
```

If the current element is greater than the current maximum, we update it.

For example:

```text
largest = 8
current = 12
```

Since:

```text
12 > 8
```

we update:

```text
largest = 12
```

---

## 6. Update the Maximum

```python
largest = arr[i]
```

This stores the newly discovered largest value.

For example:

```text
Before:
largest = 8

Current element:
12

After:
largest = 12
```

---

## 7. Print the Answer

```python
print(largest)
```

After the complete traversal, `largest` contains the maximum element.

---

# 📊 Dry Run

Consider:

```text
N = 5
Array = [8, 3, 12, 1, 6]
```

| Step    | Current Element | Largest Before | Comparison | Largest After |
| ------- | --------------- | -------------- | ---------- | ------------- |
| Initial | 8               | —              | —          | 8             |
| 1       | 3               | 8              | `3 > 8` ❌  | 8             |
| 2       | 12              | 8              | `12 > 8` ✅ | 12            |
| 3       | 1               | 12             | `1 > 12` ❌ | 12            |
| 4       | 6               | 12             | `6 > 12` ❌ | 12            |

### Final Answer

```text
12
```

---

# ⏱️ Complexity Analysis

## Time Complexity

```text
O(N)
```

We traverse the array once.

If there are `N` elements, each element is checked at most once.

Therefore:

```text
Time Complexity = O(N)
```

---

## Space Complexity

```text
O(1)
```

Apart from the input array, the algorithm only uses one additional variable:

```text
largest
```

Therefore, the **auxiliary space complexity** is:

```text
O(1)
```

> **Note:** The input array itself requires `O(N)` memory. `O(1)` refers to the extra/auxiliary space used by the algorithm.

---

# 🧪 Test Cases

## Test Case 1 — Normal Case

### Input

```text
5
8 3 12 1 6
```

### Output

```text
12
```

---

## Test Case 2 — Negative Numbers

### Input

```text
5
-4 -10 -3 -2 -7
```

### Output

```text
-2
```

---

## Test Case 3 — All Elements Are Equal

### Input

```text
4
5 5 5 5
```

### Output

```text
5
```

---

## Test Case 4 — Largest Element at the Beginning

### Input

```text
5
20 8 12 6 9
```

### Output

```text
20
```

---

## Test Case 5 — Largest Element at the End

### Input

```text
5
8 12 6 9 25
```

### Output

```text
25
```

---

# 🚫 Why Not Use `max()`?

Python provides a built-in function for finding the largest element:

```python
print(max(arr))
```

This solution also has:

```text
Time Complexity = O(N)
```

However, the purpose of this problem is to practice the **underlying algorithm rather than relying on a built-in function**.

Manually implementing the traversal helps strengthen your understanding of:

* Array traversal
* Comparisons
* Running maximum
* Loops
* Time complexity
* Space complexity

This approach is particularly useful for **DSA preparation and coding assessments** where built-in functions may be restricted.

---

# 🎯 Key DSA Pattern

This problem teaches the fundamental:

## **Running Maximum Pattern**

The general idea is:

```text
Initialize maximum
       ↓
Traverse the array
       ↓
Compare current element with maximum
       ↓
If current element is larger
       ↓
Update maximum
       ↓
Continue until the array ends
```

In code:

```python
largest = arr[0]

for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
```

This pattern is useful for many other problems involving:

* Maximum element
* Minimum element
* Second largest element
* Second smallest element
* Maximum difference
* Top `K` elements
* Running maximum/minimum
* Array optimization problems

---

# 📚 What You Learn From This Problem

By solving this problem, you practice:

* Array traversal
* Python lists
* `input()`
* `.split()`
* `map()`
* Integer conversion
* `for` loops
* Conditional statements
* Indexing
* Running maximum
* Handling negative numbers
* Time complexity
* Space complexity
* Single-pass algorithms

---

# 🚀 TCS NQT Relevance

Finding the largest element is one of the simplest array problems, but the underlying **running maximum pattern** appears in many more difficult problems.

Understanding this pattern gives you a foundation for:

* Second largest element
* Second smallest element
* Maximum difference
* Kth largest element
* Kth smallest element
* Top two elements
* Maximum subarray-related problems
* Array optimization problems

### Recommended Thought Process During an Exam

When you see a problem asking for the maximum element:

```text
1. Do I need to sort the array?
        ↓
2. Can I solve it with one traversal?
        ↓
3. What should my initial maximum be?
        ↓
4. Can the array contain negative numbers?
        ↓
5. When should I update the maximum?
        ↓
6. What is the final complexity?
```

For this problem:

```text
Initial Maximum → arr[0]

Traversal       → O(N)

Auxiliary Space → O(1)

Sorting         → Not Required
```

---

# 📌 Summary

| Property                  | Value                              |
| ------------------------- | ---------------------------------- |
| **Problem**               | Find Largest Element               |
| **Technique**             | Linear Traversal                   |
| **Pattern**               | Running Maximum                    |
| **Time Complexity**       | `O(N)`                             |
| **Auxiliary Space**       | `O(1)`                             |
| **Sorting Used**          | ❌ No                               |
| **Built-in `max()` Used** | ❌ No                               |
| **Difficulty**            | Easy                               |
| **Language**              | Python                             |
| **Suitable For**          | DSA / Coding Assessments / TCS NQT |

---

## ⭐ Key Takeaway

> **You do not need to sort an array to find its largest element. Initialize the first element as the current maximum and scan the remaining elements once. Whenever a larger value is found, update the maximum.**

The core pattern is:

```text
Current Element
      ↓
Compare with largest
      ↓
Is it larger?
   ↙       ↘
 Yes        No
 ↓           ↓
Update     Continue
largest    traversal
```

Therefore:

```text
Time Complexity  → O(N)
Auxiliary Space  → O(1)
```

This simple **running maximum / single-pass technique** is one of the most important foundations for solving array-based DSA problems efficiently.


# 3.🔢 Find the Second Largest and Second Smallest Element in an Array

A fundamental **array traversal problem** commonly used in coding assessments such as **TCS NQT**.

The objective is to find the **second largest** and **second smallest distinct elements** in an array **without using Python's built-in sorting functions**.

The problem can be solved efficiently using a **single traversal** of the array.

---

## 📌 Problem Statement

Given an array of `N` integers, find and print:

* The **second largest distinct element**
* The **second smallest distinct element**

### Input Format

* The first line contains an integer `N`, representing the number of elements.
* The second line contains `N` space-separated integers representing the array.

### Output Format

Print the second largest and second smallest distinct elements.

---

## 🧪 Example

### Input

```text
6
10 5 8 20 3 15
```

### Output

```text
Second Largest: 15
Second Smallest: 5
```

### Explanation

Given array:

```text
10 5 8 20 3 15
```

If the elements were sorted:

```text
3 5 8 10 15 20
```

Therefore:

```text
Largest = 20
Second Largest = 15

Smallest = 3
Second Smallest = 5
```

Final result:

```text
Second Largest: 15
Second Smallest: 5
```

---

# 💡 Approach

Instead of sorting the array, maintain four variables while traversing it:

```text
largest
second_largest
smallest
second_smallest
```

During each iteration:

* If a new **largest** value is found, the previous largest becomes the second largest.
* If a new **smallest** value is found, the previous smallest becomes the second smallest.
* Intermediate values are checked to determine whether they should become the second largest or second smallest.
* Duplicate values are ignored so that the result contains **distinct elements**.

This gives an optimal:

```text
Time Complexity: O(N)
```

---

# 🧠 Algorithm

1. Read the number of elements `N`.
2. Read the array.
3. Initialize:

   * `largest = -∞`
   * `second_largest = -∞`
   * `smallest = +∞`
   * `second_smallest = +∞`
4. Traverse every element of the array.
5. For the largest values:

   * If the current element is greater than `largest`:

     * Move `largest` to `second_largest`.
     * Update `largest`.
   * Otherwise, if the current element is greater than `second_largest` and different from `largest`, update `second_largest`.
6. For the smallest values:

   * If the current element is smaller than `smallest`:

     * Move `smallest` to `second_smallest`.
     * Update `smallest`.
   * Otherwise, if the current element is smaller than `second_smallest` and different from `smallest`, update `second_smallest`.
7. Print the second largest and second smallest values.

---

# 💻 Python Code

```python
n = int(input())

arr = list(map(int, input().split()))

largest = float('-inf')
second_largest = float('-inf')

smallest = float('inf')
second_smallest = float('inf')

for num in arr:

    # Find largest and second largest
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

    # Find smallest and second smallest
    if num < smallest:
        second_smallest = smallest
        smallest = num

    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)
```

---

# 🔍 Code Explanation

## 1. Read the Size of the Array

```python
n = int(input())
```

`input()` reads the value as a string, while `int()` converts it into an integer.

For example:

```text
6
```

becomes:

```python
n = 6
```

---

## 2. Read the Array

```python
arr = list(map(int, input().split()))
```

This performs three operations.

### `input()`

Reads the complete line:

```text
10 5 8 20 3 15
```

### `.split()`

Splits the input into individual strings:

```python
["10", "5", "8", "20", "3", "15"]
```

### `map(int, ...)`

Converts each string into an integer:

```python
[10, 5, 8, 20, 3, 15]
```

Finally, `list()` creates the Python list.

So:

```python
arr = [10, 5, 8, 20, 3, 15]
```

---

# 🏆 Finding the Largest and Second Largest

## 3. Initialize the Variables

```python
largest = float('-inf')
second_largest = float('-inf')
```

`float('-inf')` represents **negative infinity**.

This is important because the array may contain negative numbers.

For example:

```text
-10 -5 -20 -3
```

If we initialized:

```python
largest = 0
```

the algorithm would fail because every value is smaller than `0`.

Using:

```python
largest = float('-inf')
```

allows the algorithm to work correctly with both positive and negative numbers.

---

## 4. Traverse the Array

```python
for num in arr:
```

This loop visits every element of the array.

For:

```python
[10, 5, 8, 20, 3, 15]
```

the values of `num` are:

```text
10
5
8
20
3
15
```

---

## 5. Find the Largest Element

```python
if num > largest:
```

If the current number is greater than the current largest value, we have found a new largest element.

---

## 6. Move the Previous Largest to Second Largest

```python
second_largest = largest
largest = num
```

Suppose:

```text
largest = 10
num = 20
```

Since:

```text
20 > 10
```

the previous largest becomes the second largest:

```text
second_largest = 10
largest = 20
```

This is a key step in the single-pass algorithm.

---

## 7. Update the Second Largest

```python
elif num > second_largest and num != largest:
    second_largest = num
```

This checks whether the current element should become the second largest.

For example:

```text
largest = 20
second_largest = 10
num = 15
```

Since:

```text
15 > 10
```

and:

```text
15 != 20
```

we update:

```text
second_largest = 15
```

---

# 🥇 Finding the Smallest and Second Smallest

## 8. Initialize the Variables

```python
smallest = float('inf')
second_smallest = float('inf')
```

`float('inf')` represents **positive infinity**.

This allows the algorithm to correctly handle both negative and positive numbers.

---

## 9. Find the Smallest Element

```python
if num < smallest:
```

If the current element is smaller than the current smallest value, we have found a new smallest element.

---

## 10. Move the Previous Smallest to Second Smallest

```python
second_smallest = smallest
smallest = num
```

For example:

```text
smallest = 10
num = 3
```

Since:

```text
3 < 10
```

we update:

```text
second_smallest = 10
smallest = 3
```

---

## 11. Update the Second Smallest

```python
elif num < second_smallest and num != smallest:
    second_smallest = num
```

This checks whether the current number should become the second smallest distinct value.

For example:

```text
smallest = 3
second_smallest = 10
num = 5
```

Since:

```text
5 < 10
```

and:

```text
5 != 3
```

we update:

```text
second_smallest = 5
```

---

# 📊 Dry Run

Consider:

```text
N = 6
Array = [10, 5, 8, 20, 3, 15]
```

## 🏆 Largest / Second Largest

| Step | Number | Largest | Second Largest |
| ---- | ------ | ------- | -------------- |
| 1    | 10     | 10      | -∞             |
| 2    | 5      | 10      | 5              |
| 3    | 8      | 10      | 8              |
| 4    | 20     | 20      | 10             |
| 5    | 3      | 20      | 10             |
| 6    | 15     | 20      | 15             |

Final values:

```text
Largest = 20
Second Largest = 15
```

---

## 🥇 Smallest / Second Smallest

| Step | Number | Smallest | Second Smallest |
| ---- | ------ | -------- | --------------- |
| 1    | 10     | 10       | +∞              |
| 2    | 5      | 5        | 10              |
| 3    | 8      | 5        | 8               |
| 4    | 20     | 5        | 8               |
| 5    | 3      | 3        | 5               |
| 6    | 15     | 3        | 5               |

Final values:

```text
Smallest = 3
Second Smallest = 5
```

Therefore:

```text
Second Largest: 15
Second Smallest: 5
```

---

# 🔁 Why Do We Check `num != largest`?

Consider:

```text
10 10 8 5
```

If duplicate values were allowed to become the second largest:

```text
Largest = 10
Second Largest = 10
```

But the problem asks for **distinct** values.

Therefore:

```text
Largest = 10
Second Largest = 8
```

That's why we use:

```python
num != largest
```

Similarly, for the second smallest:

```python
num != smallest
```

prevents duplicate values from being counted twice.

---

# 🚫 Why Not Sort the Array?

A straightforward solution would be:

```python
arr.sort()
```

Sorting could then be used to find the second smallest and second largest elements.

However, sorting requires:

```text
O(N log N)
```

time.

Our approach only requires:

```text
O(N)
```

time.

### Comparison

| Approach         | Time Complexity | Auxiliary Space           |
| ---------------- | --------------- | ------------------------- |
| Sorting          | `O(N log N)`    | Depends on implementation |
| Linear Traversal | `O(N)`          | `O(1)`                    |

For coding assessments such as **TCS NQT**, the single-pass approach is preferable when an `O(N)` solution is possible.

---

# ⏱️ Complexity Analysis

## Time Complexity

```text
O(N)
```

The array is traversed exactly once.

Each element requires only a constant number of comparisons and assignments.

Therefore:

```text
Time Complexity = O(N)
```

---

## Space Complexity

```text
O(1)
```

The algorithm uses only four additional variables:

```text
largest
second_largest
smallest
second_smallest
```

Therefore, the **auxiliary space complexity** is:

```text
O(1)
```

> **Note:** The input array itself requires `O(N)` memory. `O(1)` refers to the additional/auxiliary space used by the algorithm.

---

# 🧪 Test Cases

## Test Case 1 — Normal Case

### Input

```text
6
10 5 8 20 3 15
```

### Output

```text
Second Largest: 15
Second Smallest: 5
```

---

## Test Case 2 — Negative Numbers

### Input

```text
6
-10 -5 -20 -3 -15 -8
```

### Output

```text
Second Largest: -5
Second Smallest: -15
```

---

## Test Case 3 — Duplicate Elements

### Input

```text
7
10 10 8 8 5 5 3
```

### Output

```text
Second Largest: 8
Second Smallest: 5
```

---

## Test Case 4 — Unsorted Array

### Input

```text
6
50 10 30 70 20 60
```

### Output

```text
Second Largest: 60
Second Smallest: 20
```

---

## Test Case 5 — Positive and Negative Numbers

### Input

```text
7
-10 25 -5 40 15 -20 30
```

### Output

```text
Second Largest: 30
Second Smallest: -10
```

---

# ⚠️ Important Edge Case

If the array does not contain at least **two distinct values**, a second largest or second smallest element does not exist.

For example:

```text
4
5 5 5 5
```

There is only one distinct value:

```text
5
```

Therefore:

```text
Second Largest  → Does not exist
Second Smallest → Does not exist
```

A production-ready implementation should handle this case explicitly.

For coding assessments, always read the problem statement carefully to determine what output is expected when a second distinct value does not exist.

---

# 🎯 Key DSA Pattern

This problem teaches the:

## **Single Traversal / Running Maximum and Minimum Pattern**

Instead of sorting the array, maintain the best candidates while traversing.

```text
                 Array
                   ↓
          ┌────────┴────────┐
          ↓                 ↓
   Largest Side      Smallest Side
          ↓                 ↓
      largest           smallest
   second_largest    second_smallest
```

The general idea is:

```text
Read an element
      ↓
Check if it is a new largest
      ↓
Update largest / second largest
      ↓
Check if it is a new smallest
      ↓
Update smallest / second smallest
```

---

# 📚 What You Learn From This Problem

By solving this problem, you practice:

* Array traversal
* Python lists
* `input()`
* `.split()`
* `map()`
* Integer conversion
* `for` loops
* Conditional statements
* Multiple variable tracking
* `float('inf')`
* `float('-inf')`
* Handling duplicate values
* Finding distinct values
* Running maximum
* Running minimum
* Time complexity analysis
* Space complexity analysis
* Single-pass algorithms

---

# 🚀 TCS NQT Relevance

This problem is more useful than simply finding the largest or smallest element because it requires maintaining **multiple values simultaneously**.

It builds the foundation for problems involving:

* Second largest element
* Second smallest element
* Third largest element
* Kth largest element
* Kth smallest element
* Maximum and minimum differences
* Finding top two values
* Finding bottom two values
* Array optimization problems

### Recommended Thought Process During an Exam

When you see a problem asking for the second largest or second smallest:

```text
1. Do I need distinct values?
        ↓
2. Can I solve it without sorting?
        ↓
3. What variables do I need to maintain?
        ↓
4. What happens when a new maximum/minimum is found?
        ↓
5. How should duplicates be handled?
        ↓
6. What is the final complexity?
```

For this problem:

```text
Largest          → largest
Second Largest   → second_largest

Smallest        → smallest
Second Smallest → second_smallest

Traversal       → O(N)
Auxiliary Space → O(1)
```

---

# 📌 Summary

| Property             | Value                              |
| -------------------- | ---------------------------------- |
| **Problem**          | Second Largest & Second Smallest   |
| **Technique**        | Linear Traversal                   |
| **Pattern**          | Running Maximum & Minimum          |
| **Time Complexity**  | `O(N)`                             |
| **Auxiliary Space**  | `O(1)`                             |
| **Sorting Used**     | ❌ No                               |
| **Duplicate Values** | Handled                            |
| **Distinct Values**  | ✅ Yes                              |
| **Difficulty**       | Easy–Medium                        |
| **Language**         | Python                             |
| **Suitable For**     | DSA / Coding Assessments / TCS NQT |

---

## ⭐ Key Takeaway

> **Maintain the largest, second largest, smallest, and second smallest values while traversing the array once. This avoids sorting and reduces the time complexity to `O(N)`.**

The key pattern to remember is:

```text
New largest found
       ↓
Old largest → second largest
New value   → largest
```

and:

```text
New smallest found
       ↓
Old smallest → second smallest
New value    → smallest
```

This **single-pass technique** is an important foundation for more advanced array and optimization problems.

# 4.🔄 Reverse the Given Array

A fundamental **array manipulation problem** commonly useful for coding assessments such as **TCS NQT**.

The objective is to reverse the elements of a given array **in-place** without using Python's built-in `reverse()` function or array slicing.

The problem can be solved efficiently using the **two-pointer approach**.

---

## 📌 Problem Statement

Given an array of `N` integers, reverse the elements of the array and print the reversed array.

### Input Format

* The first line contains an integer `N`, representing the number of elements.
* The second line contains `N` space-separated integers representing the array.

### Output Format

Print the elements of the array in reverse order.

---

# 🧪 Example

### Input

```text
5
10 20 30 40 50
```

### Output

```text
50 40 30 20 10
```

### Explanation

The given array is:

```text
10 20 30 40 50
```

We reverse the array by swapping elements from both ends:

```text
10 20 30 40 50
↑           ↑
L           R
```

Swap `10` and `50`:

```text
50 20 30 40 10
```

Move the pointers towards the center:

```text
50 20 30 40 10
   ↑       ↑
   L       R
```

Swap `20` and `40`:

```text
50 40 30 20 10
```

The pointers meet at the middle, so the reversal is complete.

Therefore, the reversed array is:

```text
50 40 30 20 10
```

---

# 💡 Approach

We can solve this problem using the **two-pointer approach**.

Instead of creating another array, we use two pointers:

```text
left
right
```

The `left` pointer starts at the beginning of the array, while the `right` pointer starts at the end.

We repeatedly swap the elements at these two positions and move both pointers towards the center.

This allows us to reverse the array **in-place**.

---

# 🧠 Algorithm

1. Read the number of elements `N`.
2. Read the array.
3. Initialize:

   * `left = 0`
   * `right = N - 1`
4. Repeat while `left < right`:

   * Swap `arr[left]` and `arr[right]`.
   * Increment `left`.
   * Decrement `right`.
5. Print the reversed array.

---

# 💻 Python Code

```python
n = int(input())

arr = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print(*arr)
```

---

# 🔍 Code Explanation

## 1. Read the Size of the Array

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

For example:

```text
5
```

becomes:

```python
n = 5
```

---

## 2. Read the Array

```python
arr = list(map(int, input().split()))
```

This line performs three operations.

### `input()`

Reads the complete line:

```text
10 20 30 40 50
```

### `.split()`

Splits the input into individual strings:

```python
["10", "20", "30", "40", "50"]
```

### `map(int, ...)`

Converts each string into an integer:

```python
[10, 20, 30, 40, 50]
```

Finally, `list()` creates the Python list.

So:

```python
arr = [10, 20, 30, 40, 50]
```

---

# 🔄 Two-Pointer Approach

## 3. Initialize the Left Pointer

```python
left = 0
```

The `left` pointer starts at the first index of the array.

For:

```text
[10, 20, 30, 40, 50]
```

we have:

```text
left = 0
```

which points to:

```text
10
```

---

## 4. Initialize the Right Pointer

```python
right = n - 1
```

The `right` pointer starts at the last index.

If:

```text
n = 5
```

then:

```text
right = 4
```

So the pointer points to:

```text
50
```

The initial state is:

```text
10 20 30 40 50
↑           ↑
L           R
```

---

## 5. Continue While the Pointers Have Not Crossed

```python
while left < right:
```

The loop continues as long as the `left` pointer is before the `right` pointer.

Once:

```text
left >= right
```

all required swaps have been completed.

---

## 6. Swap the Elements

```python
arr[left], arr[right] = arr[right], arr[left]
```

This swaps the elements at the two pointer positions.

For example:

```text
10 20 30 40 50
↑           ↑
L           R
```

After the swap:

```text
50 20 30 40 10
```

Python allows both values to be swapped in a single statement without using a temporary variable.

---

## 7. Move the Left Pointer

```python
left += 1
```

After the first swap, move the `left` pointer one position towards the center.

For example:

```text
50 20 30 40 10
   ↑
   L
```

---

## 8. Move the Right Pointer

```python
right -= 1
```

Similarly, move the `right` pointer one position towards the center.

The pointers now become:

```text
50 20 30 40 10
   ↑       ↑
   L       R
```

---

## 9. Print the Reversed Array

```python
print(*arr)
```

The `*` operator unpacks the list elements.

Instead of printing:

```text
[50, 40, 30, 20, 10]
```

it prints:

```text
50 40 30 20 10
```

which matches the required output format.

---

# 📊 Dry Run

Consider:

```text
N = 5
Array = [10, 20, 30, 40, 50]
```

## Initial State

```text
10 20 30 40 50
↑           ↑
L           R
```

```text
left = 0
right = 4
```

---

## Step 1

Swap:

```text
10 ↔ 50
```

Array becomes:

```text
50 20 30 40 10
```

Move pointers:

```text
left = 1
right = 3
```

---

## Step 2

Current array:

```text
50 20 30 40 10
   ↑       ↑
   L       R
```

Swap:

```text
20 ↔ 40
```

Array becomes:

```text
50 40 30 20 10
```

Move pointers:

```text
left = 2
right = 2
```

---

## Step 3

Now:

```text
left = 2
right = 2
```

The condition:

```text
left < right
```

is false.

The loop terminates.

### Final Array

```text
50 40 30 20 10
```

---

# 🔁 Visual Representation

The two-pointer process can be represented as:

```text
Initial:

10  20  30  40  50
↑                   ↑
L                   R


After Swap 1:

50  20  30  40  10
    ↑           ↑
    L           R


After Swap 2:

50  40  30  20  10
        ↑   ↑
        L   R


Pointers meet:

50  40  30  20  10
        ↑
      L = R
```

The array is now completely reversed.

---

# 🚫 Why Not Use `reverse()`?

Python provides a built-in method:

```python
arr.reverse()
```

We could also use slicing:

```python
arr = arr[::-1]
```

Both approaches are valid Python.

However, for **DSA preparation and coding assessments**, implementing the reversal manually is better practice because it teaches the **two-pointer technique**.

The two-pointer pattern can be reused in many problems involving:

* Array reversal
* String reversal
* Palindrome checking
* Pair-sum problems
* Two-pointer searching
* In-place array manipulation
* Partitioning problems

The objective is to understand the underlying algorithm rather than simply use a built-in function.

---

# 🎯 Key DSA Pattern

This problem teaches the:

## **Two-Pointer Technique**

The general idea is:

```text
Initialize two pointers
       ↓
Left → beginning
Right → end
       ↓
Compare / Swap / Process
       ↓
Move Left forward
Move Right backward
       ↓
Repeat until pointers meet
```

For this problem:

```text
left  → 0
right → N - 1
```

Then:

```text
arr[left] ↔ arr[right]
```

followed by:

```text
left += 1
right -= 1
```

This continues until:

```text
left >= right
```

---

# ⏱️ Complexity Analysis

## Time Complexity

```text
O(N)
```

Each element is processed at most once.

Although the loop performs approximately `N / 2` swaps, constants are ignored in Big-O notation.

Therefore:

```text
Time Complexity = O(N)
```

---

## Space Complexity

```text
O(1)
```

The array is reversed **in-place**.

We only use two pointer variables:

```text
left
right
```

No additional array is created.

Therefore, the **auxiliary space complexity** is:

```text
O(1)
```

> **Note:** The input array itself requires `O(N)` memory. `O(1)` refers to the additional/auxiliary space used by the reversal algorithm.

---

# 🧪 Test Cases

## Test Case 1 — Normal Case

### Input

```text
5
10 20 30 40 50
```

### Output

```text
50 40 30 20 10
```

---

## Test Case 2 — Even Number of Elements

### Input

```text
6
1 2 3 4 5 6
```

### Output

```text
6 5 4 3 2 1
```

---

## Test Case 3 — Odd Number of Elements

### Input

```text
5
1 2 3 4 5
```

### Output

```text
5 4 3 2 1
```

---

## Test Case 4 — Negative Numbers

### Input

```text
5
-10 -20 -30 -40 -50
```

### Output

```text
-50 -40 -30 -20 -10
```

---

## Test Case 5 — Duplicate Elements

### Input

```text
6
10 20 10 30 20 10
```

### Output

```text
10 20 30 10 20 10
```

---

## Test Case 6 — Single Element

### Input

```text
1
25
```

### Output

```text
25
```

A single-element array is already reversed.

---

# ⚠️ Important Edge Cases

## 1. Single Element

```text
[10]
```

The array remains:

```text
[10]
```

No swap is required.

---

## 2. Two Elements

```text
[10, 20]
```

After one swap:

```text
[20, 10]
```

---

## 3. Duplicate Elements

For:

```text
[5, 10, 5, 20, 10]
```

the reversal is performed normally.

Duplicates do not require any special handling.

---

## 4. Negative Numbers

The algorithm works exactly the same way for negative values.

For:

```text
[-5, -10, -15]
```

the result is:

```text
[-15, -10, -5]
```

---

# 📚 What You Learn From This Problem

By solving this problem, you practice:

* Array input handling
* Python lists
* `input()`
* `.split()`
* `map()`
* Integer conversion
* Array indexing
* `while` loops
* Multiple pointer variables
* Two-pointer technique
* Swapping elements
* In-place array manipulation
* `print(*arr)`
* Time complexity analysis
* Space complexity analysis

---

# 🚀 TCS NQT Relevance

This is an important **basic array manipulation problem** because it introduces the **two-pointer technique**.

The technique is useful for solving more advanced coding problems efficiently.

### Recommended Thought Process During an Exam

When you see a problem asking you to reverse an array:

```text
1. Can I reverse it in-place?
        ↓
2. Can I use two pointers?
        ↓
3. One pointer starts from the beginning.
        ↓
4. One pointer starts from the end.
        ↓
5. Swap the two elements.
        ↓
6. Move both pointers toward the center.
        ↓
7. Stop when the pointers meet.
```

For this problem:

```text
Left Pointer   → 0
Right Pointer  → N - 1

Swap           → arr[left], arr[right]
Move Left      → left += 1
Move Right     → right -= 1

Time           → O(N)
Auxiliary Space → O(1)
```

---

# 📌 Summary

| Property                  | Value                              |
| ------------------------- | ---------------------------------- |
| Problem                   | Reverse an Array                   |
| Technique                 | Two-Pointer                        |
| Pattern                   | In-Place Array Manipulation        |
| Time Complexity           | `O(N)`                             |
| Auxiliary Space           | `O(1)`                             |
| Built-in `reverse()` Used | ❌ No                               |
| Array Slicing Used        | ❌ No                               |
| In-Place                  | ✅ Yes                              |
| Difficulty                | Easy                               |
| Language                  | Python                             |
| Suitable For              | DSA / Coding Assessments / TCS NQT |

---

## ⭐ Key Takeaway

> **Use two pointers—one at the beginning and one at the end—swap their elements, and move both pointers toward the center until the array is completely reversed.**

The key pattern to remember is:

```text
Left →→→       ←←← Right
       Swap
        ↓
Left moves right
Right moves left
```

This **two-pointer technique** is one of the most important patterns to learn for array and string problems.


# 5. 🔢 Count Frequency of Each Element in an Array

A fundamental **array traversal and frequency counting problem** commonly useful for coding assessments such as **TCS NQT**.

The objective is to find and print the **frequency of each distinct element** present in a given array.

The problem can be solved efficiently using a **Python dictionary (hash map)** to store each element and its corresponding frequency.

---

# 📌 Problem Statement

Given an array of `N` integers, count how many times each distinct element appears in the array.

### Input Format

* The first line contains an integer `N`, representing the number of elements.
* The second line contains `N` space-separated integers representing the array.

### Output Format

Print each distinct element along with its frequency.

The elements are printed in the order in which they first appear in the array.

---

# 🧪 Example

### Input

```text
7
10 20 10 30 20 10 40
```

### Output

```text
10 3
20 2
30 1
40 1
```

### Explanation

The given array is:

```text
10 20 10 30 20 10 40
```

We count how many times each element occurs:

```text
10 → 3 times
20 → 2 times
30 → 1 time
40 → 1 time
```

Therefore, the frequency of each element is:

```text
10 3
20 2
30 1
40 1
```

---

# 💡 Approach

We can solve this problem efficiently using a **dictionary/hash map**.

A dictionary stores data in the form:

```text
element → frequency
```

For example:

```text
10 → 3
20 → 2
30 → 1
40 → 1
```

We traverse the array once.

For every element:

* If the element already exists in the dictionary, increase its frequency by `1`.
* Otherwise, add the element to the dictionary with frequency `1`.

This allows us to count all frequencies in a **single traversal**.

---

# 🧠 Algorithm

1. Read the number of elements `N`.
2. Read the array.
3. Create an empty dictionary called `frequency`.
4. Traverse every element in the array.
5. For each element:

   * If the element already exists in `frequency`, increment its count.
   * Otherwise, initialize its count to `1`.
6. Traverse the dictionary.
7. Print each element along with its frequency.

---

# 💻 Python Code

```python
n = int(input())

arr = list(map(int, input().split()))

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num in frequency:
    print(num, frequency[num])
```

---

# 🔍 Code Explanation

## 1. Read the Size of the Array

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

For example:

```text
7
```

becomes:

```python
n = 7
```

---

## 2. Read the Array

```python
arr = list(map(int, input().split()))
```

This line performs three operations.

### `input()`

Reads the complete line:

```text
10 20 10 30 20 10 40
```

### `.split()`

Splits the input into individual strings:

```python
["10", "20", "10", "30", "20", "10", "40"]
```

### `map(int, ...)`

Converts each string into an integer:

```python
[10, 20, 10, 30, 20, 10, 40]
```

Finally, `list()` creates the Python list.

So:

```python
arr = [10, 20, 10, 30, 20, 10, 40]
```

---

# 📊 Frequency Counting Using a Dictionary

## 3. Create an Empty Dictionary

```python
frequency = {}
```

This dictionary will store:

```text
element → frequency
```

Initially:

```python
{}
```

As we process the array, it will become:

```python
{10: 3, 20: 2, 30: 1, 40: 1}
```

---

## 4. Traverse the Array

```python
for num in arr:
```

This loop visits every element in the array.

For:

```text
[10, 20, 10, 30, 20, 10, 40]
```

the values of `num` will be:

```text
10
20
10
30
20
10
40
```

---

## 5. Check Whether the Element Already Exists

```python
if num in frequency:
```

This checks whether the current element already exists as a key in the dictionary.

For example, after processing:

```text
10
20
```

the dictionary is:

```python
{10: 1, 20: 1}
```

When `10` appears again:

```python
if 10 in frequency:
```

the condition is `True`.

---

## 6. Increase the Frequency

```python
frequency[num] += 1
```

If the element already exists, increase its frequency by `1`.

For example:

```python
frequency[10] = 1
```

After another `10`:

```python
frequency[10] = 2
```

After another `10`:

```python
frequency[10] = 3
```

---

## 7. Add a New Element

```python
else:
    frequency[num] = 1
```

If the element does not exist in the dictionary, add it with an initial frequency of `1`.

For example, when `30` is encountered for the first time:

```python
frequency[30] = 1
```

The dictionary becomes:

```python
{10: 2, 20: 1, 30: 1}
```

---

## 8. Traverse the Frequency Dictionary

```python
for num in frequency:
```

After the entire array has been processed, the dictionary contains every distinct element and its frequency.

For example:

```python
{10: 3, 20: 2, 30: 1, 40: 1}
```

The loop visits:

```text
10
20
30
40
```

Because Python dictionaries preserve insertion order, the elements are printed in the order in which they first appeared.

---

## 9. Print the Element and Frequency

```python
print(num, frequency[num])
```

This prints the element followed by its frequency.

For example:

```text
10 3
```

means:

```text
Element = 10
Frequency = 3
```

The final output is:

```text
10 3
20 2
30 1
40 1
```

---

# 📊 Dry Run

Consider:

```text
N = 7
Array = [10, 20, 10, 30, 20, 10, 40]
```

We process each element one by one.

| Step | Current Element | Frequency Dictionary           |
| ---- | --------------- | ------------------------------ |
| 1    | 10              | `{10: 1}`                      |
| 2    | 20              | `{10: 1, 20: 1}`               |
| 3    | 10              | `{10: 2, 20: 1}`               |
| 4    | 30              | `{10: 2, 20: 1, 30: 1}`        |
| 5    | 20              | `{10: 2, 20: 2, 30: 1}`        |
| 6    | 10              | `{10: 3, 20: 2, 30: 1}`        |
| 7    | 40              | `{10: 3, 20: 2, 30: 1, 40: 1}` |

### Final Frequency Table

```text
10 → 3
20 → 2
30 → 1
40 → 1
```

Therefore:

```text
10 3
20 2
30 1
40 1
```

---

# 🔁 How the Dictionary Changes

The frequency dictionary evolves as follows.

### Initially

```python
{}
```

### After processing `10`

```python
{10: 1}
```

### After processing `20`

```python
{10: 1, 20: 1}
```

### After processing another `10`

```python
{10: 2, 20: 1}
```

### After processing `30`

```python
{10: 2, 20: 1, 30: 1}
```

### After processing another `20`

```python
{10: 2, 20: 2, 30: 1}
```

### After processing another `10`

```python
{10: 3, 20: 2, 30: 1}
```

### After processing `40`

```python
{10: 3, 20: 2, 30: 1, 40: 1}
```

---

# 🚫 Why Not Use `count()`?

Python provides a built-in `count()` method:

```python
arr.count(num)
```

We could write:

```python
for num in arr:
    print(num, arr.count(num))
```

However, this approach has a major problem.

`count()` traverses the array every time it is called.

If the array contains `N` elements and we call `count()` for every element, the time complexity can become:

```text
O(N²)
```

For example:

```text
Array = [10, 20, 10, 30, 20, 10]
```

The array is repeatedly scanned to count each element.

The dictionary approach is much more efficient because we count every element during a **single traversal**.

---

# 🚫 Why Not Use Nested Loops?

Another possible approach is:

```python
for i in range(n):
    count = 0

    for j in range(n):
        if arr[i] == arr[j]:
            count += 1
```

This also requires:

```text
O(N²)
```

time complexity.

The dictionary/hash map approach reduces the average time complexity to:

```text
O(N)
```

Therefore, it is the preferred approach for larger arrays.

---

# ⏱️ Complexity Analysis

## Time Complexity

```text
O(N)
```

We traverse the array once to build the frequency dictionary.

Dictionary lookup and update operations are **O(1) on average**.

Therefore:

```text
Time Complexity = O(N)
```

> **Note:** Python dictionary operations such as membership checking, insertion, and updating are average-case `O(1)`.

---

## Space Complexity

```text
O(K)
```

where `K` is the number of **distinct elements** in the array.

For example:

```text
[10, 10, 10, 10]
```

has:

```text
N = 4
K = 1
```

while:

```text
[10, 20, 30, 40]
```

has:

```text
N = 4
K = 4
```

Therefore, the frequency dictionary requires space proportional to the number of distinct elements.

```text
Auxiliary Space = O(K)
```

In the worst case, when every element is unique:

```text
K = N
```

so the space complexity becomes:

```text
O(N)
```

---

# 🧪 Test Cases

## Test Case 1 — Normal Case

### Input

```text
7
10 20 10 30 20 10 40
```

### Output

```text
10 3
20 2
30 1
40 1
```

---

## Test Case 2 — All Elements Are Unique

### Input

```text
5
10 20 30 40 50
```

### Output

```text
10 1
20 1
30 1
40 1
50 1
```

---

## Test Case 3 — All Elements Are Same

### Input

```text
5
7 7 7 7 7
```

### Output

```text
7 5
```

---

## Test Case 4 — Negative Numbers

### Input

```text
7
-5 -10 -5 -20 -10 -5 -20
```

### Output

```text
-5 3
-10 2
-20 2
```

---

## Test Case 5 — Positive and Negative Numbers

### Input

```text
8
10 -5 10 -5 20 -5 30 10
```

### Output

```text
10 3
-5 3
20 1
30 1
```

---

## Test Case 6 — Duplicate Elements

### Input

```text
8
5 10 5 20 10 5 20 10
```

### Output

```text
5 3
10 3
20 2
```

---

# ⚠️ Important Edge Cases

## 1. Single Element

For:

```text
1
25
```

the frequency is:

```text
25 1
```

---

## 2. All Elements Are Identical

For:

```text
5
10 10 10 10 10
```

there is only one distinct element:

```text
10 5
```

---

## 3. All Elements Are Unique

For:

```text
4
10 20 30 40
```

every element has frequency `1`:

```text
10 1
20 1
30 1
40 1
```

---

## 4. Negative Numbers

The dictionary approach works with negative integers without any special modification.

For:

```text
-2 -5 -2 -10
```

the result is:

```text
-2 2
-5 1
-10 1
```

---

# 🎯 Key DSA Pattern

This problem teaches the:

## **Frequency Counting / Hash Map Pattern**

The general idea is:

```text
Read an element
       ↓
Check if it exists in the dictionary
       ↓
    ┌──┴──┐
    ↓     ↓
   Yes    No
    ↓     ↓
Increase  Set to 1
frequency
    ↓     ↓
    └──┬──┘
       ↓
Process next element
```

The dictionary stores:

```text
Element → Number of Occurrences
```

For example:

```text
10 → 3
20 → 2
30 → 1
40 → 1
```

This pattern is extremely useful in array and string problems.

---

# 📚 What You Learn From This Problem

By solving this problem, you practice:

* Array input handling
* Python lists
* `input()`
* `.split()`
* `map()`
* Integer conversion
* `for` loops
* Conditional statements
* Python dictionaries
* Key-value pairs
* Dictionary membership checking
* Frequency counting
* Hash map technique
* Handling duplicate values
* Handling negative values
* Time complexity analysis
* Space complexity analysis
* Single-pass algorithms

---

# 🚀 TCS NQT Relevance

Frequency counting is an important pattern for coding assessments such as **TCS NQT**.

The same concept can be used in many problems involving arrays and strings.

### Problems Based on the Same Pattern

* Count frequency of each element
* Find the most frequent element
* Find the least frequent element
* Find the first non-repeating element
* Find duplicate elements
* Count duplicate elements
* Find unique elements
* Find the frequency of a particular number
* Check whether two arrays contain the same frequencies
* Check whether two strings are anagrams
* Count character frequency in a string

### Recommended Thought Process During an Exam

When you see a problem involving frequency:

```text
1. Do I need to count occurrences?
        ↓
2. Can I use a dictionary/hash map?
        ↓
3. What should be the key?
        ↓
4. What should be the value?
        ↓
5. Can I solve it in one traversal?
        ↓
6. What is the final complexity?
```

For this problem:

```text
Key       → Array Element
Value     → Frequency
Traversal → O(N)
Space     → O(K)
```

where `K` is the number of distinct elements.

---

# 📌 Summary

| Property                | Value                              |
| ----------------------- | ---------------------------------- |
| Problem                 | Count Frequency of Each Element    |
| Technique               | Frequency Counting                 |
| Pattern                 | Hash Map / Dictionary              |
| Time Complexity         | `O(N)` Average                     |
| Auxiliary Space         | `O(K)`                             |
| Worst-Case Space        | `O(N)`                             |
| Built-in `count()` Used | ❌ No                               |
| Nested Loop Used        | ❌ No                               |
| Duplicate Values        | ✅ Handled                          |
| Negative Values         | ✅ Handled                          |
| Difficulty              | Easy–Medium                        |
| Language                | Python                             |
| Suitable For            | DSA / Coding Assessments / TCS NQT |

---

## ⭐ Key Takeaway

> **Use a dictionary to store each array element as a key and its frequency as the value. Traverse the array once and update the frequency whenever an element is encountered.**

The key pattern to remember is:

```text
Element
   ↓
Exists in Dictionary?
   ↓
 ┌───────┴───────┐
 ↓               ↓
Yes              No
 ↓                ↓
Count += 1      Count = 1
```

This **frequency counting / hash map technique** is one of the most important patterns for solving array and string problems efficiently.


# 6.🔢 Rearrange Array in Increasing and Decreasing Order

A fundamental **array sorting and rearrangement problem** commonly useful for coding assessments such as **TCS NQT**.

The objective is to rearrange the elements of a given array such that the **first half is in increasing order** and the **second half is in decreasing order**.

The problem can be solved by first sorting the array and then rearranging its two halves.

---

# 📌 Problem Statement

Given an array of `N` integers, rearrange the elements such that:

* The first half of the array is arranged in **increasing order**.
* The second half of the array is arranged in **decreasing order**.

### Input Format

* The first line contains an integer `N`, representing the number of elements.
* The second line contains `N` space-separated integers representing the array.

### Output Format

Print the rearranged array where:

* The first half is in increasing order.
* The second half is in decreasing order.

---

# 🧪 Example

### Input

```text
8
10 5 20 8 15 3 12 7
```

### Output

```text
3 5 7 8 20 15 12 10
```

### Explanation

The given array is:

```text
10 5 20 8 15 3 12 7
```

First, sort the array in increasing order:

```text
3 5 7 8 10 12 15 20
```

Now divide the sorted array into two halves:

### Increasing Half

```text
3 5 7 8
```

### Second Half

```text
10 12 15 20
```

Reverse the second half:

```text
20 15 12 10
```

Therefore, the final rearranged array is:

```text
3 5 7 8 20 15 12 10
```

---

# 💡 Approach

We can solve this problem using **sorting and array rearrangement**.

The approach consists of three main steps:

### Step 1: Sort the Array

Sort the complete array in increasing order.

```python
arr.sort()
```

For example:

```text
10 5 20 8 15 3 12 7
```

becomes:

```text
3 5 7 8 10 12 15 20
```

### Step 2: Divide the Array

Find the middle position:

```python
mid = n // 2
```

Then divide the sorted array into two parts:

```text
First Half:
3 5 7 8

Second Half:
10 12 15 20
```

### Step 3: Reverse the Second Half

The first half remains in increasing order.

The second half is reversed to make it decreasing:

```text
20 15 12 10
```

Finally, combine both parts:

```text
3 5 7 8 20 15 12 10
```

---

# 🧠 Algorithm

1. Read the number of elements `N`.
2. Read the array.
3. Sort the array in increasing order.
4. Calculate the middle index using `N // 2`.
5. Store the first half in `increasing`.
6. Store the second half in `decreasing`.
7. Reverse the `decreasing` part.
8. Combine the two parts.
9. Print the resulting array.

---

# 💻 Python Code

```python
n = int(input())

arr = list(map(int, input().split()))

arr.sort()

mid = n // 2

increasing = arr[:mid]
decreasing = arr[mid:]

decreasing.reverse()

result = increasing + decreasing

print(*result)
```

---

# 🔍 Code Explanation

## 1. Read the Size of the Array

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

For example:

```text
8
```

becomes:

```python
n = 8
```

---

## 2. Read the Array

```python
arr = list(map(int, input().split()))
```

This line performs three operations.

### `input()`

Reads the complete line:

```text
10 5 20 8 15 3 12 7
```

### `.split()`

Splits the input into individual strings:

```python
["10", "5", "20", "8", "15", "3", "12", "7"]
```

### `map(int, ...)`

Converts each string into an integer:

```python
[10, 5, 20, 8, 15, 3, 12, 7]
```

Finally, `list()` creates the Python list.

So:

```python
arr = [10, 5, 20, 8, 15, 3, 12, 7]
```

---

# 📊 Sorting and Rearranging the Array

## 3. Sort the Array

```python
arr.sort()
```

This sorts the array in increasing order.

Before sorting:

```text
10 5 20 8 15 3 12 7
```

After sorting:

```text
3 5 7 8 10 12 15 20
```

---

## 4. Find the Middle Position

```python
mid = n // 2
```

The `//` operator performs integer division.

For:

```text
n = 8
```

we get:

```text
mid = 8 // 2
mid = 4
```

Therefore, the array is divided at index `4`.

---

## 5. Store the Increasing Half

```python
increasing = arr[:mid]
```

This takes all elements from the beginning of the array up to, but not including, `mid`.

For:

```python
arr = [3, 5, 7, 8, 10, 12, 15, 20]
```

we get:

```python
increasing = [3, 5, 7, 8]
```

This part is already in increasing order because the complete array was sorted first.

---

## 6. Store the Second Half

```python
decreasing = arr[mid:]
```

This takes all elements from `mid` to the end.

Therefore:

```python
decreasing = [10, 12, 15, 20]
```

At this point, this part is still in increasing order.

---

## 7. Reverse the Second Half

```python
decreasing.reverse()
```

The second half becomes:

```text
[20, 15, 12, 10]
```

Now it is in decreasing order.

---

## 8. Combine Both Parts

```python
result = increasing + decreasing
```

The two lists are joined together.

### Increasing

```text
3 5 7 8
```

### Decreasing

```text
20 15 12 10
```

### Result

```text
3 5 7 8 20 15 12 10
```

---

## 9. Print the Result

```python
print(*result)
```

The `*` operator unpacks the list elements.

Instead of printing:

```text
[3, 5, 7, 8, 20, 15, 12, 10]
```

it prints:

```text
3 5 7 8 20 15 12 10
```

which matches the required output format.

---

# 📊 Dry Run

Consider:

```text
N = 8
Array = [10, 5, 20, 8, 15, 3, 12, 7]
```

## Step 1 — Sort the Array

### Original

```text
10 5 20 8 15 3 12 7
```

### Sorted

```text
3 5 7 8 10 12 15 20
```

---

## Step 2 — Find the Middle

```text
N = 8

mid = 8 // 2
mid = 4
```

---

## Step 3 — Divide the Array

### First Half

```text
3 5 7 8
```

### Second Half

```text
10 12 15 20
```

---

## Step 4 — Reverse the Second Half

### Before

```text
10 12 15 20
```

### After

```text
20 15 12 10
```

---

## Step 5 — Combine Both Parts

```text
3 5 7 8 + 20 15 12 10
```

### Final Result

```text
3 5 7 8 20 15 12 10
```

---

# 🔁 Visual Representation

The complete process can be represented as:

```text
Original Array
      ↓
    Sort
      ↓
3  5  7  8  10  12  15  20
      ↓
  Split at middle
      ↓
3  5  7  8 | 10  12  15  20
      ↓
First Half  |  Reverse Second Half
      ↓
3  5  7  8 | 20  15  12  10
      ↓
     Combine
        ↓
3  5  7  8  20  15  12  10
```

---

# 🚫 Why Not Use Only `sort()`?

Simply sorting the array:

```python
arr.sort()
```

produces:

```text
3 5 7 8 10 12 15 20
```

But this does **not** satisfy the required arrangement because the second half is still increasing.

We need:

```text
3 5 7 8 20 15 12 10
```

Therefore, after sorting, the second half must be reversed.

---

# 🚫 Why Not Use Nested Loops?

We could manually compare and rearrange elements using nested loops.

However, that would make the solution unnecessarily complicated and could result in:

```text
O(N²)
```

time complexity.

Python's sorting algorithm provides an efficient way to arrange the elements.

The important part is understanding how to manipulate the sorted array into the required increasing/decreasing structure.

---

# ⏱️ Complexity Analysis

## Time Complexity

```text
O(N log N)
```

The dominant operation is:

```python
arr.sort()
```

Python's sorting algorithm takes:

```text
O(N log N)
```

time in the general case.

The remaining operations such as slicing, reversing, and combining the two halves are linear:

```text
O(N)
```

Therefore, the overall complexity is:

```text
Time Complexity = O(N log N)
```

---

## Space Complexity

The solution creates additional lists:

```text
increasing
decreasing
result
```

Therefore, the additional space used is proportional to the number of elements.

```text
Auxiliary Space = O(N)
```

> **Note:** Python's sorting implementation also uses additional memory internally. The exact implementation details are handled by Python.

---

# 🧪 Test Cases

## Test Case 1 — Normal Case

### Input

```text
8
10 5 20 8 15 3 12 7
```

### Output

```text
3 5 7 8 20 15 12 10
```

---

## Test Case 2 — Even Number of Elements

### Input

```text
6
1 6 3 5 2 4
```

### Output

```text
1 2 3 6 5 4
```

---

## Test Case 3 — Odd Number of Elements

### Input

```text
5
10 2 8 4 6
```

### Output

```text
2 4 8 10 6
```

---

## Test Case 4 — Negative Numbers

### Input

```text
6
-10 -5 -20 -2 -15 -8
```

### Output

```text
-20 -15 -10 -2 -5 -8
```

---

## Test Case 5 — Duplicate Elements

### Input

```text
8
10 5 10 20 5 15 20 10
```

### Output

```text
5 5 10 10 20 20 15 10
```

---

## Test Case 6 — Already Sorted Array

### Input

```text
6
1 2 3 4 5 6
```

### Output

```text
1 2 3 6 5 4
```

---

# ⚠️ Important Edge Cases

## 1. Single Element

For:

```text
1
25
```

the result remains:

```text
25
```

There is only one element, so no rearrangement is required.

---

## 2. Two Elements

For:

```text
2
20 10
```

after sorting:

```text
10 20
```

The first half contains `10` and the second half contains `20`.

Final result:

```text
10 20
```

---

## 3. Duplicate Elements

For:

```text
8
10 5 10 20 5 15 20 10
```

duplicates are retained.

The algorithm does not remove or modify duplicate values.

---

## 4. Negative Numbers

The sorting approach works with negative values as well.

For:

```text
-10 -5 -20 -2 -15 -8
```

the sorted array is:

```text
-20 -15 -10 -8 -5 -2
```

The required arrangement becomes:

```text
-20 -15 -10 -2 -5 -8
```

---

# 🎯 Key DSA Pattern

This problem teaches the:

## **Sorting + Array Partitioning Pattern**

The general idea is:

```text
Sort the array
      ↓
Find the middle
      ↓
Separate into two halves
      ↓
First half → Increasing
      ↓
Second half → Reverse
      ↓
Combine both halves
```

The important operations are:

```text
arr.sort()
     ↓
mid = n // 2
     ↓
arr[:mid]
     ↓
arr[mid:]
     ↓
reverse()
```

This pattern is useful for problems where an array must be rearranged according to different ordering rules.

---

# 📚 What You Learn From This Problem

By solving this problem, you practice:

* Array input handling
* Python lists
* `input()`
* `.split()`
* `map()`
* Integer conversion
* Python sorting
* `.sort()`
* Integer division
* Array slicing
* List reversal
* List concatenation
* Array partitioning
* Increasing order
* Decreasing order
* Time complexity analysis
* Space complexity analysis

---

# 🚀 TCS NQT Relevance

This is a useful **array sorting and manipulation problem** for coding assessments such as **TCS NQT**.

It combines multiple basic concepts instead of testing only one operation.

### Problems Based on Similar Concepts

* Sort an array in increasing order
* Sort an array in decreasing order
* Rearrange positive and negative elements
* Rearrange even and odd elements
* Move zeros to the end
* Move negative elements to one side
* Separate elements based on a condition
* Find the median of an array
* Find the Kth largest element
* Find the Kth smallest element

### Recommended Thought Process During an Exam

When you see a problem involving increasing and decreasing arrangement:

```text
1. What exact ordering is required?
        ↓
2. Can sorting simplify the problem?
        ↓
3. Where should the array be divided?
        ↓
4. Which part should be increasing?
        ↓
5. Which part should be decreasing?
        ↓
6. Can I rearrange the parts without nested loops?
        ↓
7. What is the final complexity?
```

For this problem:

```text
Sorting          → O(N log N)
Middle           → N // 2
First Half       → Increasing
Second Half      → Decreasing
Final Complexity → O(N log N)
```

---

# 📌 Summary

| Property           | Value                                            |
| ------------------ | ------------------------------------------------ |
| Problem            | Rearrange Array in Increasing & Decreasing Order |
| Technique          | Sorting + Partitioning                           |
| Pattern            | Array Rearrangement                              |
| Time Complexity    | `O(N log N)`                                     |
| Auxiliary Space    | `O(N)`                                           |
| Sorting Used       | ✅ Yes                                            |
| Array Slicing Used | ✅ Yes                                            |
| Duplicate Values   | ✅ Handled                                        |
| Negative Values    | ✅ Handled                                        |
| Difficulty         | Easy–Medium                                      |
| Language           | Python                                           |
| Suitable For       | DSA / Coding Assessments / TCS NQT               |

---

## ⭐ Key Takeaway

> **Sort the array first, keep the first half in increasing order, reverse the second half to make it decreasing, and combine both parts.**

The key pattern to remember is:

```text
Original Array
      ↓
    Sort
      ↓
3  5  7  8  10  12  15  20
      ↓
  Split at middle
      ↓
3  5  7  8 | 10  12  15  20
      ↓
Reverse second half
      ↓
3  5  7  8 | 20  15  12  10
      ↓
Final Answer
```

This **sorting + partitioning technique** is a useful foundation for more advanced array rearrangement and ordering problems.


# 7. ➕ Calculate Sum of the Elements of an Array

A fundamental **array traversal and accumulation problem** commonly useful for coding assessments such as **TCS NQT**.

The objective is to calculate the **sum of all elements** present in a given array without using Python's built-in **`sum()`** function.

The problem can be solved efficiently using **linear traversal** and a **running sum**.

---

## 📌 Problem Statement

Given an array of `N` integers, calculate and print the sum of all elements present in the array.

### Input Format

* The first line contains an integer `N`, representing the number of elements.
* The second line contains `N` space-separated integers representing the array.

### Output Format

Print the sum of all elements in the array.

---

# 🧪 Example

### Input

```text
5
10 20 30 40 50
```

### Output

```text
150
```

### Explanation

The given array is:

```text
10 20 30 40 50
```

We add each element to a running total:

```text
10 → total = 10
20 → total = 30
30 → total = 60
40 → total = 100
50 → total = 150
```

Therefore, the sum of all elements is:

```text
150
```

---

# 💡 Approach

We can solve this problem using **linear traversal** of the array.

The main idea is to maintain a variable called `total` that stores the sum of all elements processed so far.

### Step 1: Initialize the Sum

Start with:

```python
total = 0
```

Initially, no elements have been added, so the total is `0`.

### Step 2: Traverse the Array

Visit every element of the array:

```python
for num in arr:
```

### Step 3: Add Each Element

Add the current element to `total`:

```python
total += num
```

### Step 4: Print the Result

After processing all elements:

```python
print(total)
```

The final value stored in `total` is the sum of all elements.

---

# 🧠 Algorithm

1. Read the number of elements `N`.
2. Read the array.
3. Initialize `total = 0`.
4. Traverse every element of the array.
5. Add the current element to `total`.
6. After the traversal is complete, print `total`.

---

# 💻 Python Code

```python
n = int(input())

arr = list(map(int, input().split()))

total = 0

for num in arr:
    total += num

print(total)
```

---

# 🔍 Code Explanation

## 1. Read the Size of the Array

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

For example:

```text
5
```

becomes:

```python
n = 5
```

---

## 2. Read the Array

```python
arr = list(map(int, input().split()))
```

This line performs three operations.

### `input()`

Reads the complete line:

```text
10 20 30 40 50
```

### `.split()`

Splits the input into individual strings:

```python
["10", "20", "30", "40", "50"]
```

### `map(int, ...)`

Converts each string into an integer:

```python
[10, 20, 30, 40, 50]
```

Finally, `list()` creates the Python list.

So:

```python
arr = [10, 20, 30, 40, 50]
```

---

# ➕ Calculating the Sum

## 3. Initialize the Running Sum

```python
total = 0
```

We start the sum at `0`.

At the beginning:

```text
total = 0
```

As we process each element, `total` will be updated.

---

## 4. Traverse the Array

```python
for num in arr:
```

This loop visits every element in the array.

For:

```text
[10, 20, 30, 40, 50]
```

the value of `num` will be:

```text
10
20
30
40
50
```

---

## 5. Add Each Element to the Total

```python
total += num
```

This is shorthand for:

```python
total = total + num
```

For example, when:

```text
total = 10
num = 20
```

the operation becomes:

```text
total = 10 + 20
```

Therefore:

```text
total = 30
```

The process continues for every element.

---

## 6. Print the Final Sum

```python
print(total)
```

After all elements have been processed, `total` contains the sum of the entire array.

For example:

```text
total = 150
```

Therefore:

```text
150
```

is printed.

---

# 📊 Dry Run

Consider:

```text
N = 5
Array = [10, 20, 30, 40, 50]
```

| Step    | Current Element | Total Before | Calculation | Total After |
| ------- | --------------- | ------------ | ----------- | ----------- |
| Initial | —               | 0            | —           | 0           |
| 1       | 10              | 0            | 0 + 10      | 10          |
| 2       | 20              | 10           | 10 + 20     | 30          |
| 3       | 30              | 30           | 30 + 30     | 60          |
| 4       | 40              | 60           | 60 + 40     | 100         |
| 5       | 50              | 100          | 100 + 50    | 150         |

### Final Answer

```text
150
```

---

# 🔁 Visual Representation

The complete process can be represented as:

```text
Array
  ↓
10 20 30 40 50
  ↓
Initialize total = 0
  ↓
Add 10 → total = 10
  ↓
Add 20 → total = 30
  ↓
Add 30 → total = 60
  ↓
Add 40 → total = 100
  ↓
Add 50 → total = 150
  ↓
Print total
  ↓
150
```

---

# 🚫 Why Not Use `sum()`?

Python provides a built-in function:

```python
print(sum(arr))
```

This is a perfectly valid Python solution.

However, for **DSA preparation and coding assessments**, implementing the accumulation manually is better practice.

The goal is to understand the **running sum / accumulation pattern**, which can be reused in many other problems.

For example:

* Calculate array sum
* Calculate array average
* Find prefix sums
* Find subarray sums
* Calculate cumulative totals
* Find maximum subarray sum
* Calculate sums based on conditions

Therefore, instead of directly using:

```python
sum(arr)
```

we practice:

```python
total = 0

for num in arr:
    total += num
```

---

# 🚫 Why Not Use Nested Loops?

A nested-loop approach is unnecessary for calculating a simple array sum.

For example, repeatedly processing the array using nested loops could result in:

```text
O(N²)
```

time complexity.

A single traversal is sufficient.

Therefore, the optimal approach is:

```text
O(N)
```

time complexity.

---

# ⏱️ Complexity Analysis

## Time Complexity

```text
O(N)
```

We traverse the array exactly once.

If there are `N` elements, each element is processed once.

Therefore:

```text
Time Complexity = O(N)
```

---

## Space Complexity

```text
O(1)
```

The algorithm uses only one additional variable:

```text
total
```

Therefore, the **auxiliary space complexity** is:

```text
O(1)
```

> **Note:** The input array itself requires `O(N)` memory. `O(1)` refers to the additional/auxiliary space used by the summation algorithm.

---

# 🧪 Test Cases

## Test Case 1 — Normal Case

### Input

```text
5
10 20 30 40 50
```

### Output

```text
150
```

---

## Test Case 2 — Positive and Negative Numbers

### Input

```text
6
10 -5 20 -10 15 -5
```

### Output

```text
25
```

---

## Test Case 3 — All Elements Are Zero

### Input

```text
5
0 0 0 0 0
```

### Output

```text
0
```

---

## Test Case 4 — All Elements Are Negative

### Input

```text
5
-10 -20 -30 -40 -50
```

### Output

```text
-150
```

---

## Test Case 5 — Single Element

### Input

```text
1
25
```

### Output

```text
25
```

---

## Test Case 6 — Duplicate Elements

### Input

```text
6
10 10 20 20 30 30
```

### Output

```text
120
```

---

# ⚠️ Important Edge Cases

## 1. Single Element

For:

```text
1
25
```

the sum is simply:

```text
25
```

---

## 2. All Elements Are Zero

For:

```text
5
0 0 0 0 0
```

the result is:

```text
0
```

---

## 3. Negative Numbers

The algorithm works correctly with negative numbers.

For:

```text
-10 -20 -30
```

the calculation is:

```text
0 + (-10) = -10
-10 + (-20) = -30
-30 + (-30) = -60
```

Therefore:

```text
-60
```

---

## 4. Mixed Positive and Negative Numbers

For:

```text
10 -5 20 -10 15 -5
```

the running total is:

```text
10
5
25
15
30
25
```

Therefore:

```text
25
```

---

# 🎯 Key DSA Pattern

This problem teaches the:

## **Linear Traversal / Running Sum Pattern**

The general idea is:

```text
Initialize total
      ↓
Traverse the array
      ↓
Add current element
      ↓
Update total
      ↓
Process next element
      ↓
Print final total
```

The key operation is:

```python
total += num
```

This pattern is one of the most fundamental techniques in array problems.

---

# 📚 What You Learn From This Problem

By solving this problem, you practice:

* Array input handling
* Python lists
* `input()`
* `.split()`
* `map()`
* Integer conversion
* `for` loops
* Running sum
* Accumulation
* Array traversal
* Handling positive numbers
* Handling negative numbers
* Handling zero values
* Time complexity analysis
* Space complexity analysis

---

# 🚀 TCS NQT Relevance

This is a **basic-level array problem** that helps build the foundation required for coding assessments such as **TCS NQT**.

Although calculating a sum is simple, the underlying **accumulation pattern** appears in many more advanced problems.

### Problems Based on Similar Concepts

* Calculate average of array elements
* Find sum of even elements
* Find sum of odd elements
* Find sum of positive elements
* Find sum of negative elements
* Find prefix sum
* Find cumulative sum
* Find maximum subarray sum
* Find sum of elements at even indices
* Find sum of elements at odd indices

### Recommended Thought Process During an Exam

When you see a problem asking for a sum:

```text
1. What values need to be added?
        ↓
2. Can I solve it with one traversal?
        ↓
3. What should the initial total be?
        ↓
4. What condition determines whether an element is added?
        ↓
5. Can I maintain a running sum?
        ↓
6. What is the final complexity?
```

For this problem:

```text
Initial Total → 0
Traversal     → O(N)
Update        → total += num
Answer        → total
```

---

# 📌 Summary

| Property              | Value                              |
| --------------------- | ---------------------------------- |
| Problem               | Calculate Sum of Array Elements    |
| Technique             | Linear Traversal                   |
| Pattern               | Running Sum / Accumulation         |
| Time Complexity       | `O(N)`                             |
| Auxiliary Space       | `O(1)`                             |
| Built-in `sum()` Used | ❌ No                               |
| Nested Loop Used      | ❌ No                               |
| Negative Values       | ✅ Handled                          |
| Zero Values           | ✅ Handled                          |
| Difficulty            | Easy                               |
| Language              | Python                             |
| Suitable For          | DSA / Coding Assessments / TCS NQT |

---

## ⭐ Key Takeaway

> **Initialize a running total with `0`, traverse every element of the array, add each element to the total, and print the final value.**

The key pattern to remember is:

```text
total = 0
     ↓
Read element
     ↓
total += element
     ↓
Read next element
     ↓
Repeat until the array ends
     ↓
Print total
```

This **running sum / accumulation pattern** is one of the most important foundations for solving array traversal and prefix-sum problems.

# 8.🔄 Left Rotate an Array by K Positions

A fundamental **array manipulation and reversal algorithm problem** commonly useful for coding assessments such as **TCS NQT**.

The objective is to rotate the elements of a given array by `K` positions.

This problem can be solved efficiently using the **reversal algorithm**, which performs the rotation in:

- **O(N) time**
- **O(1) auxiliary space**

The reversal algorithm is an important **in-place array manipulation technique** used in DSA and coding interviews.

---

## 📌 Problem Statement

Given an array of `N` integers and an integer `K`, rotate the array to the **left by `K` positions**.

### Input Format

- The first line contains an integer `N`, representing the number of elements.
- The second line contains `N` space-separated integers representing the array.
- The third line contains an integer `K`, representing the number of positions by which the array should be rotated.

### Output Format

Print the array after rotating it to the left by `K` positions.

---

# 🧪 Example

### Input

```text
5
1 2 3 4 5
2
```

### Output

```text
3 4 5 1 2
```

### Explanation

The given array is:

```text
1 2 3 4 5
```

We need to perform a left rotation by `2` positions.

After the first rotation:

```text
2 3 4 5 1
```

After the second rotation:

```text
3 4 5 1 2
```

Therefore, the final rotated array is:

```text
3 4 5 1 2
```

---

# 💡 Approach

We can solve this problem using the **Reversal Algorithm**.

Instead of shifting each element one position at a time, we reverse different sections of the array.

For a left rotation by `K` positions:

### Step 1: Reverse the First `K` Elements

For:

```text
1 2 3 4 5
```

and:

```text
K = 2
```

reverse the first `2` elements:

```text
2 1 3 4 5
```

### Step 2: Reverse the Remaining Elements

Reverse the remaining elements:

```text
2 1 5 4 3
```

### Step 3: Reverse the Entire Array

Reverse the complete array:

```text
3 4 5 1 2
```

The final result is the required left rotation.

---

# 🧠 Algorithm

1. Read the number of elements `N`.
2. Read the array.
3. Read the rotation value `K`.
4. Calculate `K = K % N`.
5. Reverse the first `K` elements.
6. Reverse the remaining `N - K` elements.
7. Reverse the complete array.
8. Print the rotated array.

---

# 💻 Python Code

```python
n = int(input())

arr = list(map(int, input().split()))

k = int(input())


def reverse_section(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


k = k % n

reverse_section(arr, 0, k - 1)

reverse_section(arr, k, n - 1)

reverse_section(arr, 0, n - 1)

print(*arr)
```

---

# 🔍 Code Explanation

## 1. Read the Size of the Array

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

For example:

```text
5
```

becomes:

```python
n = 5
```

---

## 2. Read the Array

```python
arr = list(map(int, input().split()))
```

This line performs three operations.

### `input()`

Reads:

```text
1 2 3 4 5
```

### `.split()`

Splits the input:

```python
["1", "2", "3", "4", "5"]
```

### `map(int, ...)`

Converts the values into integers:

```python
[1, 2, 3, 4, 5]
```

Finally:

```python
arr = [1, 2, 3, 4, 5]
```

---

## 3. Read the Rotation Value

```python
k = int(input())
```

For example:

```text
2
```

becomes:

```python
k = 2
```

This means the array must be rotated two positions to the left.

---

# 🔁 Reversal Algorithm

## 4. Create the Reverse Function

```python
def reverse_section(arr, start, end):
```

This function reverses a specific section of the array.

For example:

```text
1 2 3 4 5
```

If:

```text
start = 0
end = 1
```

the function reverses:

```text
1 2
```

and produces:

```text
2 1
```

---

## 5. Use Two Pointers

Inside the function:

```python
while start < end:
```

Two pointers are used:

```text
start → points to the beginning
end   → points to the end
```

The elements at these positions are swapped:

```python
arr[start], arr[end] = arr[end], arr[start]
```

Then both pointers move toward the center:

```python
start += 1
end -= 1
```

This continues until:

```text
start >= end
```

---

# 📐 Why Use `K % N`?

## 6. Handle Large Values of `K`

```python
k = k % n
```

This is important for hidden test cases.

Suppose:

```text
N = 5
K = 7
```

Rotating an array by `5` positions brings it back to its original state.

Therefore:

```text
7 % 5 = 2
```

So rotating by `7` positions is equivalent to rotating by `2` positions.

For example:

```text
K = 12
N = 5
```

Then:

```text
12 % 5 = 2
```

Therefore, we only need to perform a rotation of `2` positions.

> **Important:** `K % N` requires `N > 0`. If a problem permits an empty array, handle that case separately.

---

# 🔄 Step 1 — Reverse the First K Elements

```python
reverse_section(arr, 0, k - 1)
```

For:

```text
Array = 1 2 3 4 5
K = 2
```

we reverse:

```text
1 2
```

Result:

```text
2 1 3 4 5
```

---

# 🔄 Step 2 — Reverse the Remaining Elements

```python
reverse_section(arr, k, n - 1)
```

The remaining section is:

```text
3 4 5
```

Reverse it:

```text
5 4 3
```

The complete array becomes:

```text
2 1 5 4 3
```

---

# 🔄 Step 3 — Reverse the Entire Array

```python
reverse_section(arr, 0, n - 1)
```

Reverse:

```text
2 1 5 4 3
```

The result is:

```text
3 4 5 1 2
```

This is the required left rotation.

---

# 📊 Dry Run

Consider:

```text
N = 5
Array = [1, 2, 3, 4, 5]
K = 2
```

### Initial Array

```text
1 2 3 4 5
```

### Step 1 — Reverse First K Elements

```text
2 1 3 4 5
```

### Step 2 — Reverse Remaining Elements

```text
2 1 5 4 3
```

### Step 3 — Reverse Entire Array

```text
3 4 5 1 2
```

### Final Answer

```text
3 4 5 1 2
```

---

# 🔁 Visual Representation

The complete process can be represented as:

```text
Original Array
      ↓
1 2 3 4 5
      ↓
K = 2
      ↓
Reverse first K elements
      ↓
2 1 3 4 5
      ↓
Reverse remaining elements
      ↓
2 1 5 4 3
      ↓
Reverse entire array
      ↓
3 4 5 1 2
      ↓
Final Answer
```

---

# 💡 Why Does the Reversal Algorithm Work?

Suppose the array is divided into two parts:

```text
A B
```

where:

```text
A = first K elements
B = remaining elements
```

For example:

```text
A = [1 2]
B = [3 4 5]
```

The required left rotation is:

```text
B A
```

which is:

```text
3 4 5 1 2
```

The reversal algorithm performs:

```text
A B
```

First reverse `A`:

```text
Aᵣ B
```

Then reverse `B`:

```text
Aᵣ Bᵣ
```

Finally reverse the complete array:

```text
(Bᵣ)ᵣ (Aᵣ)ᵣ
```

which becomes:

```text
B A
```

Therefore, the required rotation is obtained.

---

# 🚫 Why Not Shift Elements One by One?

A simple approach would be to move each element one position at a time.

For example:

```text
1 2 3 4 5
```

Rotate once:

```text
2 3 4 5 1
```

Rotate again:

```text
3 4 5 1 2
```

If `K` is large, repeatedly shifting elements can result in:

```text
O(N × K)
```

time complexity.

The reversal algorithm performs the entire rotation in:

```text
O(N)
```

time.

Therefore, it is more efficient.

---

# 🚫 Why Not Use Python Slicing?

A shorter Python solution is:

```python
k = k % n
arr = arr[k:] + arr[:k]
```

This produces the correct result.

However, slicing creates additional lists and therefore uses extra memory.

The reversal algorithm performs the rotation **in-place**.

### Comparison

| Approach | Time Complexity | Auxiliary Space |
|----------|------------------|-----------------|
| Repeated shifting | `O(N × K)` | `O(1)` |
| Python slicing | `O(N)` | `O(N)` |
| **Reversal Algorithm** | **`O(N)`** | **`O(1)`** |

For DSA preparation, the **reversal algorithm is preferred** because it teaches an important in-place array manipulation technique.

---

# ⏱️ Complexity Analysis

## Time Complexity

```text
O(N)
```

We reverse three sections of the array:

```text
First K elements       → O(K)
Remaining N-K elements → O(N-K)
Entire array            → O(N)
```

Therefore:

```text
O(K) + O(N-K) + O(N)
```

which simplifies to:

```text
O(N)
```

So:

```text
Time Complexity = O(N)
```

---

## Space Complexity

```text
O(1)
```

The array is modified **in-place**.

The algorithm only uses a few variables:

```text
start
end
k
```

No additional array proportional to `N` is created.

Therefore:

```text
Auxiliary Space = O(1)
```

---

# 🧪 Test Cases

## Test Case 1 — Normal Case

### Input

```text
5
1 2 3 4 5
2
```

### Output

```text
3 4 5 1 2
```

---

## Test Case 2 — Rotate by One Position

### Input

```text
5
1 2 3 4 5
1
```

### Output

```text
2 3 4 5 1
```

---

## Test Case 3 — Rotate by Array Size

### Input

```text
5
1 2 3 4 5
5
```

### Output

```text
1 2 3 4 5
```

Because:

```text
5 % 5 = 0
```

the array remains unchanged.

---

## Test Case 4 — K Greater Than N

### Input

```text
5
1 2 3 4 5
7
```

### Output

```text
3 4 5 1 2
```

Because:

```text
7 % 5 = 2
```

---

## Test Case 5 — Single Element

### Input

```text
1
25
1
```

### Output

```text
25
```

A single-element array remains unchanged.

---

## Test Case 6 — Negative Numbers

### Input

```text
6
-10 -20 -30 -40 -50 -60
2
```

### Output

```text
-30 -40 -50 -60 -10 -20
```

---

# ⚠️ Important Edge Cases

## 1. K = 0

If:

```text
K = 0
```

the array should remain unchanged.

For example:

```text
1 2 3 4 5
```

remains:

```text
1 2 3 4 5
```

---

## 2. K = N

If:

```text
K = N
```

the array returns to its original configuration.

For:

```text
1 2 3 4 5
```

and:

```text
K = 5
```

the output is:

```text
1 2 3 4 5
```

---

## 3. K > N

Always use:

```python
k = k % n
```

For example:

```text
K = 12
N = 5
```

becomes:

```text
12 % 5 = 2
```

---

## 4. Single Element

For:

```text
25
```

there is nothing to rotate.

The result remains:

```text
25
```

---

## 5. Negative Numbers

The reversal algorithm works exactly the same way with negative values.

For example:

```text
-10 -20 -30 -40
```

rotated left by `2` becomes:

```text
-30 -40 -10 -20
```

---

# 🔄 Left Rotation vs Right Rotation

It is important not to confuse **left rotation** and **right rotation**.

## Left Rotation

Example:

```text
1 2 3 4 5
```

Left rotate by `2`:

```text
3 4 5 1 2
```

The first `K` elements move to the end.

---

## Right Rotation

Example:

```text
1 2 3 4 5
```

Right rotate by `2`:

```text
4 5 1 2 3
```

The last `K` elements move to the beginning.

### Quick Memory Trick

```text
LEFT

1 2 | 3 4 5
 ↓
3 4 5 | 1 2
```

```text
RIGHT

1 2 3 | 4 5
        ↓
4 5 | 1 2 3
```

Always check the question carefully before implementing the rotation.

---

# 🎯 Key DSA Pattern

This problem teaches the:

## **Reversal Algorithm / Two-Pointer Pattern**

The general idea is:

```text
Divide the array
      ↓
Reverse first section
      ↓
Reverse second section
      ↓
Reverse entire array
      ↓
Rotated array
```

The key operation is:

```python
arr[start], arr[end] = arr[end], arr[start]
```

This demonstrates **in-place swapping using two pointers**.

---

# 📚 What You Learn From This Problem

By solving this problem, you practice:

- Array input handling
- Python lists
- `input()`
- `.split()`
- `map()`
- Integer conversion
- Array rotation
- Left rotation
- Right rotation concept
- Reversal algorithm
- Two-pointer technique
- In-place array manipulation
- Swapping elements
- Modulo operation
- Handling large `K`
- Time complexity analysis
- Space complexity analysis

---

# 🚀 TCS NQT Relevance

This is an important **array manipulation problem** for coding assessments such as **TCS NQT**.

The problem is valuable because it combines several fundamental DSA concepts:

- Arrays
- Two pointers
- Reversal
- Modulo
- In-place operations
- Time and space optimization

### Problems Based on Similar Concepts

- Rotate array left by K positions
- Rotate array right by K positions
- Reverse an array
- Reverse a section of an array
- Reverse words in a string
- Reverse a linked list
- Move zeros to the end
- Rearrange positive and negative elements
- Rotate a matrix
- Cyclically rotate an array

### Recommended Thought Process During an Exam

When you see an array rotation problem:

```text
1. Is it left rotation or right rotation?
        ↓
2. What is N?
        ↓
3. What is K?
        ↓
4. Can K be greater than N?
        ↓
5. Use K % N
        ↓
6. Can the array be rotated in-place?
        ↓
7. Can the reversal algorithm be used?
        ↓
8. What is the final complexity?
```

For this problem:

```text
Rotation        → Left
Normalization   → K % N
Technique       → Reversal Algorithm
Traversal       → O(N)
Extra Space     → O(1)
```

---

# 📌 Summary

| Property | Value |
|----------|-------|
| Problem | Rotate Array by K Elements |
| Rotation | Left Rotation |
| Technique | Reversal Algorithm |
| Pattern | Two Pointers / In-Place Manipulation |
| Time Complexity | `O(N)` |
| Auxiliary Space | `O(1)` |
| Built-in Rotation Used | ❌ No |
| Slicing Used | ❌ No |
| Modulo Used | ✅ Yes |
| Handles `K > N` | ✅ Yes |
| Negative Values | ✅ Handled |
| Difficulty | Easy–Medium |
| Language | Python |
| Suitable For | DSA / Coding Assessments / TCS NQT |

---

## ⭐ Key Takeaway

> **For left rotation by `K` positions, reverse the first `K` elements, reverse the remaining elements, and finally reverse the entire array.**

The key pattern to remember is:

```text
Original Array
      ↓
1 2 3 4 5
      ↓
K = 2
      ↓
Reverse first K
      ↓
2 1 3 4 5
      ↓
Reverse remaining
      ↓
2 1 5 4 3
      ↓
Reverse entire array
      ↓
3 4 5 1 2
```

The most important concepts are:

```text
K % N
   +
Two Pointers
   +
In-Place Reversal
   =
O(N) Time + O(1) Auxiliary Space
```

This reversal technique is one of the most useful array-manipulation patterns to remember for DSA and coding assessments.


# 9. 📊 Calculate the Average of All Elements in an Array

A fundamental **array traversal and accumulation problem** commonly useful for coding assessments such as **TCS NQT**.

The objective is to calculate the **average of all elements** present in a given array. The array can contain **integers, decimal values, or a mixture of both**.

The problem can be solved efficiently using **linear traversal**, a **running sum**, and the arithmetic mean formula.

---

## 📌 Problem Statement

Given an array of `N` numbers, calculate and print the average of all elements present in the array.

### Input Format

- The first line contains an integer `N`, representing the number of elements.
- The second line contains `N` space-separated numbers representing the array.

### Output Format

Print the average of all elements in the array.

> If the problem specifies a particular number of decimal places, format the answer according to the required output format.

---

# 🧪 Example

### Input

```text
5
3 9.8 2 4.5 10
```

### Output

```text
5.86
```

### Explanation

The given array is:

```text
3 9.8 2 4.5 10
```

First calculate the sum:

```text
3 + 9.8 + 2 + 4.5 + 10 = 29.3
```

Then calculate the average:

```text
Average = Sum / Number of Elements
        = 29.3 / 5
        = 5.86
```

Therefore, the average is:

```text
5.86
```

---

# 💡 Approach

We can solve this problem using **linear traversal** of the array.

The main idea is to maintain a variable called `total` that stores the sum of all elements processed so far. After calculating the total, divide it by `N` to obtain the average.

### Step 1: Initialize the Sum

```python
total = 0.0
```

### Step 2: Traverse the Array

```python
for num in arr:
```

### Step 3: Add Each Element

```python
total += num
```

### Step 4: Calculate the Average

```python
average = total / n
```

### Step 5: Print the Result

```python
print(average)
```

If exactly two decimal places are required:

```python
print(f"{average:.2f}")
```

---

# 🧠 Algorithm

1. Read the number of elements `N`.
2. Read the array.
3. Initialize `total = 0.0`.
4. Traverse every element of the array.
5. Add the current element to `total`.
6. Calculate `average = total / N`.
7. Print the average according to the required output format.

---

# 💻 Python Code

```python
n = int(input())

arr = list(map(float, input().split()))

total = 0.0

for num in arr:
    total += num

average = total / n

print(average)
```

---

# 🔍 Code Explanation

## 1. Read the Size of the Array

```python
n = int(input())
```

`input()` reads the value as a string and `int()` converts it into an integer.

For example:

```text
5
```

becomes:

```python
n = 5
```

---

## 2. Read the Array

```python
arr = list(map(float, input().split()))
```

This performs three operations.

### `input()`

Reads:

```text
3 9.8 2 4.5 10
```

### `.split()`

Creates:

```text
["3", "9.8", "2", "4.5", "10"]
```

### `map(float, ...)`

Converts the values into:

```text
[3.0, 9.8, 2.0, 4.5, 10.0]
```

Using `float()` means the program accepts both integers such as `3` and decimal values such as `9.8`, including mixed input.

---

## 3. Initialize the Running Sum

```python
total = 0.0
```

Initially:

```text
total = 0.0
```

The value is updated as every element is processed.

---

## 4. Traverse the Array

```python
for num in arr:
```

The loop visits every element exactly once.

---

## 5. Add Each Element to the Total

```python
total += num
```

This is shorthand for:

```python
total = total + num
```

For example:

```text
total = 3.0
num = 9.8
```

becomes:

```text
total = 12.8
```

---

## 6. Calculate the Average

```python
average = total / n
```

The formula is:

```text
Average = Sum of Elements / Number of Elements
```

For the example:

```text
total = 29.3
n = 5

average = 29.3 / 5
        = 5.86
```

---

## 7. Print the Average

```python
print(average)
```

If the question requires exactly two decimal places:

```python
print(f"{average:.2f}")
```

Do not add rounding or formatting unless the problem's output specification requires it.

---

# 📊 Dry Run

Consider:

```text
N = 5
Array = [3, 9.8, 2, 4.5, 10]
```

| Step | Current Element | Total Before | Calculation | Total After |
|------|-----------------|--------------|-------------|-------------|
| Initial | — | 0.0 | — | 0.0 |
| 1 | 3.0 | 0.0 | 0.0 + 3.0 | 3.0 |
| 2 | 9.8 | 3.0 | 3.0 + 9.8 | 12.8 |
| 3 | 2.0 | 12.8 | 12.8 + 2.0 | 14.8 |
| 4 | 4.5 | 14.8 | 14.8 + 4.5 | 19.3 |
| 5 | 10.0 | 19.3 | 19.3 + 10.0 | 29.3 |

Then:

```text
Average = 29.3 / 5
        = 5.86
```

### Final Answer

```text
5.86
```

---

# 🔁 Visual Representation

```text
Array
  ↓
3 9.8 2 4.5 10
  ↓
Initialize total = 0.0
  ↓
Add each element
  ↓
Total = 29.3
  ↓
Average = total / N
  ↓
29.3 / 5
  ↓
5.86
```

---

# 🚫 Why Not Use `sum()`?

Python provides:

```python
print(sum(arr) / n)
```

This is valid Python, but for **DSA preparation and coding assessments**, manually implementing the running sum is better practice because it teaches the accumulation pattern.

Instead of:

```python
sum(arr)
```

we practice:

```python
total = 0.0

for num in arr:
    total += num
```

Then:

```python
average = total / n
```

---

# 🚫 Why Not Use Nested Loops?

A nested-loop approach is unnecessary. A single traversal is enough to calculate the total.

A nested-loop approach could lead to:

```text
O(N²)
```

while the optimal approach is:

```text
O(N)
```

---

# ⏱️ Complexity Analysis

## Time Complexity

```text
O(N)
```

Every element is processed exactly once.

## Auxiliary Space Complexity

```text
O(1)
```

Apart from the input array, the calculation uses only a few variables such as `total` and `average`.

> **Note:** The input array itself requires `O(N)` memory. `O(1)` refers to the additional/auxiliary space used by the algorithm.

---

# 🧪 Test Cases

## Test Case 1 — Normal Integer Values

### Input

```text
5
10 20 30 40 50
```

### Output

```text
30.0
```

---

## Test Case 2 — Decimal Values

### Input

```text
5
0.3 1.5 2.7 4.2 1.3
```

### Output

```text
2.0
```

---

## Test Case 3 — Mixed Integers and Decimals

### Input

```text
5
3 9.8 2 4.5 10
```

### Output

```text
5.86
```

---

## Test Case 4 — Negative Numbers

### Input

```text
5
-10 -20 -30 -40 -50
```

### Output

```text
-30.0
```

---

## Test Case 5 — Positive and Negative Values

### Input

```text
6
10 -5 20 -10 15 -5
```

### Output

```text
4.166666666666667
```

If two decimal places are required:

```text
4.17
```

---

## Test Case 6 — All Elements Are Equal

### Input

```text
4
5 5 5 5
```

### Output

```text
5.0
```

---

## Test Case 7 — Single Element

### Input

```text
1
9.8
```

### Output

```text
9.8
```

---

# ⚠️ Important Edge Cases

## 1. Single Element

For:

```text
1
9.8
```

the average is:

```text
9.8
```

## 2. All Elements Are Zero

For:

```text
5
0 0 0 0 0
```

the average is:

```text
0.0
```

## 3. Negative Numbers

For:

```text
-10 -20 -30
```

the sum is `-60` and the average is:

```text
-60 / 3 = -20.0
```

## 4. Mixed Integers and Decimals

This is valid:

```text
3 9.8 2 4.5 10
```

because the program uses:

```python
map(float, ...)
```

## 5. Decimal Output Formatting

If the problem requires exactly two decimal places:

```python
print(f"{average:.2f}")
```

Otherwise, follow the exact output format given in the problem.

---

# 🎯 Key DSA Pattern

This problem teaches the:

## **Linear Traversal / Running Sum + Average Pattern**

```text
Initialize total
      ↓
Traverse the array
      ↓
Add current element
      ↓
Update total
      ↓
Calculate total / N
      ↓
Print average
```

The key operations are:

```python
total += num
```

and:

```python
average = total / n
```

This is a direct extension of the **running sum / accumulation technique**.

---

# 📚 What You Learn From This Problem

By solving this problem, you practice:

- Array input handling
- Python lists
- `input()`
- `.split()`
- `map()`
- `float()` conversion
- Integer and decimal input
- `for` loops
- Running sum
- Accumulation
- Arithmetic mean
- Array traversal
- Floating-point calculations
- Output formatting
- Time complexity analysis
- Space complexity analysis

---

# 🚀 TCS NQT Relevance

This is a **basic-level array problem** that helps build the foundation required for coding assessments such as **TCS NQT**.

Although calculating an average is simple, the underlying **accumulation pattern** appears in many other problems.

### Problems Based on Similar Concepts

- Calculate sum of array elements
- Calculate average of array elements
- Find sum of even elements
- Find sum of odd elements
- Find sum of positive elements
- Find sum of negative elements
- Find prefix sum
- Find cumulative average
- Find maximum and minimum
- Calculate average under a condition
- Calculate average of a subarray

### Recommended Thought Process During an Exam

```text
1. What values need to be included?
        ↓
2. Can I solve it with one traversal?
        ↓
3. What should the initial total be?
        ↓
4. Are the elements integers or decimals?
        ↓
5. What is the number of elements?
        ↓
6. Calculate total / N
        ↓
7. Does the output require decimal formatting?
        ↓
8. What is the final complexity?
```

For this problem:

```text
Input Type     → Integer / Decimal
Initial Total  → 0.0
Traversal      → O(N)
Update         → total += num
Average        → total / N
Answer         → average
```

---

# 📌 Summary

| Property | Value |
|----------|-------|
| Problem | Calculate Average of Array Elements |
| Technique | Linear Traversal |
| Pattern | Running Sum / Accumulation |
| Time Complexity | `O(N)` |
| Auxiliary Space | `O(1)` |
| Built-in `sum()` Used | ❌ No |
| Nested Loop Used | ❌ No |
| Decimal Values | ✅ Supported |
| Negative Values | ✅ Supported |
| Zero Values | ✅ Supported |
| Difficulty | Easy |
| Language | Python |
| Suitable For | DSA / Coding Assessments / TCS NQT |

---

## ⭐ Key Takeaway

> **Traverse the array once, maintain a running sum, and divide the final sum by the number of elements to calculate the average.**

The key pattern is:

```text
total = 0.0
     ↓
Read each element
     ↓
total += element
     ↓
Repeat until the array ends
     ↓
average = total / N
     ↓
Print average
```

For flexible numeric input, remember:

```python
arr = list(map(float, input().split()))
```

This accepts integers, decimals, and mixed values such as:

```text
3 9.8 2 4.5 10
```

The core algorithm remains:

```text
Running Sum + Arithmetic Mean
```

with:

```text
O(N) Time + O(1) Auxiliary Space
```
# 10. 📊 Find the Median of a Given Array

A fundamental **array sorting and statistical calculation problem** commonly useful for coding assessments such as **TCS NQT**.

The objective is to find the **median value** of a given array.

The problem can be solved by first **sorting the array** and then selecting the middle element(s) based on whether the number of elements is odd or even.

---

## 📌 Problem Statement

Given an array of `N` numbers, find and print the **median** of the array.

The array may contain integers, decimal values, or a mixture of both.

### Input Format

- The first line contains an integer `N`, representing the number of elements.
- The second line contains `N` space-separated numbers representing the array.

### Output Format

Print the median of the array.

---

# 🧪 Example

### Input

```text
5
7 2 9 4 1
```

### Output

```text
4.0
```

### Explanation

The given array is:

```text
7 2 9 4 1
```

First, sort the array:

```text
1 2 4 7 9
```

There are `5` elements, which is an **odd number**.

Therefore, the middle element is:

```text
4
```

So the median is:

```text
4.0
```

---

# 💡 Approach

To find the median, we first need to arrange the elements in **ascending order**.

After sorting, there are two cases.

### Case 1: Odd Number of Elements

If `N` is odd, there is exactly one middle element.

For example:

```text
1 2 4 7 9
```

Here:

```text
N = 5
```

The middle element is:

```text
4
```

Its index is:

```python
n // 2
```

Therefore:

```python
median = arr[n // 2]
```

---

### Case 2: Even Number of Elements

If `N` is even, there are two middle elements.

For example:

```text
2 4 6 8 10 12
```

Here:

```text
N = 6
```

The two middle elements are:

```text
6 and 8
```

The median is their average:

```text
(6 + 8) / 2 = 7
```

Therefore:

```python
median = (arr[n // 2 - 1] + arr[n // 2]) / 2
```

---

# 🧠 Algorithm

1. Read the number of elements `N`.
2. Read the array.
3. Sort the array in ascending order.
4. Check whether `N` is odd or even.
5. If `N` is odd:
   - Select the middle element.
6. If `N` is even:
   - Select the two middle elements.
   - Calculate their average.
7. Print the median.

---

# 💻 Python Code

```python
n = int(input())

arr = list(map(float, input().split()))

arr.sort()

if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

print(median)
```

---

# 🔍 Code Explanation

## 1. Read the Size of the Array

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

For example:

```text
5
```

becomes:

```python
n = 5
```

---

## 2. Read the Array

```python
arr = list(map(float, input().split()))
```

This line performs three operations.

### `input()`

Reads the complete line:

```text
7 2 9 4 1
```

### `.split()`

Splits the input into individual strings:

```text
["7", "2", "9", "4", "1"]
```

### `map(float, ...)`

Converts each value into a floating-point number:

```text
[7.0, 2.0, 9.0, 4.0, 1.0]
```

Using `float()` allows the program to handle:

```text
3
```

as well as:

```text
9.8
```

and mixed values such as:

```text
3 9.8 2 4.5 10
```

---

## 3. Sort the Array

```python
arr.sort()
```

This arranges the elements in ascending order.

For example:

```text
7 2 9 4 1
```

becomes:

```text
1.0 2.0 4.0 7.0 9.0
```

Sorting is necessary because the median depends on the **ordered position** of the elements.

---

# 🔢 Odd Number of Elements

## 4. Check if N is Odd

```python
if n % 2 == 1:
```

The `%` operator gives the remainder after division.

For example:

```text
5 % 2 = 1
```

Therefore, `5` is odd.

---

## 5. Find the Middle Element

```python
median = arr[n // 2]
```

For:

```text
N = 5
```

we have:

```text
5 // 2 = 2
```

Python uses zero-based indexing:

```text
Index:    0   1   2   3   4
Array:    1   2   4   7   9
```

Therefore:

```text
arr[2] = 4
```

So the median is:

```text
4.0
```

---

# 🔢 Even Number of Elements

## 6. Handle the Even Case

```python
else:
```

If `N` is even, there are two middle elements.

For example:

```text
2 4 6 8 10 12
```

Here:

```text
N = 6
```

The indices are:

```text
Index:    0  1  2  3   4   5
Array:    2  4  6  8  10  12
```

The two middle elements are:

```text
arr[2] = 6
arr[3] = 8
```

---

## 7. Calculate the Average of the Two Middle Elements

```python
median = (arr[n // 2 - 1] + arr[n // 2]) / 2
```

For:

```text
N = 6
```

we get:

```text
n // 2 = 3
```

Therefore:

```text
arr[3 - 1] = arr[2] = 6
arr[3]     = arr[3] = 8
```

So:

```text
median = (6 + 8) / 2
       = 7.0
```

---

## 8. Print the Median

```python
print(median)
```

After calculating the median, the final result is printed.

---

# 📊 Dry Run — Odd Number of Elements

Consider:

```text
N = 5
Array = [7, 2, 9, 4, 1]
```

### Step 1 — Sort

```text
1 2 4 7 9
```

### Step 2 — Check N

```text
5 % 2 = 1
```

So `N` is odd.

### Step 3 — Find Middle Index

```text
5 // 2 = 2
```

### Step 4 — Select Middle Element

```text
arr[2] = 4
```

### Final Answer

```text
4.0
```

---

# 📊 Dry Run — Even Number of Elements

Consider:

```text
N = 6
Array = [10, 2, 8, 4, 6, 12]
```

### Step 1 — Sort

```text
2 4 6 8 10 12
```

### Step 2 — Check N

```text
6 % 2 = 0
```

So `N` is even.

### Step 3 — Find the Two Middle Elements

```text
n // 2 = 3
```

Therefore:

```text
arr[2] = 6
arr[3] = 8
```

### Step 4 — Calculate the Median

```text
(6 + 8) / 2 = 7
```

### Final Answer

```text
7.0
```

---

# 🔁 Visual Representation

For an odd number of elements:

```text
Original Array
      ↓
7 2 9 4 1
      ↓
Sort
      ↓
1 2 4 7 9
      ↓
Select middle element
      ↓
4
      ↓
Median = 4.0
```

For an even number of elements:

```text
Original Array
      ↓
10 2 8 4 6 12
      ↓
Sort
      ↓
2 4 6 8 10 12
      ↓
Select two middle elements
      ↓
6 and 8
      ↓
(6 + 8) / 2
      ↓
7.0
```

---

# 🚫 Why Can't We Find the Median Without Sorting?

The median depends on the **position of the elements after ordering them**.

For example:

```text
7 2 9 4 1
```

The middle element of the original unsorted array is:

```text
9
```

But that is **not** the median.

After sorting:

```text
1 2 4 7 9
```

the middle element is:

```text
4
```

Therefore, simply selecting the middle element from an unsorted array is incorrect.

For this basic approach, sorting is necessary.

---

# 🚫 Common Mistake — Forgetting the Even Case

A common incorrect solution is:

```python
arr.sort()
median = arr[n // 2]
```

This works for odd `N`, but it is **wrong for even `N`**.

For:

```text
2 4 6 8
```

this code gives:

```text
arr[4 // 2] = arr[2] = 6
```

But the correct median is:

```text
(4 + 6) / 2 = 5
```

Therefore, always handle both cases:

```python
if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2
```

---

# ⏱️ Complexity Analysis

## Time Complexity

The major operation is:

```python
arr.sort()
```

Python sorting takes:

```text
O(N log N)
```

Finding the middle element(s) takes:

```text
O(1)
```

Therefore, the overall time complexity is:

```text
Time Complexity = O(N log N)
```

---

## Space Complexity

The median calculation itself uses only a few variables.

However, Python's built-in sorting algorithm may use additional memory internally.

Therefore, it is better **not to claim the entire program has O(1) auxiliary space**.

The important complexity for this solution is:

```text
Time Complexity = O(N log N)
```

with sorting being the dominant operation.

---

# 🧪 Test Cases

## Test Case 1 — Odd Number of Elements

### Input

```text
5
7 2 9 4 1
```

### Output

```text
4.0
```

---

## Test Case 2 — Even Number of Elements

### Input

```text
6
10 2 8 4 6 12
```

### Output

```text
7.0
```

---

## Test Case 3 — Decimal Values

### Input

```text
5
3.5 1.2 9.8 4.1 2.6
```

### Output

```text
3.5
```

---

## Test Case 4 — Mixed Integers and Decimals

### Input

```text
5
3 9.8 2 4.5 10
```

Sorted:

```text
2.0 3.0 4.5 9.8 10.0
```

### Output

```text
4.5
```

---

## Test Case 5 — Negative Numbers

### Input

```text
5
-10 -20 -30 -40 -50
```

Sorted:

```text
-50 -40 -30 -20 -10
```

### Output

```text
-30.0
```

---

## Test Case 6 — Duplicate Elements

### Input

```text
6
5 5 10 10 15 15
```

Sorted:

```text
5 5 10 10 15 15
```

The middle elements are:

```text
10 and 10
```

### Output

```text
10.0
```

---

## Test Case 7 — Single Element

### Input

```text
1
9.8
```

### Output

```text
9.8
```

---

# ⚠️ Important Edge Cases

## 1. Single Element

For:

```text
1
25
```

the median is:

```text
25.0
```

---

## 2. Two Elements

For:

```text
2
10 20
```

the median is:

```text
(10 + 20) / 2 = 15
```

Output:

```text
15.0
```

---

## 3. Negative Numbers

The algorithm works correctly with negative values.

For:

```text
-10 -20 -30 -40 -50
```

after sorting:

```text
-50 -40 -30 -20 -10
```

The middle element is:

```text
-30
```

---

## 4. Decimal Values

Using:

```python
float
```

allows values such as:

```text
0.3 1.5 2.7 4.2
```

to be processed correctly.

---

## 5. Duplicate Values

Duplicate values do not cause any problem.

For:

```text
5 5 5 10 10
```

the median is:

```text
5.0
```

---

# 🎯 Key DSA Pattern

This problem teaches the:

## **Sorting + Middle Element Pattern**

The general idea is:

```text
Read Array
     ↓
Sort Array
     ↓
Check N
     ↓
 ┌───────────────┐
 │               │
Odd             Even
 │               │
 ↓               ↓
One middle     Two middle
element         elements
 │               │
 ↓               ↓
Median          Average
 │               │
 └───────┬───────┘
         ↓
      Print Answer
```

The two formulas are:

### Odd N

```text
Median = arr[N // 2]
```

### Even N

```text
Median = (arr[N // 2 - 1] + arr[N // 2]) / 2
```

---

# 📚 What You Learn From This Problem

By solving this problem, you practice:

- Array input handling
- Python lists
- `input()`
- `.split()`
- `map()`
- `float()` conversion
- Array sorting
- Zero-based indexing
- Odd/even conditions
- Finding middle elements
- Arithmetic mean
- Handling decimal values
- Handling negative values
- Handling duplicate values
- Time complexity analysis
- Space complexity analysis

---

# 🚀 TCS NQT Relevance

This is a useful **array and sorting problem** for coding assessments such as **TCS NQT**.

Although the basic median calculation is simple, it tests whether you understand:

- Sorting
- Array indexing
- Odd/even cases
- Conditional logic
- Arithmetic operations
- Edge cases
- Complexity analysis

### Problems Based on Similar Concepts

- Find minimum and maximum
- Find second largest element
- Find second smallest element
- Find mode of an array
- Find frequency of elements
- Find kth smallest element
- Find kth largest element
- Find percentile
- Find middle element after sorting
- Find statistics of an array

### Recommended Thought Process During an Exam

When you see a problem asking for a median:

```text
1. Does the median require the array to be ordered?
        ↓
2. Sort the array
        ↓
3. Is N odd or even?
        ↓
4. If odd, select one middle element
        ↓
5. If even, select two middle elements
        ↓
6. Calculate their average
        ↓
7. Check the required output format
        ↓
8. Analyze the complexity
```

For this problem:

```text
Sorting       → O(N log N)
Odd N         → arr[N // 2]
Even N        → Average of two middle elements
Final Search  → O(1)
Overall       → O(N log N)
```

---

# 📌 Summary

| Property | Value |
|----------|-------|
| Problem | Find Median of an Array |
| Technique | Sorting + Middle Element |
| Pattern | Odd/Even Middle Element |
| Time Complexity | `O(N log N)` |
| Median for Odd N | One middle element |
| Median for Even N | Average of two middle elements |
| Decimal Values | ✅ Supported |
| Negative Values | ✅ Supported |
| Duplicate Values | ✅ Supported |
| Built-in `median()` Used | ❌ No |
| Difficulty | Easy–Medium |
| Language | Python |
| Suitable For | DSA / Coding Assessments / TCS NQT |

---

## ⭐ Key Takeaway

> **Sort the array first. If the number of elements is odd, the median is the middle element. If the number of elements is even, the median is the average of the two middle elements.**

Remember:

```text
Sort
  ↓
Check N % 2
  ↓
Odd → One middle element
  ↓
Even → Average of two middle elements
  ↓
Print Median
```

The most important formulas are:

```text
Odd:
Median = arr[N // 2]
```

```text
Even:
Median = (arr[N // 2 - 1] + arr[N // 2]) / 2
```

The core technique is:

```text
Sorting + Correct Indexing + Odd/Even Handling
```

with an overall time complexity of:

```text
O(N log N)
```
