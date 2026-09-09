# 🔥 1. Subarray With Given Sum

> **Pattern:** Prefix Sum + Hashing  
> **Difficulty:** Medium  
> **Time Complexity:** O(N)  
> **Space Complexity:** O(N)

---

## 📌 Problem Name

### Subarray With Given Sum

---

## 📝 Problem Statement

Given an array of integers and a target sum `K`, find a **contiguous subarray** whose elements add up to `K`.

Return the **starting and ending indices** of the first such subarray.

If no such subarray exists, print `-1`.

---

# 🧠 1. Pattern Used

## Prefix Sum + Hashing

The key idea is:

```text
Current Prefix Sum - Previous Prefix Sum = Subarray Sum