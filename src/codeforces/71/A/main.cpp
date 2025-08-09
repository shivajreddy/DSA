// https://codeforces.com/problemset/problem/71/A

#include <iostream>
#include <string>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif // !ONLINE_JUDGE
}

void solution(const string& word);

int main() {
    setupIO();

    int t;
    cin >> t;

    string word;
    for (int i = 0; i < t; i++) {
        cin >> word;
        solution(word);
    }
}

void solution(const string& word) {
    int n = word.length();

    // abbreviate only if length is > 10
    if (n > 10) {
        string first = word.substr(0, 1);
        string last = word.substr(n - 1, 1);
        cout << first << (n - 2) << last << "\n";
    } else {
        cout << word << "\n";
    }
}
