# 🔥 6. First Non-Repeating Character

> A very common **String + Hashing** pattern for TCS NQT.
>
> The main idea is simple:
>
> **Count the frequency first → then scan the original string to preserve order.**

---

# 1. Problem Name

## First Non-Repeating Character

Given a string, find the **first character that occurs exactly once**.

If every character occurs more than once, return:

```text
-1
```

### Example

```text
Input:
aabbcdde

Output:
c
```

Frequencies:

```text
a → 2
b → 2
c → 1
d → 2
e → 1
```

Both `c` and `e` occur exactly once.

But `c` appears first in the original string.

Therefore:

```text
Answer = c
```

---

# 2. Pattern Used

## 🧠 Frequency Hashing + Second Traversal

We use a dictionary to count how many times each character occurs.

Then we traverse the original string again from **left to right**.

The first character whose frequency is `1` is the answer.

```text
Count Frequencies
       ↓
Scan Original String
       ↓
Find frequency == 1
       ↓
Answer
```

### Core Pattern

```text
FREQUENCY MAP
+
ORIGINAL ORDER
```

---

# 3. How to Recognize the Pattern

Look for phrases such as:

* First non-repeating character
* First unique character
* First character occurring once
* First character with frequency `1`
* Find the first character that appears only once
* Character frequency + original order

The strongest clue is:

> **FIRST + UNIQUE / NON-REPEATING**

Immediately think:

```text
Frequency Hashing
```

But there is an important distinction:

```text
Frequency tells us:
"How many times?"

Original string tells us:
"Which one comes first?"
```

Therefore we need both.

---

# 4. The Key Idea

Consider:

```text
s = "swiss"
```

First count every character:

```text
s → 3
w → 1
i → 1
```

Now scan the original string:

```text
s → frequency 3 → skip

w → frequency 1 → FOUND
```

Therefore:

```text
Answer = w
```

Notice something important:

We did **not** search the dictionary for a frequency of `1`.

Why?

Because the dictionary only tells us frequency.

The question asks for the **first** such character.

So we scan:

```text
original string → left to right
```

---

# 5. Why Two Traversals?

The problem has two separate requirements:

```text
1. Know the frequency
2. Preserve original order
```

The first traversal handles:

```text
Frequency
```

The second traversal handles:

```text
Order
```

Therefore:

```text
Traversal 1 → Count
Traversal 2 → Find first unique
```

This is one of the most important concepts in this problem.

---

# 6. Step-by-Step Approach

Suppose:

```text
s = "aabbcdde"
```

### Step 1 — Create frequency map

```python
freq = {}
```

---

### Step 2 — Count every character

After processing the string:

```text
a → 2
b → 2
c → 1
d → 2
e → 1
```

---

### Step 3 — Scan original string

Start from the beginning:

```text
a → 2 → skip
a → 2 → skip
b → 2 → skip
b → 2 → skip
c → 1 → FOUND
```

Stop immediately.

Answer:

```text
c
```

---

# 7. Optimal Python Code — TCS NQT Style

```python
s = input().strip()

freq = {}

# Count frequency of every character
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Find the first non-repeating character
answer = -1

for ch in s:
    if freq[ch] == 1:
        answer = ch
        break

print(answer)
```

This is the version to remember for TCS NQT.

It is:

* Simple
* Easy to reproduce
* `O(N)`
* Uses standard Python
* Does not require sorting
* Handles repeated characters naturally

---

# 8. Understanding `freq.get()`

This line is important:

```python
freq[ch] = freq.get(ch, 0) + 1
```

Suppose:

```text
freq = {}
```

and we process:

```text
a
```

Since `a` doesn't exist:

```python
freq.get('a', 0)
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
a → 1
```

Process another `a`:

```text
freq.get('a', 0)
```

returns:

```text
1
```

Then:

```text
1 + 1 = 2
```

So:

```text
a → 2
```

---

# 9. Example 1

### Input

```text
aabbcdde
```

### Frequency Map

```text
a → 2
b → 2
c → 1
d → 2
e → 1
```

### Scan

```text
a → 2 → Skip
a → 2 → Skip
b → 2 → Skip
b → 2 → Skip
c → 1 → Found
```

### Output

```text
c
```

---

# 10. Dry Run

String:

```text
a a b b c d d e
```

Initially:

```text
freq = {}
```

### First Traversal

Process `a`:

```text
a → 1
```

Process second `a`:

```text
a → 2
```

Process `b`:

```text
b → 1
```

Process second `b`:

```text
b → 2
```

Process `c`:

```text
c → 1
```

Process `d`:

```text
d → 1
```

Process second `d`:

```text
d → 2
```

Process `e`:

```text
e → 1
```

Final map:

```text
a → 2
b → 2
c → 1
d → 2
e → 1
```

---

# 11. Second Traversal

Now scan:

```text
a a b b c d d e
```

### Position 0

```text
a → frequency = 2
```

Skip.

---

### Position 1

```text
a → frequency = 2
```

Skip.

---

### Position 2

```text
b → frequency = 2
```

Skip.

---

### Position 3

```text
b → frequency = 2
```

Skip.

---

### Position 4

```text
c → frequency = 1
```

Found.

Stop.

```text
Answer = c
```

---

# 12. Dry Run Table

| Position | Character | Frequency | Action  |
| -------: | :-------: | --------: | :------ |
|        0 |    `a`    |         2 | Skip    |
|        1 |    `a`    |         2 | Skip    |
|        2 |    `b`    |         2 | Skip    |
|        3 |    `b`    |         2 | Skip    |
|        4 |    `c`    |         1 | ✅ Found |

Final answer:

```text
c
```

---

# 13. Example 2 — All Characters Repeated

### Input

```text
aabbcc
```

Frequency:

```text
a → 2
b → 2
c → 2
```

No character has frequency `1`.

Therefore:

```text
Output:
-1
```

---

# 14. Example 3 — First Character Is Not Unique

Consider:

```text
abcdefa
```

Frequency:

```text
a → 2
b → 1
c → 1
d → 1
e → 1
f → 1
```

Scan from left:

```text
a → 2 → Skip
b → 1 → Found
```

Therefore:

```text
Output:
b
```

---

# 15. Example 4 — One Character

### Input

```text
z
```

Frequency:

```text
z → 1
```

Therefore:

```text
Output:
z
```

---

# 16. Example 5 — Case Sensitivity

Consider:

```text
aAbB
```

Python treats lowercase and uppercase characters as different:

```text
a ≠ A
b ≠ B
```

Frequencies:

```text
a → 1
A → 1
b → 1
B → 1
```

Therefore:

```text
Output:
a
```

### Important

Do **not** automatically convert the string to lowercase.

Only use:

```python
s = s.lower()
```

if the question explicitly says:

> Ignore case.

---

# 17. What About Spaces?

Suppose the input is:

```text
hello world
```

If spaces are supposed to be treated as characters, then:

```python
s = input()
```

is safer.

Using:

```python
s = input().strip()
```

removes leading and trailing whitespace.

For normal TCS questions involving a word or a string without meaningful spaces, `.strip()` is fine.

If the problem explicitly says spaces are part of the string, preserve them.

---

# 18. Why Not Use Nested Loops?

You could solve it without hashing:

```python
for i in range(len(s)):
    count = 0

    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1

    if count == 1:
        print(s[i])
        break
```

This works.

But for every character, we scan the entire string.

Therefore:

```text
Time = O(N²)
```

Our frequency-map approach needs only two linear traversals:

```text
Time = O(N)
```

---

# 19. Why Not Sort the String?

Sorting may seem tempting:

```python
sorted(s)
```

But the problem asks for the:

> **FIRST** non-repeating character.

Sorting changes the original order.

For example:

```text
s = "dcab"
```

Sorting gives:

```text
a b c d
```

The original order was:

```text
d c a b
```

Therefore, sorting is not the natural solution.

The correct pattern is:

```text
Frequency Map + Original Order
```

---

# 20. Why Not Just Find `freq[ch] == 1`?

This is a subtle but important mistake.

Suppose:

```text
s = "aabbcdde"
```

The unique characters are:

```text
c
e
```

Both have:

```text
frequency = 1
```

But the answer is:

```text
c
```

because `c` occurs first.

Therefore:

```text
Dictionary → frequency
String → order
```

You need both.

---

# 21. Complexity

We traverse the string twice.

First traversal:

```text
O(N)
```

Second traversal:

```text
O(N)
```

Total:

```text
O(N) + O(N)
```

Drop the constant:

```text
O(N)
```

### Final Complexity

```text
Time Complexity:  O(N)
Space Complexity: O(K)
```

Where:

```text
K = number of distinct characters
```

For lowercase English letters:

```text
K ≤ 26
```

So the auxiliary space is effectively constant for that fixed alphabet.

---

# 22. Brute Force vs Hashing

| Approach          |       Time |   Space | Recommended |
| ----------------- | ---------: | ------: | :---------: |
| Nested Loops      |      O(N²) |    O(1) |      ❌      |
| Sorting           | O(N log N) | Depends |      ❌      |
| Frequency Hashing |       O(N) |    O(K) |      ✅      |

For TCS NQT:

```text
Frequency Hashing
        ↓
      O(N)
```

is the pattern you should recognize.

---

# 23. ⚠️ TCS Exam Trap

Do not confuse these three problems.

## 1. First Non-Repeating Character

Find the first character where:

```text
frequency == 1
```

---

## 2. First Repeating Character

Find the first character that repeats.

Depending on the exact wording, this may require tracking when a character is encountered for the second time.

---

## 3. Count Non-Repeating Characters

Do **not** stop at the first unique character.

Instead, count all characters where:

```text
frequency == 1
```

These are related problems, but the required output is different.

---

# 24. Important Variations

## Variation 1 — First Repeating Character

Example:

```text
s = "abcad"
```

`a` is the first character that appears again.

Pattern:

```text
Hashing
```

---

## Variation 2 — Count All Non-Repeating Characters

Instead of:

```python
break
```

process the entire string and count every:

```python
freq[ch] == 1
```

---

## Variation 3 — Character Occurring Exactly K Times

Replace:

```python
if freq[ch] == 1:
```

with:

```python
if freq[ch] == k:
```

---

## Variation 4 — Most Frequent Character

Track the maximum frequency:

```text
frequency → maximum
```

---

## Variation 5 — Least Frequent Character

Track the minimum frequency.

If the question also asks for the **first** such character, preserve original order during the final scan.

---

# 25. Pattern Family

```text
FREQUENCY HASHING
│
├── First Non-Repeating Character
│
├── First Repeating Character
│
├── Count Unique Characters
│
├── Most Frequent Character
│
├── Least Frequent Character
│
└── Character Occurring K Times
```

The common foundation is:

```text
Count → Use Frequency
```

---

# 26. General Frequency Map Template

This is worth memorizing separately:

```python
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

It works for:

```text
Characters
Strings
Integers
Words
Array elements
```

Example:

```python
arr = [1, 2, 2, 3, 3, 3]
```

produces:

```text
1 → 1
2 → 2
3 → 3
```

So whenever a TCS problem asks:

```text
How many times does X occur?
```

think:

```text
Frequency Map
```

---

# 27. Pattern Recognition Shortcut

When you see:

```text
FIRST
+
UNIQUE / NON-REPEATING
+
CHARACTER
```

immediately think:

```text
FREQUENCY MAP
```

Then ask:

> **Do I need the first one?**

If yes:

```text
Count frequencies
      ↓
Scan original string
      ↓
freq[ch] == 1
      ↓
Stop
```

---

# 28. Core Skeleton

```python
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
```

If no character is found, use:

```python
answer = -1
```

and print it after the loop.

---

# 29. 🧠 Mental Model

Think of the dictionary as a **scoreboard**.

First pass:

```text
Character → How many times?
```

Example:

```text
a → 2
b → 2
c → 1
d → 2
e → 1
```

Then the string acts as the **queue/order**:

```text
a → a → b → b → c → d → d → e
```

We check the queue from the front.

The first character whose scoreboard says:

```text
1
```

wins.

Therefore:

```text
Dictionary = Frequency
String      = Order
```

This is the key concept behind the entire problem.

---

# 30. Edge Cases

Always test:

### All repeated

```text
aabbcc
```

Expected:

```text
-1
```

---

### All unique

```text
abcdef
```

Expected:

```text
a
```

---

### First character repeated

```text
aabbc
```

Expected:

```text
c
```

---

### One character

```text
z
```

Expected:

```text
z
```

---

### Mixed case

```text
aAbB
```

Expected:

```text
a
```

if case-sensitive.

---

### Multiple unique characters

```text
aabbcdde
```

Unique:

```text
c, e
```

Answer:

```text
c
```

---

# 31. Quick Revision

Before the exam, remember:

```text
Problem:
First non-repeating character

Pattern:
Frequency Hashing

Step 1:
Count every character

Step 2:
Scan original string

Condition:
freq[ch] == 1

Answer:
First matching character

If none:
-1

Time:
O(N)

Space:
O(K)
```

---

# 🔥 32. Final Memory Trick

Memorize this:

```text
FIRST + UNIQUE
       ↓
FREQUENCY MAP
       ↓
COUNT EVERYTHING
       ↓
SCAN ORIGINAL ORDER
       ↓
freq == 1
       ↓
ANSWER
```

### One-line formula:

> **COUNT → SCAN → `frequency == 1`**

---

# 🚀 33. Final Takeaway

The important lesson is not just how to write the dictionary.

The real pattern is understanding that the problem has **two jobs**:

```text
JOB 1
Find frequency
      ↓
Hash Map
```

and:

```text
JOB 2
Preserve original order
      ↓
Second traversal
```

Therefore:

```text
FIRST NON-REPEATING CHARACTER
             ↓
      FREQUENCY HASHING
             ↓
       TWO TRAVERSALS
             ↓
   FIRST freq[ch] == 1
             ↓
           O(N)
```

> ### 🧠 TCS NQT Memory Formula
>
> **`FIRST + UNIQUE → FREQUENCY MAP → SCAN ORIGINAL ORDER → freq == 1`**
