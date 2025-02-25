# This function helps to find the representative (root) of the set containing node u using path compression.
# Path compression ensures that all nodes directly point to the root of their set, which optimizes future find operations to nearly constant time O(α(n)).
def find(parent, u):
    """Find with path compression."""
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

# This function unites two sets by connecting the root of one set to the root of another.
#  Uses union by rank to keep the tree shallow, improving efficiency.
def union(parent, rank, u, v):
    """Union by rank."""
    rootU = find(parent, u)
    rootV = find(parent, v)
    if rootU != rootV: #only merge if they are in different sets
        if rank[rootU] > rank[rootV]:
            parent[rootV] = rootU
        elif rank[rootU] < rank[rootV]:
            parent[rootU] = rootV
        else:
            parent[rootV] = rootU
            rank[rootU] += 1
        return True # if the union was successful
    return False

# This function computes the minimum cost to rebuild ByteLand's water supply system using a Minimum Spanning Tree (MST) approach with Kruskal’s algorithm.
    # The problem is modeled as a graph where:
    # - Villages are nodes.
    # - Roads are edges with given reconstruction costs.
    # - Wells are treated as edges connecting villages to a virtual node (node 0).
def computeMinimumCost(weights, edges):
    """Computes the minimum cost to rebuild ByteLand's water supply system."""
    n = len(weights) - 1  # Number of villages
    m = len(edges)  # Number of roads
    
    # Initialize Disjoint Set Union (DSU) structures
    parent = list(range(n + 1))  # +1 for virtual node 0
    rank = [0] * (n + 1)

    # Convert wells into edges (cost, 0, village)
    well_edges = [(weights[i], 0, i) for i in range(1, n + 1) if weights[i] > 0]

    # Combine road and well edges
    all_edges = [(w, u, v) for u, v, w in edges] + well_edges

    # Sort all edges by cost (because Kruskal's algorithm requires sorted edges)
    all_edges.sort()
    
    cost = 0 # Tracks total minimum cost
    edges_used = 0 # Number of edges added to the MST

    # This loop implements Kruskal’s Algorithm to build the Minimum Spanning Tree (MST)
    for w, u, v in all_edges:
        if union(parent, rank, u, v):
            cost += w
            edges_used += 1
            if edges_used == n: 
                break # Stop early once all villages are connected

    return cost # Return the minimum reconstruction cost

T = int(input()) # Read the number of test cases

# This function processes each test case
for _ in range(T):
    n, m = map(int, input().split()) # Reads the number of villages (n) and roads (m)
    weights = list(map(int, ("0 " + input()).split())) 

    edges = []
    # Reads all road connections and their reconstruction costs
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    print(computeMinimumCost(weights, edges)) #calls the function to  compute and print the minimum reconstruction cost for this test case