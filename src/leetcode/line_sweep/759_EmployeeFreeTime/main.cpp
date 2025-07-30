// 759. Employee Free Time
// https://leetcode.com/problems/employee-free-time

#include <bits/stdc++.h>
using namespace std;

// Definition for an Interval.
class Interval {
public:
    int start;
    int end;

    Interval() {
    }

    Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};

class Solution {
public:
    vector<Interval> employeeFreeTime(vector<vector<Interval>> schedule) {
        return {};
    }
};

int main() {
    Solution* sol = new Solution();

    vector<vector<Interval>> schedule;

    auto print_intervals = [&](vector<Interval> v) {
        int n = v.size();
        for (int i = 0; i < n; i++)
            cout << "[" << v[i].start << " " << v[i].end << "] ";
        cout << endl;
    };

    {
        schedule = { { Interval(1, 2), Interval(5, 6) },
                     { Interval(1, 3), Interval(4, 10) } };
        cout << "RECEIVED: ";
        print_intervals(sol->employeeFreeTime(schedule));
        cout << "EXPECTED: [[3,4]]" << endl;
    }
    {
        schedule = { { Interval(1, 3), Interval(6, 7) },
                     { Interval(2, 4) },
                     { Interval(2, 5), Interval(9, 12) } };
        cout << "RECEIVED: ";
        print_intervals(sol->employeeFreeTime(schedule));
        cout << "EXPECTED: [[5,6],[7,9]]" << endl;
    }
    delete sol;
}
