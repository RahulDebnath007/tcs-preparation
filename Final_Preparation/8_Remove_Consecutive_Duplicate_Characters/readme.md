# 🔥 8. Remove Consecutive Duplicate Characters

> A very TCS-friendly **String Traversal** problem.
>
> The solution is simple, but the important part is recognizing the word **CONSECUTIVE**.
>
> We are **not removing duplicates globally**. We are only removing repeated characters that occur **next to each other**.

---

# 1. Problem Name

## Remove Consecutive Duplicate Characters

Given a string, remove consecutive duplicate characters so that each group of identical adjacent characters appears only once.

### Example

```text
Input:
aaabbccdaa

Output:
abcda
```

Break the string into consecutive groups:

```text
aaa → a
bb  → b
cc  → c
d   → d
aa  → a
```

Therefore:

```text
aaabbccdaa
     ↓
abcda
```

---

# 2. Pattern Used

## 🧠 String Traversal + Previous Character Comparison

We do **not** need hashing.

Why?

Because the problem only asks:

> Is the current character the same as the previous character?

The basic rule is:

```text
if current != previous:
    keep current
else:
    skip current
```

So the pattern is:

```text
CURRENT CHARACTER
        ↓
COMPARE WITH PREVIOUS
        ↓
Same?
 ↙          ↘
YES          NO
 ↓            ↓
Skip         Keep
```

---

# 3. How to Recognize the Pattern

Look for phrases such as:

* Remove consecutive duplicates
* Remove repeated adjacent characters
* Compress consecutive characters
* Eliminate adjacent duplicates
* Keep only one character from each group
* Remove duplicate characters occurring consecutively

The most important word is:

# **CONSECUTIVE**

For example:

```text
aaabbc
```

contains consecutive duplicate groups:

```text
aaa
bb
```

So:

```text
aaabbc
  ↓
abc
```

But:

```text
abaca
```

should remain:

```text
abaca
```

Why?

Because the repeated `a` characters are **not adjacent**.

---

# 4. What Does "Consecutive" Mean?

Consecutive means:

> **Immediately next to each other.**

Consider:

```text
a a b c a
```

The first two `a`s are consecutive.

But the first `a` and last `a` are not consecutive.

Therefore:

```text
aaabc
```

would compress to:

```text
abc
```

while:

```text
abaca
```

remains:

```text
abaca
```

### 🧠 Key distinction

```text
CONSECUTIVE DUPLICATE
        ≠
GLOBAL DUPLICATE
```

This distinction is extremely important in TCS questions.

---

# 5. Solve Approach

Consider:

```text
s = "aaabbccdaa"
```

Start with an empty result:

```text
result = []
```

Take the first character:

```text
a
```

There is nothing before it.

So keep it:

```text
result = [a]
```

Next character:

```text
a
```

Compare with the last kept character:

```text
a == a
```

Duplicate → skip.

Continue:

```text
a → skip
b → keep
b → skip
c → keep
c → skip
d → keep
a → keep
a → skip
```

Final result:

```text
abcda
```

---

# 6. Optimal Python Code — TCS NQT Style

```python
s = input().strip()

result = []

for ch in s:
    if not result or result[-1] != ch:
        result.append(ch)

print("".join(result))
```

This is the clean solution to remember.

---

# 7. Understanding `result[-1]`

This is an important Python concept.

```python
result[-1]
```

means:

> The last element of the list.

Suppose:

```python
result = ['a', 'b', 'c']
```

Then:

```python
result[-1]
```

is:

```text
c
```

So when the next character is `c`:

```python
if result[-1] != ch:
```

becomes:

```text
c != c
```

which is false.

Therefore we skip it.

---

# 8. Why `not result` Is Needed

Consider the first character.

Initially:

```python
result = []
```

There is no previous character.

Therefore this condition:

```python
if not result or result[-1] != ch:
```

handles two cases:

### Case 1 — Result is empty

```text
not result = True
```

So the first character is automatically added.

### Case 2 — Result is not empty

Then:

```text
result[-1] != ch
```

checks whether the current character differs from the last kept character.

---

# 9. Example 1

### Input

```text
aaabbccdaa
```

### Output

```text
abcda
```

---

# 10. Complete Dry Run

String:

```text
a a a b b c c d a a
```

Initially:

```text
result = []
```

---

### Step 1 — `a`

Result is empty.

```text
Add a
```

```text
result = [a]
```

---

### Step 2 — `a`

Last kept character:

```text
a
```

Current:

```text
a
```

Comparison:

```text
a == a
```

Duplicate.

```text
Skip
```

Result:

```text
a
```

---

### Step 3 — `a`

Again:

```text
a == a
```

Skip.

Result:

```text
a
```

---

### Step 4 — `b`

Compare:

```text
b != a
```

Different.

Add:

```text
ab
```

---

### Step 5 — `b`

```text
b == b
```

Skip.

Result:

```text
ab
```

---

### Step 6 — `c`

```text
c != b
```

Add:

```text
abc
```

---

### Step 7 — `c`

```text
c == c
```

Skip.

---

### Step 8 — `d`

```text
d != c
```

Add:

```text
abcd
```

---

### Step 9 — `a`

```text
a != d
```

Add:

```text
abcda
```

---

### Step 10 — `a`

```text
a == a
```

Skip.

Final:

```text
abcda
```

---

# 11. Dry Run Table

| Step | Current | Last Kept | Action |  Result |
| ---: | :-----: | :-------: | :----: | :-----: |
|    1 |   `a`   |     —     |   Add  |   `a`   |
|    2 |   `a`   |    `a`    |  Skip  |   `a`   |
|    3 |   `a`   |    `a`    |  Skip  |   `a`   |
|    4 |   `b`   |    `a`    |   Add  |   `ab`  |
|    5 |   `b`   |    `b`    |  Skip  |   `ab`  |
|    6 |   `c`   |    `b`    |   Add  |  `abc`  |
|    7 |   `c`   |    `c`    |  Skip  |  `abc`  |
|    8 |   `d`   |    `c`    |   Add  |  `abcd` |
|    9 |   `a`   |    `d`    |   Add  | `abcda` |
|   10 |   `a`   |    `a`    |  Skip  | `abcda` |

Final:

```text
abcda
```

---

# 12. Example 2 — No Consecutive Duplicates

### Input

```text
abcdef
```

Every character is different from the previous one.

Therefore:

```text
Output:
abcdef
```

Nothing changes.

---

# 13. Example 3 — All Characters Same

### Input

```text
aaaaaaa
```

There is only one consecutive group:

```text
aaaaaaa
```

Compress it to:

```text
a
```

### Output

```text
a
```

---

# 14. Example 4 — Alternating Characters

### Input

```text
abababab
```

There are no adjacent duplicate characters.

Therefore:

```text
Output:
abababab
```

This is an important test case.

It proves that we are **not removing duplicates globally**.

---

# 15. Example 5 — Repeated Characters Separated

Consider:

```text
abca
```

The character `a` appears twice.

But:

```text
a
```

and:

```text
a
```

are not adjacent.

Therefore:

```text
Output:
abca
```

This is **not**:

```text
abc
```

---

# 16. Example 6 — Case Sensitivity

Input:

```text
aAAbbB
```

Python treats:

```text
a
```

and:

```text
A
```

as different characters.

Therefore the consecutive groups are:

```text
a
AA
bb
B
```

Result:

```text
aAbB
```

unless the problem explicitly says to ignore case.

If case should be ignored, then you would first normalize the input:

```python
s = s.lower()
```

Only do this when the problem requires case-insensitive processing.

---

# 17. Why Not Use a Set?

A set removes **global duplicates**.

For example:

```python
set("abca")
```

contains:

```text
a
b
c
```

But the correct answer for consecutive duplicate removal is:

```text
abca
```

Therefore:

```text
Set
↓
Global uniqueness
```

is the wrong pattern.

The correct pattern is:

```text
Previous-character comparison
↓
Adjacent uniqueness
```

---

# 18. Consecutive vs Global Duplicate Removal

This is the most important TCS trap.

## Problem A — Remove Consecutive Duplicates

```text
aaabbcc
↓
abc
```

Pattern:

```text
Previous Character Comparison
```

---

## Problem B — Remove All Duplicate Characters

```text
abca
↓
abc
```

Pattern:

```text
Hashing / Set
```

---

## Problem C — Remove Duplicates From Sorted Array

```text
1 1 2 2 3
↓
1 2 3
```

Pattern:

```text
Two Pointers
```

These problems look similar but require different patterns.

---

# 19. Why Not Use `replace()` Repeatedly?

You might try:

```python
while "aa" in s:
    s = s.replace("aa", "a")
```

This can work for simple examples, but it is not the pattern you should learn.

It repeatedly searches and modifies the string.

The direct traversal is:

```text
Simpler
+
Clearer
+
Predictable
```

Use:

```text
Current vs Previous
```

instead.

---

# 20. Complexity

We scan the string exactly once.

Therefore:

```text
Time Complexity = O(N)
```

The result can contain up to `N` characters.

Therefore:

```text
Space Complexity = O(N)
```

### Final:

```text
Time:  O(N)
Space: O(N)
```

If the output string is excluded from auxiliary-space analysis, the algorithm needs only constant extra state beyond the result.

---

# 21. 🧠 Pattern Recognition Shortcut

When you see:

```text
REMOVE
+
CONSECUTIVE / ADJACENT
+
DUPLICATES
```

immediately think:

# **COMPARE CURRENT WITH PREVIOUS**

Mental model:

```text
Current Character
       ↓
Compare with Previous
       ↓
   Same?
   ↙   ↘
 YES    NO
  ↓      ↓
Skip    Keep
```

---

# 22. Core Code to Remember

Memorize this:

```python
result = []

for ch in s:
    if not result or result[-1] != ch:
        result.append(ch)

print("".join(result))
```

That's the entire pattern.

---

# 23. Alternative Approach — Compare With `s[i-1]`

You can also solve it using indexes:

```python
s = input().strip()

result = []

for i in range(len(s)):
    if i == 0 or s[i] != s[i - 1]:
        result.append(s[i])

print("".join(result))
```

This is also `O(N)`.

### Which version is easier?

For TCS NQT, both are valid.

The `result[-1]` version is particularly useful because it directly expresses:

> **Keep the current character if it differs from the last character already kept.**

---

# 24. When the `result[-1]` Version Is Better

Consider:

```text
aaabbbccca
```

Suppose we have already compressed:

```text
abc
```

Now the next character is `a`.

We compare:

```text
result[-1] = c
```

with:

```text
ch = a
```

Since:

```text
c != a
```

we keep it:

```text
abca
```

This naturally handles transitions between groups.

---

# 25. TCS Variations

TCS can easily modify this pattern.

## Variation 1 — Remove Consecutive Duplicates

```text
aaabb
↓
ab
```

---

## Variation 2 — Count Consecutive Groups

Example:

```text
aaabbcc
```

Groups:

```text
aaa
bb
cc
```

Therefore:

```text
3 groups
```

Pattern:

```text
Previous Character Comparison
```

---

## Variation 3 — Find Longest Consecutive Run

Example:

```text
aaabbbbcc
```

Runs:

```text
aaa      → 3
bbbb     → 4
cc       → 2
```

Answer:

```text
4
```

Again, compare the current character with the previous character and maintain a run length.

---

## Variation 4 — Character Compression

Example:

```text
aaabbc
```

Output:

```text
a3b2c1
```

The same consecutive-group traversal can identify:

```text
character + count
```

---

# 26. Pattern Family

```text
STRING TRAVERSAL
│
├── Remove Consecutive Duplicates
│
├── Count Consecutive Groups
│
├── Longest Consecutive Run
│
├── Run-Length Encoding
│
└── Character Compression
```

The common idea is:

```text
Compare Current
with Previous
```

---

# 27. Edge Cases

Always test these.

### Empty string

```text
""
```

Expected result:

```text
""
```

if empty input is allowed.

---

### One character

```text
"a"
```

Result:

```text
"a"
```

---

### All same

```text
"aaaaa"
```

Result:

```text
"a"
```

---

### No duplicates

```text
"abcdef"
```

Result:

```text
"abcdef"
```

---

### Alternating

```text
"abababab"
```

Result:

```text
"abababab"
```

---

### Duplicate separated

```text
"abca"
```

Result:

```text
"abca"
```

---

### Mixed groups

```text
"aaabbccdaa"
```

Result:

```text
"abcda"
```

---

# 28. ⚠️ Common Mistakes

## Mistake 1 — Using a Set

Wrong because a set removes global duplicates.

---

## Mistake 2 — Removing every repeated character

For:

```text
abca
```

the answer is:

```text
abca
```

not:

```text
abc
```

---

## Mistake 3 — Comparing with the wrong character

You only care about the **immediately previous character**.

```text
current
   ↓
previous
```

Not:

```text
current
   ↓
anywhere earlier in the string
```

---

## Mistake 4 — Forgetting the first character

The first character has no previous character.

That's why:

```python
not result
```

is included.

---

# 29. Quick Revision

Before the exam, remember:

```text
Problem:
Remove consecutive duplicates

Keyword:
CONSECUTIVE / ADJACENT

Pattern:
String Traversal

Comparison:
Current vs Previous

Same:
Skip

Different:
Keep

Time:
O(N)

Space:
O(N)
```

---

# 🧠 30. Final Memory Trick

Memorize:

```text
CONSECUTIVE DUPLICATES
          ↓
CURRENT vs PREVIOUS
          ↓
       SAME?
       ↙   ↘
     YES    NO
      ↓      ↓
    SKIP    KEEP
          ↓
        RESULT
```

### One-line exam rule:

> **If duplicates must be removed only when they are adjacent → compare the current character with the previous character.**

---

# 🚀 31. Final Takeaway

The important thing about this problem is recognizing that **consecutive** changes everything.

Compare:

```text
aaabbcc
```

Here duplicates are adjacent:

```text
aaa
bb
cc
```

So:

```text
abc
```

But:

```text
abca
```

contains a repeated `a`, but the two `a`s are separated.

Therefore:

```text
abca
```

remains unchanged.

So the real pattern is:

```text
CONSECUTIVE
     ↓
ADJACENT
     ↓
CURRENT + PREVIOUS
     ↓
SAME → SKIP
DIFFERENT → KEEP
```

> ### 🔥 TCS NQT Memory Formula
>
> **`CONSECUTIVE DUPLICATES → CURRENT vs PREVIOUS → SAME = SKIP → DIFFERENT = KEEP`**
