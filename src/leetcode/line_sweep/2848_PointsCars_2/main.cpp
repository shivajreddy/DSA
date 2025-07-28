// 2848. Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars

#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    int numberOfPoints(vector<vector<int>>& nums) {

        int n = nums.size();

        sort(nums.begin(), nums.end());

        int res = 0;

        int left_most, right_most;

        left_most = nums[0][0], right_most = nums[0][1];
        for (int i = 1; i < n; i++) {
            if (nums[i][0] > right_most + 1) {
                res += (right_most - left_most + 1);
                left_most = nums[i][0], right_most = nums[i][1];
            } else {
                right_most = max(right_most, nums[i][1]);
            }
        }
        res += (right_most - left_most + 1);

        return res;
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
