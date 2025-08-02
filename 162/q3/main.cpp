// Q3. Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/contest/biweekly-contest-162/problems/earliest-finish-time-for-land-and-water-rides-ii/

#include <bits/stdc++.h>
#include <climits>
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

        // Case 1 : land then water
        // find earliest end time
        int earliest_land_end = INT_MAX;
        for (int i = 0; i < landDuration.size(); i++)
            earliest_land_end =
                min(earliest_land_end, landStartTime[i] + landDuration[i]);
        int case1_res = INT_MAX;
        for (int i = 0; i < waterDuration.size(); i++) {
            int val;
            if (waterStartTime[i] > earliest_land_end) {
                val = waterStartTime[i] + waterDuration[i];
            } else {
                val = earliest_land_end + waterDuration[i];
            }
            case1_res = min(case1_res, val);
        }

        // Case 2 : water then land
        // find earliest end time
        int earliest_water_end = INT_MAX;
        for (int i = 0; i < waterDuration.size(); i++)
            earliest_water_end =
                min(earliest_water_end, waterStartTime[i] + waterDuration[i]);
        int case2_res = INT_MAX;
        for (int i = 0; i < landDuration.size(); i++) {
            int val;
            if (landStartTime[i] > earliest_water_end) {
                val = landStartTime[i] + landDuration[i];
            } else {
                val = earliest_water_end + landDuration[i];
            }
            case1_res = min(case1_res, val);
        }

        return min(case1_res, case2_res);
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
