# 🔥 7. Anagram

> A very common **String + Hashing** problem for TCS NQT.
>
> The main idea is:
>
> **Two strings are anagrams if they contain exactly the same characters with exactly the same frequencies.**
>
> Character order does **not** matter.

---

# 1. Problem Name

## Check Whether Two Strings Are Anagrams

Given two strings, determine whether they are **anagrams** of each other.

Two strings are anagrams when:

```text
Same characters
+
Same frequencies
```

The order can be different.

### Example

```text
String 1:
listen

String 2:
silent
```

Both contain:

```text
l → 1
i → 1
s → 1
t → 1
e → 1
n → 1
```

Therefore:

```text
Output:
Anagram
```

---

# 2. What Is an Anagram?

An anagram is a string formed by rearranging the characters of another string while keeping:

* The same characters
* The same number of occurrences

### Example

```text
listen
silent
```

They contain exactly the same characters.

Therefore:

```text
listen → silent
```

is an anagram relationship.

---

# 3. Pattern Used

## 🧠 Frequency Hashing

The primary pattern is:

```text
FREQUENCY HASHING
```

We count the frequency of every character.

For two strings to be anagrams:

```text
frequency of every character in String 1
=
frequency of every character in String 2
```

The order does not matter.

---

# 4. How to Recognize the Pattern

Look for phrases such as:

* Check whether two strings are anagrams
* Same characters in different order
* Rearrangement of characters
* Check whether one string can be formed by rearranging another
* Same character frequencies
* Check whether two strings are permutations of each other

The strongest clue is:

> **Same characters + same number of occurrences + order doesn't matter**

Immediately think:

```text
Hashing
+
Frequency Map
```

---

# 5. Core Concept

Suppose:

```text
s1 = "listen"
s2 = "silent"
```

Count `s1`:

```text
l → 1
i → 1
s → 1
t → 1
e → 1
n → 1
```

Now process `s2`.

For every character in `s2`, decrease its frequency:

```text
s → 0
i → 0
l → 0
e → 0
n → 0
t → 0
```

At the end:

```text
Every frequency = 0
```

Therefore:

```text
Anagram
```

---

# 6. Why Frequency Matters

Consider:

```text
s1 = "aabbc"
s2 = "abbbc"
```

Both strings contain:

```text
a
b
c
```

So checking only whether the **set of characters** is the same is not enough.

Frequencies are:

### String 1

```text
a → 2
b → 2
c → 1
```

### String 2

```text
a → 1
b → 3
c → 1
```

The frequencies are different.

Therefore:

```text
Not Anagram
```

### Important Rule

> **Anagram checking requires frequency equality, not just character presence.**

---

# 7. First Check — String Length

Before building the frequency map, check:

```python
if len(s1) != len(s2):
```

If the lengths are different, they cannot be anagrams.

Example:

```text
s1 = "abc"
s2 = "abcd"
```

Lengths:

```text
3 != 4
```

Therefore:

```text
Not Anagram
```

This avoids unnecessary processing.

---

# 8. Optimal Python Code — TCS NQT Style

```python
s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("Not Anagram")
else:
    freq = {}

    # Count characters in first string
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    # Subtract characters from second string
    for ch in s2:
        freq[ch] = freq.get(ch, 0) - 1

    is_anagram = True

    for value in freq.values():
        if value != 0:
            is_anagram = False
            break

    if is_anagram:
        print("Anagram")
    else:
        print("Not Anagram")
```

---

# 9. Understanding the Code

There are three important parts.

## Part 1 — Count String 1

```python
for ch in s1:
    freq[ch] = freq.get(ch, 0) + 1
```

This creates:

```text
character → frequency
```

For:

```text
aabbc
```

we get:

```text
a → 2
b → 2
c → 1
```

---

## Part 2 — Subtract String 2

```python
for ch in s2:
    freq[ch] = freq.get(ch, 0) - 1
```

Every matching character reduces the frequency.

If the strings are anagrams, everything eventually becomes:

```text
0
```

---

## Part 3 — Check the Result

```python
for value in freq.values():
    if value != 0:
        is_anagram = False
        break
```

If even one frequency is not zero:

```text
Not Anagram
```

If every frequency is zero:

```text
Anagram
```

---

# 10. Example 1 — Anagram

### Input

```text
listen
silent
```

### Output

```text
Anagram
```

---

# 11. Dry Run — Example 1

### String 1

```text
listen
```

Build the frequency map:

| Character | Frequency |
| :-------: | --------: |
|    `l`    |         1 |
|    `i`    |         1 |
|    `s`    |         1 |
|    `t`    |         1 |
|    `e`    |         1 |
|    `n`    |         1 |

Current map:

```text
l → 1
i → 1
s → 1
t → 1
e → 1
n → 1
```

Now process:

```text
silent
```

---

### Character `s`

```text
s: 1 → 0
```

---

### Character `i`

```text
i: 1 → 0
```

---

### Character `l`

```text
l: 1 → 0
```

---

### Character `e`

```text
e: 1 → 0
```

---

### Character `n`

```text
n: 1 → 0
```

---

### Character `t`

```text
t: 1 → 0
```

Final map:

```text
l → 0
i → 0
s → 0
t → 0
e → 0
n → 0
```

Everything is zero.

Therefore:

```text
Anagram
```

---

# 12. Complete Dry Run Table

| Step | Character from `s2` | Frequency Before | Frequency After |
| ---: | :-----------------: | ---------------: | --------------: |
|    1 |         `s`         |                1 |               0 |
|    2 |         `i`         |                1 |               0 |
|    3 |         `l`         |                1 |               0 |
|    4 |         `e`         |                1 |               0 |
|    5 |         `n`         |                1 |               0 |
|    6 |         `t`         |                1 |               0 |

Final:

```text
All frequencies = 0
```

Therefore:

```text
Anagram
```

---

# 13. Example 2 — Not Anagram

### Input

```text
hello
world
```

The character frequencies are different.

Therefore:

```text
Output:
Not Anagram
```

---

# 14. Example 3 — Same Characters, Different Frequencies

### Input

```text
aabbc
abbbc
```

String 1:

```text
a → 2
b → 2
c → 1
```

String 2:

```text
a → 1
b → 3
c → 1
```

After subtraction, the frequencies are not all zero.

Therefore:

```text
Output:
Not Anagram
```

---

# 15. Example 4 — Different Length

### Input

```text
abc
abcd
```

Immediately:

```text
len(s1) != len(s2)
```

Therefore:

```text
Output:
Not Anagram
```

No frequency calculation is necessary.

---

# 16. Example 5 — Duplicate Characters

Consider:

```text
s1 = "aabb"
s2 = "abab"
```

Frequencies:

```text
s1:
a → 2
b → 2
```

```text
s2:
a → 2
b → 2
```

Therefore:

```text
Anagram
```

The order is different, but the frequencies are identical.

---

# 17. Example 6 — Empty Strings

If both strings are empty:

```text
s1 = ""
s2 = ""
```

They have the same length and no character frequencies differ.

Under the usual mathematical definition:

```text
Output:
Anagram
```

However, always follow the exact TCS problem specification if it defines special handling for empty input.

---

# 18. Important TCS Edge Case — Spaces

Suppose the strings are:

```text
"The eyes"
"they see"
```

If spaces should be ignored, remove them:

```python
s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")
```

Then compare.

But do **not** automatically remove spaces.

If the problem says spaces are meaningful characters, keep them.

### Recognition Rule

```text
Question says ignore spaces
        ↓
Remove spaces

Question doesn't say that
        ↓
Treat input exactly as specified
```

---

# 19. Important TCS Edge Case — Case Sensitivity

Consider:

```text
Listen
silent
```

Python treats:

```text
L
```

and:

```text
l
```

as different characters.

Therefore, case-sensitive comparison would say:

```text
Not Anagram
```

If the question says **case-insensitive**, normalize both strings:

```python
s1 = s1.lower()
s2 = s2.lower()
```

Then compare.

### Important

Do not use `.lower()` unless the problem explicitly requires ignoring case.

---

# 20. Alternative Solution — Sorting

Another common solution is:

```python
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
```

This is valid.

For example:

```text
listen
```

becomes:

```text
eilnst
```

and:

```text
silent
```

also becomes:

```text
eilnst
```

Therefore they are anagrams.

But sorting requires:

```text
O(N log N)
```

while frequency hashing can achieve:

```text
O(N)
```

So for your **optimal TCS NQT pattern sheet**, frequency hashing is the better pattern to memorize.

---

# 21. Hashing vs Sorting

| Method            |       Time |                            Space | Recommended |
| ----------------- | ---------: | -------------------------------: | :---------: |
| Frequency Hashing |       O(N) |                             O(K) |    ✅ Best   |
| Sorting           | O(N log N) | O(N) depending on implementation |   👍 Valid  |
| Nested Loops      |      O(N²) |                             O(1) |   ❌ Avoid   |

Where:

```text
K = number of distinct characters
```

---

# 22. Why Hashing Is the Natural Solution

The problem does not care about character order.

It only asks:

```text
What characters exist?
+
How many times does each occur?
```

That is exactly what a frequency map provides.

Instead of spending time arranging characters:

```text
Sorting
   ↓
Arrange
   ↓
Compare
```

we simply count:

```text
Hashing
   ↓
Count
   ↓
Compare
```

Therefore:

```text
Anagram
   ↓
Frequency
   ↓
Hash Map
```

---

# 23. ⚠️ TCS Exam Traps

## Trap 1 — Checking only unique characters

Wrong idea:

```text
"aabb"
"abbb"
```

Both contain:

```text
a
b
```

But they are not anagrams.

Frequency matters.

---

## Trap 2 — Different lengths

```text
abc
abcd
```

Cannot be anagrams.

Always check:

```python
len(s1) == len(s2)
```

---

## Trap 3 — Case sensitivity

```text
A
a
```

are different unless the problem says to ignore case.

---

## Trap 4 — Spaces

```text
"rail safety"
"fairy tales"
```

These are anagrams only if spaces are ignored.

---

## Trap 5 — Order

This is **not** important.

For example:

```text
listen
silent
```

are anagrams even though the order is completely different.

---

# 24. Pattern Recognition Shortcut

When you see:

```text
TWO STRINGS
      +
SAME CHARACTERS
      +
SAME FREQUENCIES
      +
ORDER DOESN'T MATTER
```

Think:

# 🧠 FREQUENCY HASHING

Mental process:

```text
String 1
   ↓
Count
   ↓
Frequency Map
   ↓
String 2
   ↓
Subtract
   ↓
Everything = 0?
   ↓
YES → Anagram
NO  → Not Anagram
```

---

# 25. Core Code to Memorize

You don't need to memorize every line of the program.

Remember the actual pattern:

```python
freq = {}

for ch in s1:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s2:
    freq[ch] = freq.get(ch, 0) - 1

for value in freq.values():
    if value != 0:
        # Not anagram
```

And remember the initial length check:

```python
if len(s1) != len(s2):
    # Not anagram
```

---

# 26. General Frequency Hashing Template

This is one of the most useful templates for TCS NQT:

```python
freq = {}

for x in data:
    freq[x] = freq.get(x, 0) + 1
```

It can be used for:

```text
Characters
Words
Integers
Array elements
Strings
```

Whenever the question asks:

```text
How many times does X occur?
```

think:

```text
Frequency Map
```

---

# 27. Important Difference — Set vs Frequency Map

### Set

A set answers:

```text
Does this element exist?
```

Example:

```text
"aabbcc"
```

Set:

```text
{a, b, c}
```

---

### Frequency Map

A frequency map answers:

```text
How many times does this element occur?
```

Example:

```text
a → 2
b → 2
c → 2
```

For anagrams, we need:

```text
Frequency Map
```

not merely a set.

---

# 28. Variations You Should Recognize

The same pattern can appear as:

### 1. Check Anagram

```text
frequency(s1) == frequency(s2)
```

---

### 2. Check Permutation

If one string is a rearrangement of another:

```text
Frequency Hashing
```

---

### 3. Group Anagrams

Strings with the same frequency signature belong to the same group.

Conceptually:

```text
same frequency pattern
        ↓
same anagram group
```

---

### 4. Find Anagram Pairs

Compare character-frequency patterns.

---

### 5. Find Different Character Frequencies

Again:

```text
Frequency Map
```

is usually the first pattern to consider.

---

# 29. Pattern Family

```text
FREQUENCY HASHING
│
├── Anagram
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

Notice the connection with Problem #6:

```text
#6 First Non-Repeating Character
        ↓
Frequency Map
```

and:

```text
#7 Anagram
        ↓
Frequency Map
```

So these two problems belong to the same **String + Hashing family**.

---

# 30. Edge Cases Checklist

Before submitting, mentally test:

```text
✓ Same strings
✓ Different order
✓ Different frequencies
✓ Different lengths
✓ Duplicate characters
✓ One-character strings
✓ Empty strings if allowed
✓ Uppercase/lowercase
✓ Spaces
✓ Special characters if allowed
```

---

# 31. Quick Revision

Before the exam, remember:

```text
Problem:
Check whether two strings are anagrams

Pattern:
Frequency Hashing

Condition:
Same characters
+
Same frequencies

Order:
Doesn't matter

Step 1:
Check lengths

Step 2:
Count String 1

Step 3:
Subtract String 2

Step 4:
All frequencies == 0 ?

YES → Anagram
NO  → Not Anagram

Time:
O(N)

Space:
O(K)
```

---

# 🧠 32. Final Memory Trick

Memorize:

```text
ANAGRAM
   ↓
SAME CHARACTERS
   +
SAME FREQUENCY
   ↓
HASH MAP
   ↓
COUNT
   ↓
SUBTRACT
   ↓
EVERYTHING = 0
```

### One-line recognition rule:

> **"Same characters + same frequency, order doesn't matter" → Frequency Hashing.**

---

# 🚀 33. Final Takeaway

The real concept behind anagram checking is:

```text
Don't care about ORDER
        ↓
Care about FREQUENCY
        ↓
Use HASHING
```

So when TCS gives you:

```text
"Are these two strings rearrangements of each other?"
```

don't think about permutations.

Don't immediately think about sorting.

Think:

```text
TWO STRINGS
     ↓
FREQUENCY MAP
     ↓
COMPARE FREQUENCIES
     ↓
O(N)
```

> ### 🔥 TCS NQT Memory Formula
>
> **`ANAGRAM → SAME CHARACTERS + SAME FREQUENCY → HASHING`**
