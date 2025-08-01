// 452. Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {

        sort(points.begin(), points.end(),
             [&](const vector<int>& a, const vector<int>& b) {
                 return a[1] < b[1];
             });

        int n = points.size();
        // NOTE: taking INT_MIN would fail when interval starts at INT_MIN, so
        // use long long to track the previous shot end.
        // or start iterating from 1, and begin prev_shot_end as points[0][1]
        // and arrows count as 1
        long long prev_shot_end = -1e17; // arrow position
        int arrows = 0;
        for (int i = 0; i < n; i++) {
            int curr_start = points[i][0], curr_end = points[i][1];
            if (prev_shot_end < curr_start) { // no overlap
                //  so we need a new arrow for this
                arrows++;
                prev_shot_end = curr_end;
            } else {
                // currstart overlaps with previous shot
                // use the same arrow. no need to increase arrows or
                // update previous shot end
            }
        }

        return arrows;
    }
};

class SolutionMain {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(),
             [&](const vector<int>& a, const vector<int>& b) {
                 return a[1] < b[1];
             });

        int n = points.size();

        int arrows = 1;
        int prev_arrow_shot_at =
            points[0][1]; // shoot arrow at end of first baloon

        for (int i = 1; i < n; i++) {
            int curr_start = points[i][0], curr_end = points[i][1];
            if (prev_arrow_shot_at < curr_start) {
                // curr baloon starts after our arrow position, need new arrow
                arrows++;
                prev_arrow_shot_at = curr_end;
            }
        }
        return arrows;
    }
};

int main() {
    // Solution* sol = new Solution();
    SolutionMain* sol = new SolutionMain();
    // SolutionPractice* sol = new SolutionPractice();

    vector<vector<int>> points;

    auto print_vvi = [&](vector<vector<int>> v) {
        int n = v.size();
        for (int i = 0; i < n; i++)
            cout << "[" << v[i][0] << " " << v[i][1] << "] ";
        cout << endl;
    };

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
    {
        points = { { 2, 3 }, { 2, 3 } };
        cout << sol->findMinArrowShots(points) << endl;
    }
    {
        points = { { -1, 1 }, { 0, 1 }, { 2, 3 }, { 1, 2 } };
        cout << sol->findMinArrowShots(points) << endl;
    }
    {
        points = { { -2147483648, 2147483647 } };
        cout << sol->findMinArrowShots(points) << endl;
    }

    delete sol;
}
