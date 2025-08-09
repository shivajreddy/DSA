// 646. Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {

        // sorting by end link, so that we greedily always use the link that
        // ends before the next link end.
        sort(pairs.begin(), pairs.end(),
             [&](const vector<int>& a, const vector<int>& b) {
                 return a[1] < b[1];
             });

        int n = pairs.size();
        int links = 1;
        int prev_end = pairs[0][1];
        for (int i = 1; i < n; i++) {
            int curr_start = pairs[i][0], curr_end = pairs[i][1];
            // case1: curr_start over laps with previous links end
            if (prev_end >= curr_start) {
                // we dont use the current link
            } else { // case2: there is no overlap, consider this link
                links++;
                prev_end = curr_end;
            }
        }
        return links;
    }
};

int main() {
    Solution* sol = new Solution();

    vector<vector<int>> pairs;

    {
        pairs = { { 1, 2 }, { 2, 3 }, { 3, 4 } };
        cout << sol->findLongestChain(pairs) << endl;
    }
    {
        pairs = { { 1, 2 }, { 7, 8 }, { 4, 5 } };
        cout << sol->findLongestChain(pairs) << endl;
    }

    delete sol;
}
