// 1893. Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {

        int n = ranges.size();

        sort(ranges.begin(), ranges.end());

        int left_most = ranges[0][0];
        int right_most = ranges[0][1];

        for (int i = 1; i < n; i++) {
            if (ranges[i][0] > right_most + 1) { // gap
                if (left >= left_most && right <= right_most) {
                    return true;
                } else {
                    left_most = ranges[i][0];
                    right_most = ranges[i][1];
                }
            }
            if (ranges[i][1] > right_most) right_most = ranges[i][1];
        }

        if (left >= left_most && right <= right_most) {
            return true;
        } else {
            return false;
        }
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
    {
        ranges = { { 3, 3 }, { 1, 1 } };
        left = 3, right = 3;
        cout << sol->isCovered(ranges, left, right) << endl;
    }

    delete sol;
}
