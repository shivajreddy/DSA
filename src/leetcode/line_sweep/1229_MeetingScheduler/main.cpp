// 1229. Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> minAvailableDuration(vector<vector<int>>& slots1,
                                     vector<vector<int>>& slots2,
                                     int duration) {
        vector<pair<int, char>> events;

        // Add all start and end events
        for (const auto& slot : slots1) {
            events.push_back({ slot[0], 's' });
            events.push_back({ slot[1], 'e' });
        }
        for (const auto& slot : slots2) {
            events.push_back({ slot[0], 's' });
            events.push_back({ slot[1], 'e' });
        }

        sort(events.begin(), events.end());

        int curr_overlap = 0;
        int overlap_start = -1;

        for (int i = 0; i < events.size(); i++) {
            if (events[i].second == 's') { // start event
                curr_overlap++;
                if (curr_overlap == 2) {
                    // Overlap period starts now
                    overlap_start = events[i].first;
                }
            } else { // end event
                if (curr_overlap == 2) {
                    // We're ending an overlap period
                    int overlap_end = events[i].first;
                    int available_duration = overlap_end - overlap_start;

                    if (available_duration >= duration) {
                        return { overlap_start, overlap_start + duration };
                    }
                }
                curr_overlap--;
            }
        }

        return {}; // No suitable slot found
    }
};

int main() {
    Solution* sol = new Solution();
    vector<vector<int>> slots1, slots2;
    int duration;

    auto print_vvi = [&](vector<vector<int>> v) {
        int n = v.size();
        for (int i = 0; i < n; i++)
            cout << "[" << v[i][0] << " " << v[i][1] << "] ";
        cout << endl;
    };
    auto printv = [&](vector<int> v) {
        for (int num : v) cout << num << " ";
        cout << endl;
    };

    {
        cout << "TESTCASE 1\n";
        slots1 = { { 10, 50 }, { 60, 120 }, { 140, 210 } };
        slots2 = { { 0, 15 }, { 60, 70 } };
        duration = 8;
        printv(sol->minAvailableDuration(slots1, slots2, duration));
    }

    {
        cout << "TESTCASE 2\n";
        slots1 = { { 10, 50 }, { 60, 120 }, { 140, 210 } };
        slots2 = { { 0, 15 }, { 60, 70 } };
        duration = 12;
        printv(sol->minAvailableDuration(slots1, slots2, duration));
    }

    delete sol;
}
