// 646. Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        return -1;
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
