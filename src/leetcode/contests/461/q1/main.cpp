// Q1. Trionic Array I
// https://leetcode.com/contest/weekly-contest-461/problems/trionic-array-i

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int n = nums.size();
        string s = nums[0] < nums[1] ? "<" : ">";
        for (int i = 2; i < n; i++) {
            char sym;
            if (nums[i - 1] < nums[i]) {
                sym = '<';
            } else if (nums[i - 1] > nums[i]) {
                sym = '>';
            } else {
                sym = '=';
            }
            if (s.back() != sym) s += sym;
        }
        return s == "<><";
    }
};

int main() {
}
