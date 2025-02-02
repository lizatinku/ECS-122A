def radio_tower_coverage(n, d, cities):
    results = []
    
    # Binary Search to find the leftmost index in the sorted cities
    def binary_search_left(i, d):
        low, high = 0, i
        while low < high:
            mid = (low + high) // 2
            if cities[i] - cities[mid] <= d:
                high = mid
            else:
                low = mid + 1
        return low
    
    # This function finds the rightmost index in the sorted cities array where the city at index i can still be covered by a tower placed at A[i]
    def binary_search_right(i, d):
        low, high = i, n - 1
        while low < high:
            mid = (low + high + 1) // 2
            if cities[mid] - cities[i] <= d:
                low = mid
            else:
                high = mid - 1
        return low

    #calling both functions
    for i in range(n):
        left = binary_search_left(i, d)
        right = binary_search_right(i, d)
        results.append(right - left + 1)
    
    max_coverage = 0
    left = 0
    
    for right in range(n):
        while cities[right] - cities[left] > 2 * d:
            left += 1
        max_coverage = max(max_coverage, right - left + 1)
    
    results.append(max_coverage)
    return results

n, d = map(int, input().split())
cities = list(map(int, input().split()))

results = radio_tower_coverage(n, d, cities)
for res in results:
    print(res)

