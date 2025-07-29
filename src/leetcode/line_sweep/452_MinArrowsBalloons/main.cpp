// 452. Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        return -1;
    }
};

int main() {
    Solution* sol = new Solution();

    vector<vector<int>> points;

    {
        points = { { 10, 16 }, { 2, 8 }, { 1, 6 }, { 7, 12 } };
        cout << sol->findMinArrowShots(points) << endl;
    }
    {
        points = { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };
        cout << sol->findMinArrowShots(points) << endl;
    }
    {
        points = { { 1, 2 }, { 2, 3 }, { 3, 4 }, { 4, 5 } };
        cout << sol->findMinArrowShots(points) << endl;
    }

    delete sol;
}
