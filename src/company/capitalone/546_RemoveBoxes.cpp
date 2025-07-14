#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class Solution {
public:
    int removeBoxes(vector<int>& boxes) {
        return -1;
    }
};

int main() {
    Solution* s = new Solution();
    vector<int> boxes;

    {
        boxes = { 1, 3, 2, 2, 2, 3, 4, 3, 1 };
        cout << s->removeBoxes(boxes) << endl;
    }
    {
        boxes = { 1, 1, 1 };
        cout << s->removeBoxes(boxes) << endl;
    }
    {
        boxes = { 1 };
        cout << s->removeBoxes(boxes) << endl;
    }
}

/*
   - only the length matters


   a a b a
   a a b b a a a

   1 3 2 2 2 3 4 3 1 = 9
   1 3 3 4 3 1 = 1
   1 3 3 3 1  = 9
   1 1 = 4
   []

   a b c b a    {a:2 b:2 c:1}

   a c b b b c d c a  {a:2 b:3 c:3 d:1}
   1 1
*/
