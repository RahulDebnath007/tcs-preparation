# 🔥 11. Fraud Transactions

**Fraud Transaction Detection** is a high-priority TCS NQT-style pattern because it often appears as a **real-world/business story**, while the actual coding problem is usually based on a simple data-structure pattern.

The important skill is:

> **Ignore the story and identify the underlying operation.**

A representative version is:

> Given transaction amounts, identify the transaction amounts that occur more than once.

The core pattern is:

```text
Frequency Hashing
        +
Conditional Filtering
```

---

# 1. Problem Name

## 🔥 Fraud Transaction Detection

You are given a sequence of transactions.

A transaction is considered **fraudulent/suspicious** if it violates a given condition.

A representative version is:

> Given transaction amounts, find transaction amounts that occur more than once.

### Example

Input:

```text
8
100 200 100 300 400 200 500 100
```

Frequency:

```text
100 → 3
200 → 2
300 → 1
400 → 1
500 → 1
```

The repeated transaction amounts are:

```text
100 200
```

because:

```text
100 → appears 3 times
200 → appears 2 times
```

---

# 2. Pattern Used

## 🧠 Pattern: Frequency Hashing + Condition Checking

The basic structure is:

```text
Input
  ↓
Count occurrences
  ↓
Check condition
  ↓
Identify suspicious/fraudulent items
```

The main data structure is a:

```text
Dictionary
```

Create:

```python
freq = {}
```

Then count each transaction:

```python
freq[x] = freq.get(x, 0) + 1
```

This gives:

```text
Transaction Value → Frequency
```

For example:

```text
100 → 3
200 → 2
300 → 1
```

Then apply the condition:

```python
if freq[x] > 1:
```

---

# 3. How to Recognize the Pattern

This is the **most important part**.

Do not get distracted by words such as:

* transaction
* customer
* bank
* fraud
* account
* payment
* suspicious
* security
* financial institution

These words are usually just the **story**.

Instead, look at what the problem actually asks you to calculate.

---

## 🔑 Frequency Pattern Signals

If the question says:

* Find repeated transactions
* Find duplicate transactions
* Identify values occurring more than once
* Count transactions
* Count occurrences
* Find the most frequent transaction
* Find suspicious repeated values
* Detect duplicates
* Find transactions appearing `K` times
* Find values occurring at least `K` times

Think:

# → FREQUENCY HASHING

---

## Example 1

> "Find all transaction amounts that occur more than once."

Immediately think:

```text
value
  ↓
frequency
```

Therefore:

```python
freq = {}
```

---

## Example 2

> "Find the transaction amount that occurs most frequently."

Think:

```text
Frequency Hashing
        +
Maximum Tracking
```

---

## Example 3

> "Find the first transaction that appears twice."

Think:

```text
Duplicate Detection
        +
Set / Hashing
```

Here, you can detect the duplicate while traversing the array.

---

# 4. Solve Approach

For the representative problem:

> **Find transaction amounts that occur more than once.**

---

## Step 1 — Read the Transactions

```python
n = int(input())
arr = list(map(int, input().split()))
```

---

## Step 2 — Create a Frequency Dictionary

```python
freq = {}
```

---

## Step 3 — Count Every Transaction

```python
for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

Suppose:

```text
100 200 100 300 400 200 500 100
```

The dictionary becomes:

```text
100 → 3
200 → 2
300 → 1
400 → 1
500 → 1
```

---

## Step 4 — Check Which Values Are Repeated

```python
for x in freq:
    if freq[x] > 1:
        print(x, end=" ")
```

The condition:

```python
freq[x] > 1
```

means:

> This transaction occurred at least twice.

---

# 5. Optimal Python Code — TCS NQT Style

```python
n = int(input())
arr = list(map(int, input().split()))

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

for x in freq:
    if freq[x] > 1:
        print(x, end=" ")
```

For:

```text
8
100 200 100 300 400 200 500 100
```

Output:

```text
100 200
```

---

## Why This Code Is Good for TCS NQT

It is:

* Short
* Easy to remember
* Efficient
* Easy to debug
* Uses a dictionary
* Handles duplicate values naturally
* Can easily be modified for different conditions

The important reusable line is:

```python
freq[x] = freq.get(x, 0) + 1
```

---

# 6. Understanding `freq.get()`

This line is extremely important:

```python
freq[x] = freq.get(x, 0) + 1
```

Suppose:

```python
freq = {}
```

and we encounter:

```text
100
```

Since `100` does not exist:

```python
freq.get(100, 0)
```

returns:

```text
0
```

Then:

```text
0 + 1 = 1
```

So:

```text
100 → 1
```

If we encounter `100` again:

```python
freq.get(100, 0)
```

returns:

```text
1
```

Then:

```text
1 + 1 = 2
```

Now:

```text
100 → 2
```

So the same line handles both:

```text
First occurrence
        ↓
Create frequency

Later occurrence
        ↓
Increase frequency
```

---

# 7. Examples

## Example 1 — Basic

### Input

```text
7
10 20 10 30 40 20 50
```

Frequency:

```text
10 → 2
20 → 2
30 → 1
40 → 1
50 → 1
```

### Output

```text
10 20
```

---

# Example 2 — No Repeated Transactions

### Input

```text
6
100 200 300 400 500 600
```

Every transaction occurs exactly once.

Therefore, there are no repeated transactions.

If the problem specifies the output message:

```text
No Fraud
```

then print exactly that.

Example implementation:

```python
if not found:
    print("No Fraud")
```

**Always follow the exact output format given in the question.**

---

# Example 3 — Multiple Repeated Transactions

### Input

```text
10
50 20 50 30 20 50 40 30 60 20
```

Frequency:

```text
50 → 3
20 → 3
30 → 2
40 → 1
60 → 1
```

Repeated values:

```text
50 20 30
```

---

# 8. Dry Run

Consider:

```python
arr = [100, 200, 100, 300, 200]
```

Initially:

```python
freq = {}
```

---

## Step 1 — Read `100`

`100` does not exist.

```text
100 → 1
```

Now:

```text
freq = {
    100: 1
}
```

---

## Step 2 — Read `200`

`200` does not exist.

```text
200 → 1
```

Now:

```text
freq = {
    100: 1,
    200: 1
}
```

---

## Step 3 — Read `100`

`100` already exists:

```text
100 → 1
```

Increase:

```text
100 → 2
```

Now:

```text
freq = {
    100: 2,
    200: 1
}
```

---

## Step 4 — Read `300`

New value:

```text
300 → 1
```

Now:

```text
freq = {
    100: 2,
    200: 1,
    300: 1
}
```

---

## Step 5 — Read `200`

Existing:

```text
200 → 1
```

Increase:

```text
200 → 2
```

Final frequency table:

```text
100 → 2
200 → 2
300 → 1
```

---

## Step 6 — Apply the Condition

Condition:

```python
freq[x] > 1
```

Check:

```text
100 → 2 → YES
200 → 2 → YES
300 → 1 → NO
```

Final answer:

```text
100 200
```

---

# 9. Time Complexity

We traverse the array once to build the frequency table:

```text
O(N)
```

Then we traverse the frequency dictionary:

```text
O(N)
```

Therefore:

```text
O(N) + O(N)
```

which simplifies to:

# ⏱️ O(N)

Average-case dictionary lookup and insertion are:

```text
O(1)
```

Therefore:

```text
Time → O(N)
```

---

# 10. Space Complexity

The frequency dictionary can contain up to `N` different values.

Therefore:

```text
Space → O(N)
```

Overall:

```text
Time  → O(N)
Space → O(N)
```

---

# 🧠 11. VERY IMPORTANT — Fraud Problems Can Change Shape

The wording may change completely while the underlying pattern remains the same.

For example:

> "A bank wants to identify customers making multiple transactions."

The actual operation may simply be:

```text
Count occurrences
```

Therefore:

```text
Frequency Hashing
```

---

Another question:

> "Find accounts where transaction count exceeds K."

Now the pattern becomes:

```text
Frequency Hashing
        +
Condition
```

Code:

```python
for x in freq:
    if freq[x] > k:
        print(x)
```

---

# 🔥 12. Variation 1 — Find First Repeated Transaction

Suppose the question says:

> Find the first transaction that appears again.

You do not necessarily need a frequency dictionary.

Use a `set`.

```python
seen = set()

for x in arr:
    if x in seen:
        print(x)
        break

    seen.add(x)
```

### Pattern

```text
Duplicate Detection
        ↓
       Set
```

---

## Why a Set?

A set answers:

> **"Have I already seen this value?"**

You don't necessarily care about the exact frequency.

Example:

```text
100
200
100
```

When the second `100` appears:

```text
100 ∈ seen
```

Therefore:

```text
Duplicate found
```

---

# 🔥 13. Variation 2 — Count Fraudulent Values

Suppose:

> A transaction is fraudulent if it appears more than once. Count how many different fraudulent transaction values exist.

First build:

```python
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

Then:

```python
count = 0

for x in freq:
    if freq[x] > 1:
        count += 1

print(count)
```

Pattern:

```text
Frequency Hashing
        +
Counting
```

---

# 🔥 14. Variation 3 — Most Frequent Transaction

Question:

> Find the transaction amount that occurs most frequently.

Pattern:

```text
Frequency Hashing
        +
Maximum Tracking
```

Code:

```python
maximum = 0
answer = -1

for x in freq:
    if freq[x] > maximum:
        maximum = freq[x]
        answer = x

print(answer)
```

The important structure is:

```text
frequency
    ↓
compare frequencies
    ↓
keep maximum
```

---

# 🔥 15. Variation 4 — Frequency ≥ K

Question:

> Find all transaction amounts occurring at least `K` times.

Pattern:

```text
Frequency Hashing
        +
Condition
```

Code:

```python
for x in freq:
    if freq[x] >= k:
        print(x)
```

The difference is:

```text
More than K
→ freq[x] > k

At least K
→ freq[x] >= k

Exactly K
→ freq[x] == k
```

This distinction is important in TCS questions.

---

# 🔥 16. Variation 5 — Frequency Exactly K

Question:

> Find transactions occurring exactly `K` times.

Use:

```python
for x in freq:
    if freq[x] == k:
        print(x)
```

Pattern:

```text
Frequency Hashing
        +
Equality Condition
```

---

# 🔥 17. Variation 6 — Find Duplicate Count Including Repeated Occurrences

There is an important distinction.

Suppose:

```text
arr = [10, 10, 10, 20, 20]
```

Frequencies:

```text
10 → 3
20 → 2
```

### Number of different duplicate values

```text
2
```

because:

```text
10
20
```

are two different values.

### Number of extra duplicate occurrences

For `10`:

```text
3 - 1 = 2
```

For `20`:

```text
2 - 1 = 1
```

Total:

```text
2 + 1 = 3
```

So always read carefully whether the question asks for:

```text
Number of duplicate VALUES
```

or:

```text
Number of duplicate OCCURRENCES
```

---

# 🚨 18. The Key NQT Recognition Trick

Suppose the question says:

> "A financial institution wants to detect suspicious transactions made by customers."

Do **not** immediately think:

```text
Finance Problem ❌
```

Strip away the story.

Ask:

> **What mathematical operation is actually being performed?**

If the problem becomes:

```text
Count how many times each value occurs
```

then:

# → Frequency Hashing

---

If it becomes:

```text
Have I seen this value before?
```

then:

# → Set / Hashing

---

If it becomes:

```text
Find the value with the highest frequency
```

then:

# → Frequency Hashing + Maximum

---

If it becomes:

```text
Find values occurring at least K times
```

then:

# → Frequency Hashing + Condition

---

# 🧠 19. Frequency Hashing vs Set

This distinction is extremely important.

## Use a Frequency Dictionary When:

You need to know:

```text
HOW MANY TIMES?
```

Example:

> How many times did each transaction occur?

Use:

```python
freq = {}
```

---

## Use a Set When:

You only need to know:

```text
HAVE I SEEN THIS BEFORE?
```

Example:

> Find the first repeated transaction.

Use:

```python
seen = set()
```

---

## Quick Comparison

| Requirement                    | Data Structure |
| ------------------------------ | -------------- |
| Count occurrences              | Dictionary     |
| Find frequency                 | Dictionary     |
| Most frequent value            | Dictionary     |
| Values appearing K times       | Dictionary     |
| Detect duplicate               | Set            |
| Find first repeated value      | Set            |
| Check whether seen before      | Set            |
| Preserve frequency information | Dictionary     |

---

# 🚨 20. Common Mistakes

## Mistake 1 — Getting Distracted by the Story

Seeing:

```text
Bank
Fraud
Transaction
Customer
Security
```

does not mean you need a special financial algorithm.

Ask:

```text
What operation is actually required?
```

---

## Mistake 2 — Using a Set When Frequency Is Required

A set removes duplicate information.

For:

```text
[10, 10, 10, 20]
```

the set is:

```text
{10, 20}
```

You lose:

```text
10 → 3
20 → 1
```

Therefore:

> If the question asks **how many times**, use a frequency dictionary.

---

## Mistake 3 — Checking Duplicates with Nested Loops

You could compare every pair:

```text
for i
    for j
        compare
```

This gives:

```text
O(N²)
```

For simple duplicate/frequency problems, hashing gives:

```text
O(N)
```

on average.

---

## Mistake 4 — Wrong Condition

These are different:

```python
freq[x] > 1
```

means:

```text
More than once
```

```python
freq[x] >= k
```

means:

```text
At least K times
```

```python
freq[x] == k
```

means:

```text
Exactly K times
```

Read the wording carefully.

---

## Mistake 5 — Ignoring Output Requirements

If no fraudulent transaction exists, the question may require:

```text
No Fraud
```

or:

```text
-1
```

or:

```text
No duplicate
```

or possibly an empty output.

Do not assume.

> **Print exactly what the problem statement specifies.**

---

# 🎯 21. TCS NQT Pattern Map

| Problem Wording                 | Pattern                      |
| ------------------------------- | ---------------------------- |
| Repeated transaction            | Frequency Hashing            |
| Duplicate transaction           | Set / Frequency Hashing      |
| Count transactions              | Frequency Hashing            |
| Count occurrences               | Frequency Hashing            |
| Most frequent transaction       | Frequency + Maximum          |
| Least frequent transaction      | Frequency + Minimum          |
| Appears more than once          | `freq[x] > 1`                |
| Appears at least K times        | `freq[x] >= k`               |
| Appears exactly K times         | `freq[x] == k`               |
| First repeated transaction      | Set                          |
| First non-repeating transaction | Frequency + Second Traversal |

---

# 🎯 22. What to Remember for TCS NQT

Do not memorize:

> **"Fraud = Dictionary."**

Instead memorize:

```text
Ignore the story
      ↓
Find the actual operation
      ↓
Repeated / Count / Occurrence?
      ↓
Frequency Hashing
```

The two most important templates are:

---

## Template 1 — Count Frequency

```python
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

---

## Template 2 — Detect Duplicate

```python
seen = set()

for x in arr:
    if x in seen:
        # duplicate found

    seen.add(x)
```

---

# ⚡ 23. Quick Revision

### Count frequency

```python
freq[x] = freq.get(x, 0) + 1
```

### Repeated values

```python
if freq[x] > 1:
```

### At least K

```python
if freq[x] >= k:
```

### Exactly K

```python
if freq[x] == k:
```

### First duplicate

```python
if x in seen:
```

### Most frequent

```text
Frequency + Maximum
```

---

# 🧠 24. Memory Trick

Remember:

```text
FRAUD STORY
     ↓
IGNORE THE STORY
     ↓
WHAT IS BEING CHECKED?
     ↓
REPEATED / COUNT / OCCURRENCE
     ↓
FREQUENCY HASHING
```

The main formula:

```text
REPEATED VALUES
      ↓
COUNT FREQUENCY
      ↓
DICTIONARY
      ↓
APPLY CONDITION
```

For duplicate detection:

```text
SEEN BEFORE?
     ↓
SET
```

For frequency:

```text
HOW MANY TIMES?
     ↓
DICTIONARY
```

---

# 🚀 Final NQT Cheat Sheet

```text
Repeated / Duplicate
→ Set OR Frequency Dictionary

Need frequency?
→ Dictionary

Need "more than once"?
→ freq[x] > 1

Need "at least K"?
→ freq[x] >= k

Need "exactly K"?
→ freq[x] == k

Need most frequent?
→ Frequency + Maximum

Need first repeated?
→ Set

Need first non-repeating?
→ Frequency + Second Traversal
```

### 🔥 Final Pattern Recognition

```text
"Fraud?"
"Suspicious?"
"Repeated?"
"Duplicate?"
"Occurrence?"
"Count?"
"Appears K times?"
        ↓
IGNORE THE STORY
        ↓
IDENTIFY THE OPERATION
        ↓
COUNT / CHECK SEEN
        ↓
DICTIONARY / SET
        ↓
APPLY THE CONDITION
```

> **FRAUD TRANSACTION → REMOVE THE BUSINESS STORY → IDENTIFY REPETITION/COUNTING → HASHING**
