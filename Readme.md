# 🧑‍💻 TCS NQT vs LeetCode — Python Input Handling Guide

When solving coding problems, one of the most important things to understand is **who is responsible for handling the input and output**.

The same algorithm can require different Python code depending on whether the platform expects:

* A **complete program**
* A **function-based solution**
* A **predefined class/method**

This guide explains the difference between **TCS NQT-style coding** and **LeetCode-style coding**.

---

# 📌 Why Input Handling Matters

Consider a simple problem:

> Given an array of integers, calculate the sum of all elements.

The algorithm is:

```python
total = 0

for num in arr:
    total += num
```

However, the way we obtain `arr` and produce the answer depends on the coding platform.

---

# 🟢 1. Complete Program Format

In a complete-program coding question, the problem provides an **Input Format** and **Output Format**.

For example:

```text
Input:
5
10 20 30 40 50

Output:
150
```

Here, your program is responsible for reading the input and printing the output.

### Python Code

```python
n = int(input())

arr = list(map(int, input().split()))

total = 0

for num in arr:
    total += num

print(total)
```

### Explanation

The first line:

```python
n = int(input())
```

reads the number of elements.

The second line:

```python
arr = list(map(int, input().split()))
```

reads the array.

Then:

```python
total = 0

for num in arr:
    total += num
```

calculates the sum.

Finally:

```python
print(total)
```

prints the answer.

---

# 🚀 2. TCS NQT-Style Coding

For a **TCS NQT programming question**, always follow the exact **Input Format** and **Output Format** given by that particular problem.

If the question expects a complete program and provides:

```text
N
Array Elements
```

then you can use:

```python
n = int(input())

arr = list(map(int, input().split()))

total = 0

for num in arr:
    total += num

print(total)
```

### Example

**Input:**

```text
5
10 20 30 40 50
```

**Output:**

```text
150
```

---

# ⚠️ Important TCS NQT Rule

Do **not** assume that every TCS NQT problem has exactly the same input format.

The problem may instead provide different formats.

## Format A — `N` Followed by Array

```text
5
10 20 30 40 50
```

Use:

```python
n = int(input())
arr = list(map(int, input().split()))
```

---

## Format B — Array Only

```text
10 20 30 40 50
```

If the problem does not provide `N`, don't try to read it.

Use:

```python
arr = list(map(int, input().split()))
```

---

## Format C — Multiple Test Cases

If the problem provides the number of test cases:

```text
3
5
1 2 3 4 5
4
10 20 30 40
3
7 8 9
```

then the program needs to process each test case.

Example:

```python
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    # Solve the problem here
```

> **Important:** The exact structure of each test case must still be taken from the problem's Input Format. Don't assume every multi-test-case problem uses exactly these two lines.

---

# 🔵 3. LeetCode-Style Format

LeetCode works differently.

Instead of writing a complete program, the platform usually provides a **function or class**.

For example:

```python
class Solution:
    def arraySum(self, arr):
```

You should **not** write:

```python
n = int(input())
arr = list(map(int, input().split()))
```

because LeetCode already provides the input through the function parameter.

### Correct LeetCode Solution

```python
class Solution:
    def arraySum(self, arr):

        total = 0

        for num in arr:
            total += num

        return total
```

Here:

```python
arr
```

is already provided by the platform.

You only need to implement the algorithm.

---

# 🔄 `print()` vs `return`

This is one of the most important differences.

## Complete Program

Use:

```python
print(total)
```

because your program is responsible for producing the output.

---

## Function-Based Platform

Use:

```python
return total
```

because the platform's driver code generally handles the result.

For example:

```python
def solve(arr):
    total = 0

    for num in arr:
        total += num

    return total
```

> The exact requirement depends on the platform. Follow the function's specified return contract.

---

# 🟡 4. Function-Based Questions

Some platforms provide something like:

```python
def solve(arr):
    # write your code here
```

In this case, don't create another input system.

Use the provided parameter:

```python
def solve(arr):

    total = 0

    for num in arr:
        total += num

    return total
```

The important rule is:

> **Do not change the provided function signature unless the platform explicitly allows it.**

---

# 🧠 Complete Program vs Function-Based Solution

The same algorithm can look different depending on the platform.

## Complete Program

```python
n = int(input())

arr = list(map(int, input().split()))

total = 0

for num in arr:
    total += num

print(total)
```

---

## Function-Based

```python
def solve(arr):

    total = 0

    for num in arr:
        total += num

    return total
```

---

## LeetCode Class-Based

```python
class Solution:

    def arraySum(self, arr):

        total = 0

        for num in arr:
            total += num

        return total
```

The **algorithm is the same**.

Only the **input/output interface** changes.

---

# 📊 Quick Comparison

| Feature                     | Complete Program                       | LeetCode / Function-Based     |
| --------------------------- | -------------------------------------- | ----------------------------- |
| Input handling              | You handle it                          | Platform handles it           |
| `input()`                   | Usually required                       | Usually not required          |
| `print()`                   | Usually required                       | Usually not required          |
| `return`                    | Usually not the final output mechanism | Usually required              |
| Function provided           | Not necessarily                        | Usually                       |
| Class provided              | Usually no                             | Sometimes                     |
| Follow problem's I/O format | ✅ Yes                                  | Function signature is primary |

---

# 💻 VS Code Practice

When practicing a TCS NQT-style problem in VS Code, you can create:

```text
solution.py
```

For example:

```python
n = int(input())

arr = list(map(int, input().split()))

total = 0

for num in arr:
    total += num

print(total)
```

Run it using:

```bash
python solution.py
```

Then enter custom input:

```text
5
10 20 30 40 50
```

Output:

```text
150
```

---

# 🧪 Testing With Custom Input

## Test Case 1

**Input:**

```text
5
10 20 30 40 50
```

**Output:**

```text
150
```

---

## Test Case 2

**Input:**

```text
6
10 -5 20 -10 15 -5
```

**Output:**

```text
25
```

---

## Test Case 3

**Input:**

```text
5
0 0 0 0 0
```

**Output:**

```text
0
```

---

# ⚠️ Common Mistakes

## ❌ Mistake 1 — Using `input()` in LeetCode

Incorrect:

```python
class Solution:
    def arraySum(self, arr):

        n = int(input())
        arr = list(map(int, input().split()))

        return sum(arr)
```

The function already receives `arr`.

Correct:

```python
class Solution:
    def arraySum(self, arr):

        total = 0

        for num in arr:
            total += num

        return total
```

---

## ❌ Mistake 2 — Using `return` Instead of `print()` in a Complete Program

If the question expects a complete program:

```python
n = int(input())
arr = list(map(int, input().split()))

total = 0

for num in arr:
    total += num

return total
```

This is incorrect because `return` cannot be used outside a function.

Use:

```python
print(total)
```

---

## ❌ Mistake 3 — Assuming Every TCS Question Has `N`

Don't automatically write:

```python
n = int(input())
```

Read the problem statement first.

If the input is only:

```text
10 20 30 40 50
```

then:

```python
arr = list(map(int, input().split()))
```

is sufficient.

---

## ❌ Mistake 4 — Changing the Provided Function Signature

If the platform gives:

```python
def solve(arr):
```

don't change it to:

```python
def solve():
```

unless the platform explicitly requires that change.

The judge may call the original function signature automatically.

---

# 🎯 Exam Strategy

When you open a coding question, **don't immediately start writing code**.

First identify:

```text
1. What is the Input Format?
        ↓
2. What is the Output Format?
        ↓
3. Is a function already provided?
        ↓
4. Is a class already provided?
        ↓
5. Who handles input?
        ↓
6. Who handles output?
        ↓
7. Then write the algorithm
```

This prevents one of the most common competitive-programming mistakes: writing correct logic with the wrong input/output interface.

---

# 🔥 The Rule to Remember

## Complete Program

```text
Input → Your Code → Output
```

Therefore:

```text
input()
   ↓
algorithm
   ↓
print()
```

---

## Function-Based Platform

```text
Platform Input
      ↓
Function Parameter
      ↓
Your Algorithm
      ↓
return
      ↓
Platform Output
```

Therefore:

```python
def solve(arr):
    # algorithm
    return answer
```

---

# 🧩 Example — Same Problem, Different Platforms

### Problem

> Calculate the sum of all elements in an array.

## TCS / Complete Program

```python
n = int(input())
arr = list(map(int, input().split()))

total = 0

for num in arr:
    total += num

print(total)
```

---

## LeetCode / Function-Based

```python
class Solution:
    def arraySum(self, arr):

        total = 0

        for num in arr:
            total += num

        return total
```

---

## Function Format

```python
def solve(arr):

    total = 0

    for num in arr:
        total += num

    return total
```

The algorithm remains:

```text
Initialize total = 0
        ↓
Traverse array
        ↓
Add each element
        ↓
Return / print result
```

Only the **interface** changes.

---

# 📚 What You Learn From This Guide

By understanding input handling, you learn:

* How competitive programming platforms handle input
* How to read TCS-style input
* How to handle custom input in VS Code
* How LeetCode function parameters work
* The difference between `print()` and `return`
* How to identify the input format
* How to handle multiple test cases
* How to avoid unnecessary input code
* How to preserve provided function signatures
* How to adapt the same algorithm to different platforms

---

# 🚀 TCS NQT Preparation Rule

For every TCS NQT coding problem:

> **Read the Input Format and Output Format before writing your code.**

Don't assume that every problem uses:

```python
n = int(input())
arr = list(map(int, input().split()))
```

Use that template **only when the problem actually provides `N` followed by the array**.

Similarly, don't assume that every coding platform requires `input()`.

If the platform gives you:

```python
def solve(arr):
```

or:

```python
class Solution:
```

then the platform is generally responsible for providing the input to your function.

---

# 📌 Summary

| Situation                     | Correct Approach                                 |
| ----------------------------- | ------------------------------------------------ |
| VS Code + TCS-style problem   | `input()` + `print()`                            |
| TCS complete-program question | Follow given Input/Output Format                 |
| LeetCode function             | Use provided parameters + `return`               |
| Function-based platform       | Don't manually read input                        |
| Multiple test cases           | Read `T` and loop according to the stated format |
| `N` not provided              | Don't read `N`                                   |
| Function signature provided   | Preserve it                                      |

---

## ⭐ Key Takeaway

> **Don't memorize one input template. Understand who is responsible for input and output.**

### Complete Program

```python
n = int(input())
arr = list(map(int, input().split()))

# Algorithm

print(answer)
```

### Function-Based

```python
def solve(arr):

    # Algorithm

    return answer
```

### LeetCode

```python
class Solution:
    def problemName(self, arr):

        # Algorithm

        return answer
```

The **algorithm doesn't change**.

The **input/output interface changes according to the platform**.
