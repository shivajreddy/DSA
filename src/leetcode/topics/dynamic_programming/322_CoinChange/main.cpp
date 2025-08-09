// https://leetcode.com/problems/coin-change

#include <bits/stdc++.h>
#include <climits>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {

        unordered_map<int, int> hm;
        function<int(long long)> rec = [&](long long curr_amount) -> int {
            if (curr_amount > amount) return INT_MAX;
            if (curr_amount == amount) return 0;
            if (hm.find(curr_amount) != hm.end()) return hm[curr_amount];

            long long val = INT_MAX;
            for (int c : coins) {
                long long res = rec(curr_amount + c);
                if (res != INT_MAX) val = min(val, 1 + res);
            }

            return hm[curr_amount] = val;
        };

        int res = rec(0);
        return res == INT_MAX ? -1 : res;
    }
};

/*

coins:
amount:

*/

int main() {
    Solution* s = new Solution();
    vector<int> coins;
    int amount;

    coins = { 1, 2, 5 };
    amount = 11;
    cout << s->coinChange(coins, amount) << endl;

    coins = { 2 };
    amount = 3;
    cout << s->coinChange(coins, amount) << endl;

    coins = { 1 };
    amount = 0;
    cout << s->coinChange(coins, amount) << endl;

    delete s;
}
