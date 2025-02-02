# HW1 - Radio Tower Coverage

## Problem Statement
In ByteLand, there are n cities located along the x-axis. A telecommunications company installs radio towers to provide coverage to cities within a certain distance d.

This program determines:
1. How many cities a tower can cover if placed at each city’s location.
2. The maximum number of cities a single tower can cover when placed optimally along the x-axis.

## Input Format
- The first line contains two integers, n (number of cities) and d (coverage distance).
- The second line contains n space-separated integers representing city locations (A1, A2, ..., An), given in increasing order.

## Output Format
Print n lines, where each line represents the number of cities covered if the tower is placed at city Ai.
Print 1 additional line showing the maximum number of cities a single tower can cover.

## Example Input/Output
### Input
```bash
4 3
1 3 5 7
```

### Output
```bash
2
3
3
2
4
```

## Dependencies
- Python 3.x (or C++/C compiler if applicable)
- No additional libraries required.
