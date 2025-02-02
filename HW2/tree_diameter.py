def bfs_farthest(node, graph):
    queue = [(node, 0)]  
    front = 0 
    visited = set([node])
    farthest_node, distance_max = node, 0

    # this while loop is used to process the nodes using BFS.  It simulates popping from the front of the queue.
    while front < len(queue):
        current, dist = queue[front]
        front += 1 

        # This if statement checks if we have found the largest distance so far.
        if dist > distance_max:
            farthest_node, distance_max = current, dist

        # This for loop iterates through all neighbors of the current node.
        # If a neighbor hasn't been visited, it marks it as visited and adds it to the queue.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

# Finally, it returns the farthest node along with the maximum distance to it.
    return farthest_node, distance_max


# The previous function was used to find the farthest node.
# This function calculates the diameter of the tree.
def compute_diameter(n, edges):
    if n == 1:
        return 0 

    # we create an adjancency list
    graph = {i: [] for i in range(1, n + 1)}

    # This for loop builds the graph by adding edges between nodes.
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    v, _ = bfs_farthest(1, graph) # calls the BFS function to find the farthest node from an arbitrary node
    _, diameter = bfs_farthest(v, graph) # calls the BFS function to find the farthest node from v

    return diameter

T = int(input())
for _ in range(T):
    n = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    print(compute_diameter(n, edges))
