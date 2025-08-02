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

        // Two-pointer approach to find longest valid subarray
        int win_len = 0; // At least one element can always be kept
        int l = 0;
        for (int r = 0; r < n; r++) {
            // Shrink window from left while condition is violated
            while ((long long)nums[l] * k < nums[r]) l++;
            win_len = max(win_len, r - l + 1); // Update max-len of valid subarr
        }

        return n - win_len;
    }
};

class SolutionMain {
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
