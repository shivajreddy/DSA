// 1893. Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        return false;
    }
};

int main() {
    Solution* sol = new Solution();
    vector<vector<int>> ranges;
    int left, right;

    {
        ranges = { { 1, 2 }, { 3, 4 }, { 5, 6 } };
        left = 2, right = 5;
        cout << sol->isCovered(ranges, left, right) << endl;
    }
    {
        ranges = { { 1, 10 }, { 10, 20 } };
        left = 21, right = 21;
        cout << sol->isCovered(ranges, left, right) << endl;
    }

    delete sol;
}
