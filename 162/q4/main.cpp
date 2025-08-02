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
