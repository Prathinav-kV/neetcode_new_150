---
name: complexity-audit
description: Quick self-audit checklist for time and space complexity of a solution the user just wrote, before requesting a full review. Use when the user asks "what's the Big-O of this" or wants a fast complexity gut-check on a file or snippet.
---

Walk the user's code structurally to derive complexity — don't guess, derive it from control flow.

## Time complexity

1. Count nested loop depth over the input — each independent nested loop over n multiplies (loop over n inside loop over n → O(n²)), sequential (non-nested) loops add, so O(n) + O(n) = O(n), not O(n²).
2. Check what each loop iterates over — the input size, a fixed range, or a shrinking window? A two-pointer/sliding-window pattern with pointers that only move forward is O(n) total even though it looks like nested loops.
3. Check for hidden costs inside a loop — `list.pop(0)`, `x in list`, string concatenation in a loop, sorting inside a loop — these silently add a multiplier (O(n) each) to whatever the surrounding loop's complexity is.
4. Recursion — express as a recurrence (calls per invocation × work per call, and depth), e.g. binary recursion with no memoization over n often gives O(2^n); with memoization, gives O(n) or O(n × state space).
5. Sorting anywhere in the function sets a floor of O(n log n) regardless of the rest.

## Space complexity

1. Count extra data structures sized relative to input (hashmap/set/list proportional to n) — that's O(n) space, separate from the input itself.
2. Recursion depth counts as space (call stack) — O(depth), not O(1), even if no explicit extra structure is allocated.
3. In-place modification of the input (two pointers swapping within the given array) is O(1) extra space — don't count the input itself.

## Output

State it as:

```
Time: O(...) — <which loop/recursion drives this>
Space: O(...) — <what structure or call stack drives this>
```

If the user's stated complexity doesn't match what you derive, point at the specific line causing the mismatch rather than just asserting the correct answer.
