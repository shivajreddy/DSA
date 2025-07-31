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

        // 1. Collect all busy intervals from all employees
        vector<Interval> all;
        for (const auto& emp : schedule)
            for (const auto& interval : emp) all.push_back(interval);
        // 2. Sort intervals by start time
        sort(all.begin(), all.end(), [](const Interval& a, const Interval& b) {
            return a.start < b.start;
        });
        // 3. combine all intervals (merge intervals)
        // Merge overlapping intervals to get union of all busy times
        vector<Interval> combined;
        for (const auto& interval : all) {
            if (combined.empty() || combined.back().end < interval.start) {
                combined.push_back(interval);
            } else {
                combined.back().end = max(combined.back().end, interval.end);
            }
        }
        // 4. Get all the free blocks b/w the merged intervals
        // Note: we dont have to check if the width of this gap is > 0,
        // because when we merged exactly next to each other intervals
        // EX: [1 3] [3 5] got merged to [1 5]
        vector<Interval> res;
        for (int i = 1; i < combined.size(); i++) {
            res.push_back(Interval(combined[i - 1].end, combined[i].start));
        }
        return res;
    }
};

// BUG: failing for 3rd test case.
// dont do this because, its a unnecessarily complex approach.
class SolutionMine {
public:
    vector<Interval> employeeFreeTime(vector<vector<Interval>> schedule) {

        int mn = 1e9, mx = -1;
        for (auto emp : schedule) {
            mn = min(mn, emp[0].start);
            mx = max(mx, emp.back().end);
        }

        vector<Interval> free_blocks;

        for (auto emp : schedule) {
            int prev_end = mn;
            for (auto e_int : emp) {
                if (prev_end < e_int.start) {
                    free_blocks.push_back(Interval(prev_end, e_int.start));
                }
                prev_end = e_int.end;
            }

            // check time after employee last's end time until mx time
            if (emp.back().end < mx)
                free_blocks.push_back(Interval(emp.back().end, mx));
        }

        int n = free_blocks.size();
        vector<pair<int, char>> events(2 * n);
        for (int i = 0; i < n; i++) {
            events[i * 2] = { free_blocks[i].start, 's' };
            events[i * 2 + 1] = { free_blocks[i].end, 'e' };
        }

        // sweep line the events.
        sort(events.begin(), events.end(),
             [&](const pair<int, char>& a, const pair<int, char>& b) {
                 return a.first < b.first;
             });

        // Before reducing overlaps, check if
        // current overlaps == no.of employees
        int total_emp = schedule.size();
        vector<Interval> res;
        int curr_free_emp = 0; // no.of employees that are free at this moment
        for (int i = 0; i < events.size(); i++) {
            if (events[i].second == 's') {
                curr_free_emp++;
            } else {
                if (curr_free_emp == total_emp) {
                    res.push_back(
                        Interval(events[i - 1].first, events[i].first));
                }
                curr_free_emp--;
            }
        }

        return res;
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
                     { Interval(1, 3) },
                     { Interval(4, 10) } };
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
