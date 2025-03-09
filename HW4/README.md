# HW4 - Radio Towers Again 📡

## Problem Statement
ByteLand has n cities positioned along the x-axis, with each city at coordinate Ai. A telecommunications company is tasked with rebuilding k radio towers after a tsunami destroyed all existing infrastructure. Each tower has a coverage radius d, but due to interference from buildings and terrain, a tower built at city i will only function at pi% of its expected range. This means that a tower placed at city i can provide service to all cities j such that:
| Ai - Aj | < d * (pi/100)
The company wants to minimize d while ensuring that all cities receive coverage using at most k towers.

## Input Format
The input consists of multiple test instances:

- The first line contains an integer C, the number of test cases.
- Each test case consists of:
- - Two integers: n → Number of cities and k → Maximum number of towers available
- - A line with n integers: p1, p2, ....pn -> coverage percentage of each city(multiples of 20)
- - A line with n integers: A1, A2,...An -> City positions(strictly increasing order)
 
## Output Format
For each test case, print a single integer, which is the minimum required coverage radius d multiplied by 60 to ensure that all cities are covered. If it's impossible to cover all cities with k towers, output -1.

## Example Input/Output
### Input
```bash
5
5 1
100 100 100 100 100
1 3 5 7 9
5 2
100 100 100 100 100
1 3 5 7 9
5 3
100 100 100 100 100
1 3 5 7 9
5 4
100 100 100 100 100
1 3 5 7 9
5 5
2
100 100 100 100 100
1 3 5 7 9
```


### Output
```bash
240
120
120
120
0
```

## Constraints
1. 1 ≤ k ≤ n ≤ 10⁵
2. pi ∈ {20, 40, 60, 80, 100}
3. 0 ≤ Ai ≤ 10^9
4. Total number of cities across all test cases ≤ 10⁵
5. Time Limits: C/C++: 4s, Python: 10s

## Approach & Solution
This problem can be efficiently solved using binary search and greedy placement of radio towers.

- ✅ Binary Search on d: We perform binary search on the minimum possible d. The search space for d is between 0 and 10⁹ (scaled by 60).

- ✅ Checking Coverage Feasibility
- Given a candidate d, we attempt to greedily place towers:
- - Start at the first city.
- - Place a tower that extends coverage as far as possible.
- - Move to the next uncovered city and repeat.
- - If more than k towers are needed, increase d.


- ✅ Optimizations
- Use integer-only calculations to prevent precision errors.
- Sort and preprocess city positions for efficient traversal.
- Use a priority queue or two-pointer technique for fast tower placement.
