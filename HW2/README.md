## HW2 - Diameter of a Tree

## Problem Statement
You are given a tree T with n vertices numbered 1, 2, ..., n. The diameter of a tree is the maximum distance among all pairs of vertices, where the distance is defined as the number of edges in the shortest path between two vertices.

This program determines the diameter of the given tree using an efficient approach.

### Hint
1. Start from an arbitrary vertex and find the farthest vertex v from it.
Then, find the farthest vertex w from v.
The diameter is the distance between v and w.
A Breadth-First Search (BFS) approach is recommended due to potential recursion depth issues with Depth-First Search (DFS).

## Input Format
Each input file contains multiple test instances.
- The first line contains a single integer C, representing the number of test instances.
- Each test instance consists of:
- - A single integer n (number of vertices in the tree).
- - n - 1 lines, each containing two space-separated integers u v, representing an edge between vertex u and vertex v.

## Output Format
For each test instance, print a single integer: the diameter of the tree.

### Input
```bash
4
8
1 2
3 1
4 3
1 6
7 5
5 1
4 8
5
3 1
1 2
5 4
4 2
4
2 1
2 3
2 4
2
1 2
```


## Output
```bash
5
4
2
1
```

## Constraints
- 1 ≤ C ≤ 1000 (number of test instances).
- Each tree has at least 2 vertices.
- The sum of sizes of all trees in a single file is at most 2 × 10⁵.
- The time limit is 1 second for C/C++ and 3 seconds for Python.

## Dependencies
Python 3.x (or C++/C compiler if applicable)
No additional libraries required.

