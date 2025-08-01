// Q3. Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/contest/biweekly-contest-162/problems/earliest-finish-time-for-land-and-water-rides-ii/

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

// Macro
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
#define vec vector

class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime,
                           vector<int>& landDuration,
                           vector<int>& waterStartTime,
                           vector<int>& waterDuration) {

        // case1: land then water
        // case1: water then land
        int n;
        // earliest to finish A, B
        n = landDuration.size();
        int eA = INT_MAX, eB = INT_MAX;
        for (int i = 0; i < n; i++) {
            pii curr = { landStartTime[i], landStartTime[i] + landDuration[i] };
        }

        // earliest to finish A, B
        int ea;
        pii target;
        target = { waterStartTime[0], waterStartTime[0] + waterDuration[0] };
        for (int i = 0; i < n; i++) {
            pii curr = { landStartTime[i], landStartTime[i] + landDuration[i] };
            ea = curr.second;
            if (curr.second <= target.first || curr.first >= target.second)
                break;
        }
        cout << "ea: " << ea << endl;

        // earliest to finish b
        int eb;
        target = { landStartTime[0], landStartTime[0] + landDuration[0] };
        for (int i = 0; i < n; i++) {
            pii curr = { waterStartTime[i],
                         waterStartTime[i] + waterDuration[i] };
            eb = curr.second;
            if (curr.second <= target.first || curr.first >= target.second)
                break;
        }
        cout << "eb: " << eb << endl;
        return max(ea, eb);
    }
};

int main() {
    Solution sol;
    vi landStartTime, landDuration, waterStartTime, waterDuration;
    {
        landStartTime = { 2, 8 };
        landDuration = { 4, 1 };
        waterStartTime = { 6 };
        waterDuration = { 3 };

        int result = sol.earliestFinishTime(landStartTime, landDuration,
                                            waterStartTime, waterDuration);
        cout << "RESULT:" << result << endl;
        cout << "EXPECTED:9" << endl;
    }
    {
        landStartTime = { 5 };
        landDuration = { 3 };
        waterStartTime = { 1 };
        waterDuration = { 10 };

        int result = sol.earliestFinishTime(landStartTime, landDuration,
                                            waterStartTime, waterDuration);
        cout << "RESULT:" << result << endl;
        cout << "EXPECTED:14" << endl;
    }

    return 0;
}
