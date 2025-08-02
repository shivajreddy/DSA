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

        for (auto q : queries) {
        }

        return {};
    }
};

int main() {
    Solution* sol = new Solution();

    {
    }
}
