// 731. My Calendar II
// https://leetcode.com/problems/my-calendar-ii

#include <bits/stdc++.h>
using namespace std;

class MyCalendarTwo {
public:
    // must use ordered hashmap
    map<int, int> timeline; // {booking_time: no.of_bookings}

    MyCalendarTwo() {
    }

    bool book(int startTime, int endTime) {
        // Temporarily add the booking
        timeline[startTime]++;
        timeline[endTime]--;

        // Check if this causes any triple booking
        int count = 0;
        for (auto& [booking_time, no_of_bookings] : timeline) {
            count += no_of_bookings;
            if (count >= 3) {
                // Triple booking detected, undo the booking
                timeline[startTime]--;
                timeline[endTime]++;
                if (timeline[startTime] == 0) timeline.erase(startTime);
                if (timeline[endTime] == 0) timeline.erase(endTime);
                return false;
            }
        }

        return true;
    }
};

class MyCalendarTwoMyAttempt {
public:
    // timeline holds { booking_time : count_of_active_bookings }
    vector<pair<long long, int>> time_line = { { -1e17, 0 } };
    // vector<long long> tl
    vector<pair<long long, int>> tl = { { -1e17, 0 }, { 1e17, 0 } };

    MyCalendarTwo() {
    }

    bool book(int startTime, int endTime) {
        int n = tl.size();

        // int count_at_s = -1, count_at_e = -1;
        // long long prev_start = -1e17 - 1;
        // pair<long long, int> target_start = { -1e17 - 1, 0 }, target_end = {
        // 1e17 + 1, 0 };

        int target_start_idx = 0;
        int target_end_idx = 1;

        for (int i = 0; i < n; i++) {
            auto pos = tl[i];
            pair<long long, int> target_start = tl[target_start_idx];
            pair<long long, int> target_end = tl[target_end_idx];
            if (pos.first <= startTime) {
                if (pos.first > target_start.first) {
                    target_start_idx = i;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            auto pos = tl[i];
            pair<long long, int> target_start = tl[target_start_idx];
            pair<long long, int> target_end = tl[target_end_idx];
            if (pos.first <= endTime + 1) {
                if (pos.first > target_end.first) {
                    target_end_idx = i;
                }
            }
        }

        // triple booking
        if (tl[target_start_idx].second == 3 || tl[target_end_idx].second == 3)
            return false;

        tl[target_start_idx].second += 1;
        tl[target_end_idx].second -= 1;

        return true;

        /*
        int count_at_s = count_before(startTime);
        int count_at_e = count_before(endTime);
        if (count_at_s == 3 || count_at_e == 3) return false;
        time_line[startTime] = count_at_s;
        time_line[endTime] = count_at_e;
        return true;
        */
    }

    // binary search on the timeline for the booking_time that is less than
    // by 1 from the given booking_time
    int count_before(int booking_time) {
        // find the booking_time
        int l = 0, r = time_line.size() - 1;
        while (r - l + 1 > 2) { // shrink to a window size of 2 elements
            int mid = l + (r - l) / 2;
            if (time_line[mid].first == booking_time) {
                return time_line[mid].second;
            }
            if (time_line[mid].first > booking_time) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return time_line[l].second; // count of active bookings at this time
    }
};

int main() {
    MyCalendarTwo* cal = new MyCalendarTwo();
    int startTime, endTime;

    {
        bool param1 = cal->book(startTime, endTime);
    }

    delete cal;
}
