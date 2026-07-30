---
name: pattern-id
description: Walks through identifying which DSA pattern (two pointers, sliding window, monotonic stack, hashmap, etc.) a new/unseen problem statement belongs to, before any code is written. Use when the user pastes a problem statement and wants help recognizing the category — the transferable skill for novel interview questions, not a solve-it-for-me shortcut.
---

Given a problem statement, work through this checklist out loud with the user — ask, don't tell, wherever possible. The goal is training their own pattern recognition, so lead with questions before naming a pattern.

## Step 1 — Extract signal from the problem shape

Ask / identify:
- Is the input an array/string that's **sorted** or **can be sorted**? → hints at two pointers or binary search.
- Does the problem involve a **contiguous subarray/substring** with a size/sum/condition? → sliding window.
- Does it ask for **next/previous greater or smaller element**, or involves comparing each element to ones before/after it in a stack-like order? → monotonic stack.
- Does it involve **counting, grouping, or fast lookup** (duplicates, complements, frequency)? → hashmap/hashset.
- Does it involve a **graph or tree structure**, explicit or implied (adjacency, grid, connections)? → BFS/DFS/Union-Find.
- Does it ask for **top-K, k-th largest/smallest, or merging sorted structures**? → heap.
- Does it have **overlapping subproblems** or "number of ways to..." phrasing? → dynamic programming.
- Does it involve **intervals** (merge, overlap, insert)? → sort + sweep.

## Step 2 — Confirm with constraints

Check the stated input size / time limit if given:
- n ≤ ~20 → brute force / backtracking may be intended.
- n ≤ ~10^4-10^5 with O(n log n) expected → sort-based or heap approach likely.
- n ≤ ~10^6+ → needs O(n) or O(n log n), rules out anything quadratic.

## Step 3 — Cross-check against prior work

Use Read/Grep on this repo's topic folders (`Arrays and Hashing`, `Sliding Window`, `Stack`, `Two Pointers`, etc.) to find a previously solved problem with a similar shape, and ask the user how this new problem is similar/different — reinforces transfer rather than rote memorization.

## Step 4 — Only then, name it

State the pattern explicitly and have the user articulate *why* it fits, in one sentence, before moving to implementation (hand off to `dsa-tutor` agent if they want hint-based guidance while coding).

## Anti-pattern to avoid

Don't jump straight to "this is a sliding window problem" as the first sentence. The point of this skill is the diagnostic process, not the label.
