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

# 3.🔢 Find the Second Largest and Second Smallest Element in an Array

A fundamental **array traversal problem** commonly useful for coding assessments such as **TCS NQT**.

The objective is to find the **second largest** and **second smallest distinct elements** present in a given array **without using Python's built-in sorting functions**.

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

# 🧪 Example

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

The given array is:

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

So the final answer is:

```text
Second Largest: 15
Second Smallest: 5
```

---

# 💡 Approach

We can solve this problem using **linear traversal** without sorting the array.

Instead of sorting, maintain four variables:

```text
largest
second_largest
smallest
second_smallest
```

While traversing the array, update these values whenever a new larger or smaller element is found.

This allows us to solve the problem in:

```text
O(N)
```

time.

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
5. For finding the largest values:

   * If the current element is greater than `largest`:

     * Move `largest` to `second_largest`.
     * Update `largest`.
   * Otherwise, if the current element is greater than `second_largest` and different from `largest`, update `second_largest`.
6. For finding the smallest values:

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

`input()` reads the value as a string.

`int()` converts it into an integer.

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

This line performs three operations.

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

`float('-inf')` represents negative infinity.

This is useful because the array may contain negative numbers.

For example:

```text
-10 -5 -20 -3
```

If we initialized:

```python
largest = 0
```

the algorithm would fail because all values are smaller than `0`.

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

the values of `num` will be:

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

This is an important part of the algorithm.

---

## 7. Update the Second Largest

```python
elif num > second_largest and num != largest:
    second_largest = num
```

This condition checks whether the current element should become the second largest.

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

`float('inf')` represents positive infinity.

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

Consider this array:

```text
10 10 8 5
```

If duplicate values were allowed to become the second largest:

```text
Largest = 10
Second Largest = 10
```

But we usually interpret **second largest** as the second **distinct** largest value.

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

ensures that duplicate values are not counted twice.

---

# 🚫 Why Not Sort the Array?

A simple approach would be:

```python
arr.sort()
```

Then we could find the second smallest and second largest.

However, sorting takes:

```text
O(N log N)
```

time.

Our approach only requires:

```text
O(N)
```

time.

Therefore, the linear traversal approach is more efficient.

### Comparison

| Approach         | Time Complexity | Extra Space                       |
| ---------------- | --------------- | --------------------------------- |
| Sorting          | `O(N log N)`    | Depends on sorting implementation |
| Linear Traversal | `O(N)`          | `O(1)`                            |

For coding interviews and TCS NQT-style problems, the **single-pass approach** is preferable.

---

# ⏱️ Complexity Analysis

## Time Complexity

```text
O(N)
```

The array is traversed exactly once.

Each element is processed using a constant number of comparisons.

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

A production-ready solution should handle this case explicitly.

For TCS NQT, always read the problem statement carefully to determine what output is expected when no second distinct value exists.

---

# 🎯 Key DSA Pattern

This problem teaches the:

## **Single Traversal / Running Maximum and Minimum Pattern**

Instead of sorting the array, we maintain the best candidates while traversing.

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

This problem is more important than simply finding the largest or smallest element because it requires maintaining **multiple values simultaneously**.

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

Smallest         → smallest
Second Smallest  → second_smallest

Traversal        → O(N)
Auxiliary Space  → O(1)
```

---

# 📌 Summary

| Property         | Value                              |
| ---------------- | ---------------------------------- |
| Problem          | Second Largest & Second Smallest   |
| Technique        | Linear Traversal                   |
| Pattern          | Running Maximum & Minimum          |
| Time Complexity  | `O(N)`                             |
| Auxiliary Space  | `O(1)`                             |
| Sorting Used     | ❌ No                               |
| Duplicate Values | Handled                            |
| Distinct Values  | ✅ Yes                              |
| Difficulty       | Easy–Medium                        |
| Language         | Python                             |
| Suitable For     | DSA / Coding Assessments / TCS NQT |

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
