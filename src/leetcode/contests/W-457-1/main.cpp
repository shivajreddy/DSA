// problem link

#include <bits/stdc++.h>
using namespace std;

int main() {
}

class Solution {
public:
    bool invalid_chars(const string& s) {
        for (char c : s)
            if (!isalnum(c) && c != '_') return true;
        return false;
    }

    vector<string> validateCoupons(vector<string>& code,
                                   vector<string>& businessLine,
                                   vector<bool>& isActive) {

        int n = code.size();
        set<string> allowed_bis = { "electronics", "grocery", "pharmacy",
                                    "restaurant" };

        map<string, vector<string>> hm;
        for (int i = 0; i < n; i++) {
            string c = code[i];
            string bis = businessLine[i];
            bool active = isActive[i];

            if (c.size() == 0 || invalid_chars(c)) continue;
            if (allowed_bis.find(bis) == allowed_bis.end()) continue;
            if (!active) continue;

            hm[bis].push_back(c);
        }

        vector<string> res;
        for (auto [b, codes] : hm) {
            // sort with in the category lexigographically
            sort(codes.begin(), codes.end());
            res.insert(res.end(), codes.begin(), codes.end());
        }
        return res;
    }
};
