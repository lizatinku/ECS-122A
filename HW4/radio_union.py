# P → List of percentages (coverage strength of each city).
# A → List of city positions.
# k → Number of towers available.

def compute_min_radius(P, A, k):
    n = len(A)

    if k >= n:
        return 0  

    def can_cover(radius):
        towers_used = 0
        i = 0  

        while i < n:
            towers_used += 1  # Place a tower

            if towers_used > k:
                return False  # if exceeded allowed towers

            best_tower = i
            while best_tower < n and A[best_tower] - A[i] <= (radius * P[best_tower]) // 100:
                best_tower += 1  # Move forward to the best possible tower

            # This tower covers up to A[best_tower - 1] + its reach
            coverage = A[best_tower - 1] + (radius * P[best_tower - 1]) // 100

            # Move i forward to the next uncovered city
            while i < n and A[i] <= coverage:
                i += 1  # Skip all covered cities

        return towers_used <= k  # Check if towers were enough

    # Binary search for the minimum radius
    low, high = 0, 10**9  
    ans = high  

    while low <= high:
        mid = (low + high) // 2
        if can_cover(mid):
            ans = mid
            high = mid - 1  # Try smaller radius
        else:
            low = mid + 1  # Increase radius

    return ans * 60  # Scale output


# Read input
tc = int(input())
results = []
for _ in range(tc):
    n, k = map(int, input().split())
    P = list(map(int, input().split()))
    A = list(map(int, input().split()))
    results.append(compute_min_radius(P, A, k))

# Print all results
for res in results:
    print(res)
