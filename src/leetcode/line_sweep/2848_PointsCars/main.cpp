// 2848. Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars

#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    int numberOfPoints(vector<vector<int>>& nums) {
        return -1;
    }
};

int main() {
    Solution* sol = new Solution();
    vector<vector<int>> nums;

    {
        nums = { { 3, 6 }, { 1, 5 }, { 4, 7 } };
        cout << sol->numberOfPoints(nums) << endl;
    }
    {
        nums = { { 1, 3 }, { 5, 8 } };
        cout << sol->numberOfPoints(nums) << endl;
    }

    delete sol;
}
