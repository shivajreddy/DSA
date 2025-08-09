#include <deque>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix) {
        vector<int> res;

        deque<pair<int, int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int rotation_idx = 0;

        int MIN_ROW = 0, MAX_ROW = matrix.size() - 1;
        int MIN_COL = 0, MAX_COL = matrix[0].size() - 1;

        int n = matrix.size() * matrix[0].size();

        int row = 0, col = 0;
        while (res.size() != n) {
            int next_num = matrix[row][col];
            res.push_back(next_num);

            // Next Postion
            int next_row = row + dirs[rotation_idx].first;
            int next_col = col + dirs[rotation_idx].second;

            // Check out of bounds
            if (next_row < MIN_ROW || next_row > MAX_ROW ||
                next_col < MIN_COL || next_col > MAX_COL) {
                // Left->Right : Shrink Top
                if (rotation_idx == 0)
                    MIN_ROW++;
                // Top -> Down : Shrink Right
                else if (rotation_idx == 1)
                    MAX_COL--;
                // Right->Left : Shrink Bot
                else if (rotation_idx == 2)
                    MAX_ROW--;
                // Down -> Top : Shrink Left
                else if (rotation_idx == 3)
                    MIN_COL++;

                // Rotate direction
                rotation_idx = (rotation_idx + 1) % 4;
                row += dirs[rotation_idx].first;
                col += dirs[rotation_idx].second;
            } else {
                row = next_row;
                col = next_col;
            }
        }

        return res;
    }
};

void print(const vector<int> &vec) {
    for (auto num : vec)
        cout << num << " ";
    cout << "\n";
}

int main() {
    Solution solution;

    vector<vector<int>> matrix1 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    vector<int> result1 = {1, 2, 3, 6, 9, 8, 7, 4, 5};
    print(solution.spiralOrder(matrix1));
    print(result1);

    vector<vector<int>> matrix2 = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    vector<int> result2 = {1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7};
    print(solution.spiralOrder(matrix2));
    print(result2);

    return 0;
}
