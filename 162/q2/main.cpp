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
    int minRemoval(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 1) return 0;

        sort(nums.begin(), nums.end());

        int maxLen = 1; // At least one element can always be kept
        int left = 0;

        // Two-pointer approach to find longest valid subarray
        for (int right = 0; right < n; right++) {
            // Shrink window from left while condition is violated
            while ((long long)nums[right] > (long long)nums[left] * k) {
                left++;
            }
            // Update maximum length of valid subarray
            maxLen = max(maxLen, right - left + 1);
        }

        return n - maxLen;
    }
};

class Solution2 {
public:
    int minRemoval(vector<int>& nums, int k) {

        int n = nums.size();
        if (n == 1) return 0;

        sort(nums.begin(), nums.end());

        struct pair_hash {
            size_t operator()(const pair<int, int>& p) const {
                return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
            }
        };
        unordered_map<pair<int, int>, int, pair_hash> hm;

        function<int(int, int)> rec = [&](int l, int r) -> int {
            if (l == r) return nums.size() - 1;
            if ((long long)nums[r] <= (long long)nums[l] * k)
                return n - (r - l + 1);
            if (hm.find({ l, r }) != hm.end()) return hm[{ l, r }];
            int L = rec(l + 1, r);
            int R = rec(l, r - 1);
            return hm[{ l, r }] = min(L, R);
        };

        return rec(0, n - 1);
    }
};

int main() {
    Solution sol;
    vi nums;
    int k;
    {
        nums = { 2, 1, 5 };
        k = 2;
        cout << "RESULT: " << sol.minRemoval(nums, k) << endl;
        cout << "EXPECTED: 1" << endl;
    }
    {
        nums = { 1, 6, 2, 9 };
        k = 3;
        cout << "RESULT: " << sol.minRemoval(nums, k) << endl;
        cout << "EXPECTED: 2" << endl;
    }
    {
        nums = { 4, 6 };
        k = 2;
        cout << "RESULT: " << sol.minRemoval(nums, k) << endl;
        cout << "EXPECTED: 0" << endl;
    }

    return 0;
}
