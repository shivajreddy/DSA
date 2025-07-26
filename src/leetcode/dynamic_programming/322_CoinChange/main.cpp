// https://leetcode.com/problems/coin-change

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        return -1;
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
