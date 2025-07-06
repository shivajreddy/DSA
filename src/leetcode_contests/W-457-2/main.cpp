// problem link

#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> processQueries(int c, vector<vector<int>>& connections,
                               vector<vector<int>>& queries) {

        unordered_map<int, vector<int>> hm; // { c1 : [1/0, c2, c3 ... ] }
        // all the items in list are sorted except first one

        // start with all c stations, turn them on individually
        for (int i = 1; i <= c; i++)
            hm[i] = vector<int> { 1 };

        for (vector<int> conn : connections) {
            int c1 = conn[0], c2 = conn[1];

            if (c1 == c2) continue;
            if (binary_search(hm[c1].begin() + 1, hm[c1].end(), c2)) {
                hm[c1].push_back(c2);
                sort(hm[c1].begin() + 1, hm[c1].end());
            }
            if (binary_search(hm[c2].begin() + 1, hm[c2].end(), c1)) {
                hm[c2].push_back(c1);
                sort(hm[c2].begin() + 1, hm[c2].end());
            }
        }

        vector<int> res;

        // do queries
        for (vector<int> query : queries) {
            int type = query[0];
            int target = query[1];

            if (type == 1) { // checking query
                if (hm[target][0] == 1)
                    res.push_back(target);
                else {
                    int smallest_c = -1;
                    // look for a station that is not turned off
                    for (int i = 1; i < hm[target].size(); i++) {
                        int next_c = hm[target][i];
                        if (hm[next_c][0] == 1) {
                            smallest_c = next_c;
                            break;
                        }
                    }
                    smallest_c == -1 ? res.push_back(-1)
                                     : res.push_back(smallest_c);
                }
            } else { // turn off station query
                hm[target][0] = 0;
            }
        }
        return res;
    }
};

int main() {
    Solution* s = new Solution();

    int c;
    vector<vector<int>> connections, queries;

    // Initialize your test data
    c = 5;
    connections = { { 1, 2 }, { 2, 3 }, { 3, 4 }, { 4, 5 } };
    queries = { { 1, 3 }, { 2, 1 }, { 1, 1 }, { 2, 2 }, { 1, 2 } };

    c = 3;
    connections = {};
    queries = { { 1, 1 }, { 2, 1 }, { 1, 1 } };

    c = 4;
    connections = { { 4, 3 }, { 3, 1 }, { 4, 2 }, { 3, 2 }, { 4, 1 } };
    queries = { { 2, 3 }, { 1, 2 }, { 2, 4 }, { 1, 1 }, { 2, 2 },
                { 1, 2 }, { 1, 2 }, { 2, 2 }, { 1, 3 }, { 2, 3 },
                { 2, 4 }, { 2, 3 }, { 2, 4 }, { 1, 2 }, { 1, 1 } };

    // Call the function
    vector<int> result = s->processQueries(c, connections, queries);

    // Print results if needed
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;

    delete s;
    return 0;
}
