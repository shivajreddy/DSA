// 253. Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        return { -1, -1 };
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
