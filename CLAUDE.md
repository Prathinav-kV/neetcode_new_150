# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Personal collection of solved NeetCode 150 problems in Python, organized by topic. Each problem is a standalone `.py` file — there is no shared package, build system, test suite, or dependency manifest.

## Running a solution

There is no test runner or entry-point script. Run a file directly:

```
python "Stack/carFleet.py"
```

Files with a `main()` guarded by `if __name__ == "__main__":` (e.g. `Stack/carFleet.py`) print a result for a hardcoded sample input when run directly. Older/other files just define the `Solution` class with no runnable driver — to exercise them, add a temporary call or use the Python REPL.

## Conventions used across files

- Each file defines one `class Solution` with the method(s) matching the LeetCode/NeetCode signature (e.g. `def twoSum(self, nums: List[int], target: int) -> List[int]:`).
- `from typing import List` is used for type hints where needed; typing imports are not always present in older files — check before assuming `List`/`Optional` are in scope.
- A few files (e.g. `Arrays and Hashing/twoSum.py`) keep multiple attempts in one file (a brute-force `Solution` followed by a `# FASTEST SOLUTION` class redefinition). This is intentional — it's a record of iterating toward an optimal solution, not dead code to clean up.
- Solutions favor concise, minimal implementations without added error handling, docstrings, or comments beyond what's needed to mark alternate attempts.

## Directory layout

Folders group problems by NeetCode topic/pattern (`Arrays and Hashing`, `Sliding Window`, `Stack`, `Two Pointers`). New solutions should go in the folder matching their pattern, following the existing filename style (camelCase, matching the problem name).
