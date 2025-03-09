import heapq

def find_fastest_path(R, C, H, grid):
    INF = float('inf')
    result = []
    for _ in range(R):
        row = []
        for _ in range(C):
            row.append([INF] * (H + 1))
        result.append(row)
    
    rows_portable = {}
    cols_portable = {}

    # This nested for loop iterates through every row and column in the grid to check for teleportation cells(-1)
    for r in range(R):
        for c in range(C): 
            if grid[r][c] == -1:

                # If the algorithm finds a teleportable cell in a column, it will initialize a list
                if c not in cols_portable:
                    cols_portable[c] = []
                if r not in rows_portable:   # If the algorithm finds a teleportable cell in a row, it will initialize a list
                    rows_portable[r] = []

                cols_portable[c].append(r)  # Stores the row index of this teleport cell in the corresponding column list
                rows_portable[r].append(c) # Stores the column index of this teleport cell in the corresponding row list

    # After getting the teleportable cells, it sorts them in ascending order
    for key in cols_portable:
        cols_portable[key].sort()
    for key in rows_portable:
        rows_portable[key].sort()

    pq = [(0, 0, 0, 0)]  # Start at location (0, 0) with time = 0 and spiky count = 0
    result[0][0][0] = 0  # Mark the starting position with shortest time of 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Defining the possible directions which is right, down, left and up 

    # This whole while loop is the main part of the algorithm. 
    # It considers teleportation, muddy terrain, and rock obstacles before making a decision to move for ADA.
    while pq:
        t, r, c, count_spikes = heapq.heappop(pq)

        if t > result[r][c][count_spikes]:
            continue

        # Teleportation Handling
        if grid[r][c] == -1:
            if c in cols_portable:

                # This condition checks if a teleport cell exists above in the same column and moves ADA to the highest available teleport cell.
                if cols_portable[c][0] != r:  
                    nr = cols_portable[c][0]
                    if t + 1 < result[nr][c][count_spikes]:
                        result[nr][c][count_spikes] = t + 1
                        heapq.heappush(pq, (t + 1, nr, c, count_spikes))
                
                # This condition deals with a teleport cell below in the same column. It moves ADA to the lowest available one.
                if cols_portable[c][-1] != r:  
                    nr = cols_portable[c][-1]
                    if t + 1 < result[nr][c][count_spikes]:
                        result[nr][c][count_spikes] = t + 1
                        heapq.heappush(pq, (t + 1, nr, c, count_spikes))

            if r in rows_portable:
                # If there's a teleport cell to the left in the same row, ADA will be moved to the leftmost available one.
                if rows_portable[r][0] != c:  
                    nc = rows_portable[r][0]
                    if t + 1 < result[r][nc][count_spikes]:
                        result[r][nc][count_spikes] = t + 1
                        heapq.heappush(pq, (t + 1, r, nc, count_spikes))

                # If there's a teleport cell to the right in the same row, ADA will be moved to the rightmost available one.
                if rows_portable[r][-1] != c:  
                    nc = rows_portable[r][-1]
                    if t + 1 < result[r][nc][count_spikes]:
                        result[r][nc][count_spikes] = t + 1
                        heapq.heappush(pq, (t + 1, r, nc, count_spikes))

        # This for loop deals with the spiky cells. When ADA lands on one, it increments the spiky count.
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # If the next cell is spiky, increase the spiky count; otherwise, keep it the same.
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 0: 
                new_spiky_count = count_spikes + 1 if grid[nr][nc] == -2 else count_spikes
                cost = grid[nr][nc] if 2 <= grid[nr][nc] <= 5 else 1  
                new_t = t + cost
                
                # This if statement ensures that ADA does not exceed the spiky cell limit and only updates if this path is faster.
                if new_spiky_count <= H and new_t < result[nr][nc][new_spiky_count]:
                    result[nr][nc][new_spiky_count] = new_t
                    heapq.heappush(pq, (new_t, nr, nc, new_spiky_count))

    # Initialize the output matrix with -1 (default value for unreachable cells)
    output = []
    for _ in range(R):
        row = []
        for _ in range(C):
            row.append(-1)  # Default value is -1
        output.append(row)

    # This for loop iterates through each cell in the grid, finds the shortest time to reach it.
    for r in range(R):
        for c in range(C):
            min_time = min(result[r][c])  # Get the minimum time to reach this cell across all spiky counts
            if min_time != INF:  
                output[r][c] = min_time  
            else:  
                output[r][c] = -1  # If unreachable, keep -1
    
    return output

T = int(input())
for _ in range(T):
    R, C, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]
    result = find_fastest_path(R, C, H, grid)

    for row in result:
        print(*row, sep=' ')
