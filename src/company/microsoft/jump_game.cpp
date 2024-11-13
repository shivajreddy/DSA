#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int> &nums) {
        int max_reach = 0;
        int remaining = 0;

        for (int num : nums) {
            if (remaining < 0)
                return false;
            max_reach += remaining + num;
            if (max_reach >= nums.size() - 1)
                return true;
        }
        remaining -= 1;

        return false;
    }
};

int main() {

    cout << "hi\n";

    return 0;
}
