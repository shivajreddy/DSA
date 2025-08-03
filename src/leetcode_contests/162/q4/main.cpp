// Q4. Threshold Majority Queries
// https://leetcode.com/contest/biweekly-contest-162/problems/threshold-majority-queries/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

// Macro
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
#define vec vector

class Solution {
public:
    vector<int> subarrayMajority(vector<int>& nums,
                                 vector<vector<int>>& queries) {
        int n = nums.size();
        int q = queries.size();
        int blockSize = max(1, (int)sqrt(n));

        // Add index to queries for tracking original order
        vector<array<int, 4>> indexedQueries(q);
        for (int i = 0; i < q; i++) {
            indexedQueries[i] = { queries[i][0], queries[i][1], queries[i][2],
                                  i };
        }

        // Sort queries using Mo's algorithm ordering
        sort(indexedQueries.begin(), indexedQueries.end(),
             [&](const array<int, 4>& a, const array<int, 4>& b) {
                 int blockA = a[0] / blockSize;
                 int blockB = b[0] / blockSize;
                 if (blockA != blockB) return blockA < blockB;
                 // If in same block, sort by right endpoint
                 // Alternate direction for odd/even blocks to minimize movement
                 return (blockA & 1) ? (a[1] < b[1]) : (a[1] > b[1]);
             });

        // Process queries using Mo's algorithm
        vector<int> result(q);
        unordered_map<int, int> freq;
        int currL = 0, currR = -1;

        // Helper functions to add/remove elements
        auto add = [&](int pos) { freq[nums[pos]]++; };

        auto remove = [&](int pos) {
            freq[nums[pos]]--;
            if (freq[nums[pos]] == 0) {
                freq.erase(nums[pos]);
            }
        };

        // Process each query
        for (const auto& query : indexedQueries) {
            int l = query[0];
            int r = query[1];
            int threshold = query[2];
            int queryIdx = query[3];

            // Expand/shrink window to match current query
            while (currR < r) add(++currR);
            while (currL > l) add(--currL);
            while (currR > r) remove(currR--);
            while (currL < l) remove(currL++);

            // Find best element that meets threshold
            int bestElement = -1;
            int bestFreq = -1;

            for (const auto& [element, count] : freq) {
                if (count >= threshold) {
                    if (bestFreq == -1 || count > bestFreq ||
                        (count == bestFreq && element < bestElement)) {
                        bestElement = element;
                        bestFreq = count;
                    }
                }
            }

            result[queryIdx] = bestElement;
        }

        return result;
    }
};

class SolutionBruteforce {
public:
    vector<int> subarrayMajority(vector<int>& nums,
                                 vector<vector<int>>& queries) {
        vector<int> result;

        for (const auto& query : queries) {
            int l = query[0], r = query[1], threshold = query[2];

            // Count frequencies in the subarray
            unordered_map<int, int> freq;
            for (int i = l; i <= r; i++) freq[nums[i]]++;

            // Find the element with highest frequency that meets the threshold
            int best_element = -1, best_freq = -1;

            for (const auto& [element, count] : freq) {
                if (count >= threshold) {
                    // Update if we find a better candidate:
                    // - First time finding a valid element
                    // - Higher frequency than current best
                    // - Same frequency but smaller element value
                    if (best_freq == -1 || count > best_freq ||
                        (count == best_freq && element < best_element)) {
                        best_element = element;
                        best_freq = count;
                    }
                }
            }

            result.push_back(best_element);
        }

        return result;
    }
};

class Solution2 {
public:
    vector<int> subarrayMajority(vector<int>& nums,
                                 vector<vector<int>>& queries) {

        int n = nums.size();

        unordered_map<int, int> hm;
        vector<pair<int, int>> max_count(n);
        pair<int, int> prev_hi = { INT_MAX, 0 };
        for (int i = 0; i < n; i++) {
            hm[nums[i]]++;
            pair<int, int> curr = { nums[i], hm[nums[i]] };
            if (curr.second > prev_hi.second) {
                max_count[i] = curr;
                prev_hi = curr;
            } else if (curr.second == prev_hi.second &&
                       curr.first < prev_hi.first) {
                max_count[i] = curr;
                prev_hi = curr;
            }
        }

        vector<int> res;

        for (auto q : queries) {
        }

        return res;
    }
};

int main() {
    Solution* sol = new Solution();
    vector<int> nums;
    vector<vector<int>> queries;

    auto printv = [](vector<int> v) {
        for (int num : v) cout << num << " ";
        cout << endl;
    };

    {
        nums = { 1, 1, 2, 2, 1, 1 };
        queries = { { 0, 5, 4 }, { 0, 3, 3 }, { 2, 3, 2 } };
        cout << "RESULT: ";
        printv(sol->subarrayMajority(nums, queries));
        cout << "EXPECTED: " << "[1,-1,2]" << endl;
    }
    {
        nums = { 3, 2, 3, 2, 3, 2, 3 };
        queries = { { 0, 6, 4 }, { 1, 5, 2 }, { 2, 4, 1 }, { 3, 3, 1 } };
        cout << "RESULT: ";
        printv(sol->subarrayMajority(nums, queries));
        cout << "EXPECTED: " << "[3,2,3,2]" << endl;
    }
}
