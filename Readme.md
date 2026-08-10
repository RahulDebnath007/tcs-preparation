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
