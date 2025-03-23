// Approach:
//  Binary Search: Used to efficiently determine valid tower placements.
//  Dynamic Programming (DP): Used to compute the number of ways to place towers while ensuring valid coverage without overlaps.
//  Modular Arithmetic: Since results can be large, all calculations are done 
//  modulo 10⁹ + 7 to prevent overflow.

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long MOD = 1000000007;

// This class is for modular arithmetic operations (+, -, *) under MOD.
class ModCalc {
public:
    long long val;

    ModCalc(long long v = 0) {
        val = v % MOD;
        if (val < 0) val += MOD;
    }

    ModCalc operator+(const ModCalc& other) const {
        return ModCalc(val + other.val);
    }

    ModCalc operator-(const ModCalc& other) const {
        return ModCalc(val - other.val);
    }

    ModCalc operator*(const ModCalc& other) const {
        return ModCalc(val * other.val);
    }
};

vector<ModCalc> Calculate_Coverage_Ways(vector<int> cities_a, vector<int> cities_b, int distance) {
    int len_a = cities_a.size();
    int len_b = cities_b.size();
    
    // Extend both city lists by adding a sentinel value to avoid boundary checks
    int extra = max(cities_a.back(), cities_b.back()) + distance + 1;
    cities_a.push_back(extra);
    cities_b.push_back(extra);
    len_a++;
    len_b++;
    
    // We have a DP table to store the number of valid ways to place towers
    vector<vector<ModCalc>> table(len_b, vector<ModCalc>(len_b + 1));
    
    // Prefix sum array for efficient range sum queries
    vector<vector<ModCalc>> prefix_sums(len_b, vector<ModCalc>(len_b + 1));

    // Initialize base case: ways to place 1 tower
    for (int i = 0; i < len_b; i++) {
        table[i][1] = ModCalc(cities_a[0] >= cities_b[i] - distance ? 1 : 0);
        prefix_sums[i][1] = (i > 0 ? prefix_sums[i - 1][1] : ModCalc(0)) + table[i][1];
    }

    // DP transition: compute ways to place multiple towers
    for (int j = 2; j <= len_b; j++) {
        for (int i = 0; i < len_b; i++) {
            // Find the farthest valid city in A that can contribute to B[i]
            int last_idx = lower_bound(cities_a.begin(), cities_a.end(), cities_b[i] - distance) - cities_a.begin() - 1;
            int next_idx = last_idx + 1;
            
            // Determine valid range [lower, upper] in B that can contribute to B[i]
            int lower = last_idx >= 0 ? lower_bound(cities_b.begin(), cities_b.end(), cities_a[last_idx] - distance) - cities_b.begin() : 0;
            int upper = lower_bound(cities_b.begin(), cities_b.end(), cities_a[next_idx] - distance) - cities_b.begin() - 1;
            
            // Ensure we don't exceed current index
            upper = min(upper, i - 1);

            // Compute DP state using prefix sum for efficient summation
            table[i][j] = (lower <= upper) ? prefix_sums[upper][j - 1] - (lower > 0 ? prefix_sums[lower - 1][j - 1] : ModCalc(0)) : ModCalc(0);
            prefix_sums[i][j] = (i > 0 ? prefix_sums[i - 1][j] : ModCalc(0)) + table[i][j];
        }
    }
    
    // Here, we are collecting results for valid placements with at least 2 towers
    vector<ModCalc> result;
    for (int j = 2; j <= len_b; j++) {
        result.push_back(table[len_b - 1][j]);
    }
    
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int test_count;
    cin >> test_count;
    
    while (test_count--) {
        int city_count_a, city_count_b, max_dist;
        cin >> city_count_a >> city_count_b >> max_dist;
        
        // Read input locations for both city sets
        vector<int> locations_a(city_count_a);
        for (int &x : locations_a) cin >> x;

        vector<int> locations_b(city_count_b);
        for (int &x : locations_b) cin >> x;

        // Compute the number of valid ways to place towers
        vector<ModCalc> solutions = Calculate_Coverage_Ways(locations_a, locations_b, max_dist);
        
        // Print results space-separated, handling last element correctly
        for (size_t i = 0; i < solutions.size(); i++) {
            cout << solutions[i].val << (i < solutions.size() - 1 ? " " : "\n");
        }
    }
    
    return 0;
}