## HW 3 - Building a Water Supply System

## Problem Statement
In ByteLand, a severe earthquake has destroyed all roads and wells, cutting off access to water for many villages. The government plans to rebuild some roads and wells to ensure that every village can access at least one functional well.

Given the cost of rebuilding each road and well, the task is to compute the minimum cost required to restore connectivity so that every village can reach at least one well.

## Input Format
The input consists of multiple test instances.
- The first line contains an integer C representing the number of test instances.
- For each test instance, The first line contains two integers n and m, where:
  - n is the number of villages.
  - m is the number of roads.
- The second line contains n space-separated integers w1, w2, ..., wn:
  - If wi is positive, it represents the cost to rebuild a well in village i.
  - If wi = -1, there was no well in village i before the earthquake.
- The next m lines contain three integers u, v, c:
  - u and v represent the villages connected by a road.
  - c is the cost to rebuild the road between these villages.

## Output Format
For each test instance, print a single integer representing the minimum cost required to reconstruct the water supply system.


## Example Input/Output
### Input
```bash
3
8 10
20 10 -1 -1 -1 -1 15 90
2 1 25
1 6 25
7 8 30
8 3 15
5 3 40
1 4 90
1 7 30
6 2 25
6 7 5
3 1 5
6 5
1 -1 -1 -1 -1 -1
1 2 1000000000
3 1 1000000000
1 4 1000000000
4 5 1000000000
6 5 1000000000
1 0
1
```

### Output
```bash
200
5000000001
1
```

## Constraints
1. 1 ≤ n ≤ 10^5.
2. m ≤ 4 ≤ 10^5.
3. Cost of rebuilding a road or well is a positive integer ≤10^9.
4. The total number of roads across all test instances is at most 4 * 10^5.
5. The output may be as large as n * 10^9,  so a 64-bit integer type should be used.

## Dependencies
- Python 3.x (or C++/C compiler if applicable)

