// 370. Range Addition
// https://leetcode.com/problems/range-addition

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {

        int n = updates.size();
        vector<tuple<int, char, int>> events(2 * n);

        for (int i = 0; i < n; i++) {
            events[i * 2] = { updates[i][0], 's', updates[i][2] };
            // since range is inclusive, start reducing after the update's end
            events[i * 2 + 1] = { updates[i][1] + 1, 'e', updates[i][2] };
        }

        sort(events.begin(), events.end()); // n.log(n)

        vector<int> res(length, 0);
        int val = 0;
        int event_idx = 0;
        for (int i = 0; i < length; i++) { // TIME: O(length)
            while (event_idx < events.size() &&
                   get<0>(events[event_idx]) == i) {
                if (get<1>(events[event_idx]) == 's') { // start
                    val += get<2>(events[event_idx]); // increase curr val by k
                } else {                              // end
                    val -= get<2>(events[event_idx]); // decrease curr val by k
                }
                event_idx++; // go to next event
            }
            res[i] = val;
        }

        return res;
    }
};

int main() {
    Solution* sol = new Solution();

    function<void(const vector<int>&)> printv = [&](const vector<int>& v) {
        for (int num : v) cout << num << " ";
        cout << endl;
    };

    int length;
    vector<vector<int>> updates;
    {
        length = 5;
        updates = { { 1, 3, 2 }, { 2, 4, 3 }, { 0, 2, -2 } };
        printv(sol->getModifiedArray(length, updates));
    }
    {
        length = 10;
        updates = { { 2, 4, 6 }, { 5, 6, 8 }, { 1, 9, -4 } };
        printv(sol->getModifiedArray(length, updates));
    }

    delete sol;
}
