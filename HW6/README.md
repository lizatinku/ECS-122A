# HW6 - Radio Towers Yet Again 📡

## Problem Statement

In ByteLand, there are n cities positioned along the x-axis at coordinates A₁, A₂, ..., Aₙ. A telecom company wants to place radio towers, each with a fixed coverage radius d, at specific possible locations B₁, B₂, ..., Bₘ. Each tower at position y covers a city at position x if |x - y| ≤ d.
The goal is to find, for each k (1 ≤ k ≤ m), how many ways we can place exactly k towers such that:
- Every city is covered by exactly one tower.
- Towers are placed only at the provided candidate locations.
- No city is covered by more than one tower.


## Input Format

Each test case consists of:
- An integer C: number of test instances.
- For each test instance:
  - Line 1: Three integers n, m, d — number of cities, number of potential tower locations, and coverage radius.
  - Line 2: n sorted integers: A₁, A₂, ..., Aₙ — positions of cities.
  - Line 3: m sorted integers: B₁, B₂, ..., Bₘ — potential tower positions.


## Output Format
- For each test instance, print a line of m space-separated integers.
- The k-th integer (1-indexed) should represent the number of valid tower placements using exactly k towers such that each city is covered uniquely by a tower.
- Since answers may be large, return each modulo 10⁹ + 7.


## Example Input/Output

### Input

```bash
2
5 5 1
1 2 3 4 5
1 2 3 4 5
60 60 2
1 2 3 8 9 10 15 ... 65
66 71 72 73 ... 136
```

### Output

```bash
0 2 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 486784380 0 0 ...
```

## Constraints
1. 1 ≤ n ≤ 10⁵, 1 ≤ m ≤ 1200
2. 0 ≤ Aᵢ, Bⱼ ≤ 10⁹
3. Arrays A and B are strictly increasing.
4. Up to 10 test instances per file.
5. Total cities across test cases ≤ 2 × 10⁵

## Approach & Solution
My solution uses a combination of:

- ✅Binary Search: To quickly identify ranges of cities that can be covered by a tower.
- ✅Dynamic Programming (DP): A 2D DP table is maintained where dp[i][k] represents the number of ways to place k towers such that the rightmost tower is at B[i] and all cities left of B[i] are uniquely covered.
- ✅Prefix Sums: For efficient computation of range sums in the DP state transitions.
- ✅Modular Arithmetic: All calculations are performed under modulo 10⁹ + 7 using a custom class to avoid overflow.
