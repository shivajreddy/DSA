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

        int arrows = 1;
        int arrowPos = points[0][1];

        for (int i = 1; i < n; i++) {
            if (points[i][0] > arrowPos) {
                arrows++;
                arrowPos = points[i][1];
            }
        }
        return arrows;
    }
};

class Solution2 {
public:
    int findMinArrowShots(vector<vector<int>>& points) {

        auto print_vvi = [&](vector<vector<int>> v) {
            int n = v.size();
            for (int i = 0; i < n; i++)
                cout << "[" << v[i][0] << " " << v[i][1] << "] ";
            cout << endl;
        };

        // print_vvi(points);
        sort(points.begin(), points.end());
        // print_vvi(points);

        int n = points.size();
        int arrows = 1;
        int prev = points[0][1];
        for (int i = 1; i < n; i++) {
            // cout << "checking points[" << i << "]" << endl;
            if (points[i][0] > prev) {
                prev = points[i][1];
                arrows++;
            } else {
                while (i < n && points[i][0] <= prev) {
                    // cout << "prev:" << prev << " skipping i:" << i << "
                    // because points[i][0]" << points[i][0] << endl;
                    i++;
                }
                i--;
            }
        }
        return arrows;
    }
};

int main() {
    Solution* sol = new Solution();

    vector<vector<int>> points;

    // /*
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
    // */
    {
        points = { { -1, 1 }, { 0, 1 }, { 2, 3 }, { 1, 2 } };
        cout << sol->findMinArrowShots(points) << endl;
    }

    delete sol;
}
