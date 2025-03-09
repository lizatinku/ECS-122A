# HW5 - Finding a House in ByteLand 🏡

## Problem Statement

ByteLand has been redesigned into a grid of R × C cells, where ADA, a little girl, wants to reach her home at the bottom-right cell as fast as possible. However, there are various types of terrain that affect movement:

- Empty cells (1) allow movement in 1 second.
- Muddy cells (2-5) take 2 to 5 seconds to traverse.
- Rocky cells (0) cannot be traversed.
- Teleportation cells (-1) allow instant movement to specific cells.
- Spiky cells (-2) can only be crossed a limited number of times (H).

The goal is to compute the minimum time required for ADA to reach each cell from the starting position (1,1), or -1 if the cell is unreachable.

## Input Format

The input consists of multiple test instances:

- The first line contains an integer T, the number of test cases.
- For each test case, The first line contains three integers:
- - R → Number of rows.
- - C → Number of columns.
- - H → Maximum number of spiky cells ADA can walk over.
- The next R lines each contain C integers, representing the grid:
- - 1 → Empty cell (1-second movement).
- - 0 → Rocky cell (impassable).
- - 2-5 → Muddy cell (movement takes grid[i][j] seconds).
- - 1 → Teleportation cell.
- - 2 → Spiky cell (can only be crossed H times).

## Output Format

For each test case, print an R × C matrix, where result[i][j] represents the minimum time to reach cell (i, j) from (1,1).

- If a cell cannot be reached, print -1.

## Example Input/Output

### Input

```bash
6
2 5 0
1 0 1 1 1
1 1 1 0 1
2 5 0
1 5 1 1 1
1 1 1 5 1
2 5 1
1 -2 5 1 1
3 -2 1 -2 1
2 5 2
1 -2 5 1 1
3 -2 1 -2 1
2 5 0
1 2 -1 0 -1
1 1 1 5 1
3 5 0
1 2 -1 0 -1
5 5 5 0 0
5 5 5 5 1
```

### Output

```bash
0 -1 4 5 6
1 2 3 -1 7
0 5 4 5 6
1 2 3 8 7
3
0 1 6 7 8
3 4 5 -1 9
0 1 6 7 8
3 2 3 6 7
0 2 3 -1 4
1 2 3 8 5
0 2 3 -1 4
5 7 8 -1 -1
10 12 13 18 19
```

## Constraints

1. 1 ≤ R, C ≤ 1000
2. 0 ≤ H ≤ 10
3. The total number of cells across all instances is at most 4 × 10⁶
4. Time Limit: 3 seconds (C/C++), 5 seconds (Python)

## Approach & Solution

This problem is solved using Dijkstra’s Algorithm with a priority queue (heapq) to handle weighted grid traversal efficiently.

- ✅ Initialize a 3D distance matrix result[r][c][spiky_count] to store the minimum time for each cell, keeping track of the number of spiky cells stepped on.
- ✅ Use a priority queue (heapq) to process the shortest paths first (Dijkstra's strategy).
- ✅ Handle teleportation cells efficiently by precomputing the leftmost/rightmost/topmost/bottommost teleport destinations.
- ✅ Ensure spiky cell constraints by maintaining a count of spiky steps used.
- ✅ Process muddy cells with their specific weight (2-5).
