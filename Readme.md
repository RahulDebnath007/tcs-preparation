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

# 2.🔢 Find the Largest Element in an Array

A simple and fundamental **array traversal problem** commonly used in coding assessments such as **TCS NQT**.

The objective is to find the **maximum/largest element** present in a given array **without using Python's built-in** **`max()`** **function**.

---

## 📌 Problem Statement

Given an array of `N` integers, find and print the **largest element** in the array.

### Input Format

- The first line contains an integer `N`, representing the number of elements.
- The second line contains `N` space-separated integers representing the array.

### Output Format

Print the largest element present in the array.

---

## 🧪 Example

### Input

```text
5
8 3 12 1 6
Output
12
Explanation

The given array is:

8 3 12 1 6

We compare each element with the current largest value:

8 → largest = 8
3 → no change
12 → largest = 12
1 → no change
6 → no change

Therefore, the largest element is:

12
💡 Approach

We can solve this problem using linear traversal of the array.

Step 1: Initialize the Maximum

Assume that the first element of the array is the largest:

largest = arr[0]
Step 2: Traverse the Remaining Elements

Start from the second element and compare every element with largest.

for i in range(1, n):
Step 3: Update the Maximum

If the current element is greater than largest, update the value:

if arr[i] > largest:
    largest = arr[i]
Step 4: Print the Result

After checking all elements:

print(largest)

The final value stored in largest is the maximum element of the array.

🧠 Algorithm
Read the number of elements N.
Read the array.
Set largest = arr[0].
Traverse the array from index 1 to N - 1.
For every element:
Compare the current element with largest.
If it is greater, update largest.
Print largest.
💻 Python Code
n = int(input())

arr = list(map(int, input().split()))

largest = arr[0]

for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

print(largest)
🔍 Code Explanation
1. Read the Size of the Array
n = int(input())

input() reads the value as a string.

int() converts it into an integer.

For example:

5

becomes:

n = 5
2. Read the Array
arr = list(map(int, input().split()))

This line performs three operations.

input()

Reads the complete line:

8 3 12 1 6
.split()

Splits the input into individual strings:

["8", "3", "12", "1", "6"]
map(int, ...)

Converts each string into an integer:

[8, 3, 12, 1, 6]

Finally, list() creates the Python list.

So:

arr = [8, 3, 12, 1, 6]
3. Assume the First Element Is the Largest
largest = arr[0]

Initially:

largest = 8

We don't initialize largest with 0 or another fixed value because the array may contain negative numbers.

For example:

-10 -5 -20

The correct largest value is:

-5

If we initialized largest = 0, the answer would incorrectly remain 0.

Therefore, using:

largest = arr[0]

is the correct approach.

4. Traverse the Array
for i in range(1, n):

The loop starts from index 1 because the element at index 0 has already been stored in largest.

For:

arr = [8, 3, 12, 1, 6]

the loop checks:

3
12
1
6
5. Compare the Current Element
if arr[i] > largest:

If the current element is greater than the current maximum, we update it.

For example:

largest = 8
current = 12

Since:

12 > 8

we update:

largest = 12
6. Update the Maximum
largest = arr[i]

This stores the newly discovered largest value.

7. Print the Answer
print(largest)

After the complete traversal, largest contains the maximum element.

📊 Dry Run

Consider:

N = 5
Array = [8, 3, 12, 1, 6]
Step	Current Element	Largest Before	Comparison	Largest After
Initial	8	—	—	8
1	3	8	3 > 8 ❌	8
2	12	8	12 > 8 ✅	12
3	1	12	1 > 12 ❌	12
4	6	12	6 > 12 ❌	12
Final Answer
12
⏱️ Complexity Analysis
Time Complexity
O(N)

We traverse the array once.

If there are N elements, each element is checked at most once.

Therefore:

Time Complexity = O(N)
Space Complexity
O(1)

Apart from the input array, the algorithm only uses one additional variable:

largest

Therefore, the auxiliary space complexity is:

O(1)

Note: The input array itself requires O(N) memory. O(1) refers to the extra/auxiliary space used by the algorithm.

🧪 Test Cases
Test Case 1 — Normal Case
Input
5
8 3 12 1 6
Output
12
Test Case 2 — Negative Numbers
Input
5
-4 -10 -3 -2 -7
Output
-2
Test Case 3 — All Elements Are Equal
Input
4
5 5 5 5
Output
5
Test Case 4 — Largest Element at the Beginning
Input
5
20 8 12 6 9
Output
20
Test Case 5 — Largest Element at the End
Input
5
8 12 6 9 25
Output
25
🚫 Why Not Use max()?

Python provides a built-in function:

print(max(arr))

This works and also has O(N) time complexity.

However, for DSA preparation and coding assessments, implementing the traversal manually is better practice.
