#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int T, W;

int main() {
    cin >> T >> W;
    vector<int> timeline;

    int prev = 1;
    int count = 0;
    for (int i=0; i<T; i++) {
        int num;
        cin >> num;
        if (num == prev) {
            count++;
        } else {
            timeline.push_back(count);
            prev = num;
            count = 1;
        }
    }
    timeline.push_back(count);
    
    vector<vector<int>> dp(timeline.size(), vector<int>(W + 1, 0));

    dp[0][0] = timeline[0];

    for (int i=1; i<timeline.size(); i++) {
        for (int w=0; w<=W; w++) {
            bool canGet = (i&1) == (w&1);
            if (!canGet) {
                dp[i][w] = dp[i-1][w];
            } else {
                if (w > 0) {
                    dp[i][w] = max(dp[i][w], dp[i-1][w-1] + timeline[i]);
                }
                if (i > 1) {
                    dp[i][w] = max(dp[i][w], dp[i-2][w] + timeline[i]);
                }
            }
        }
    }

    int answer = 0;
    for (auto d: dp[dp.size()-1]) {
        answer = max(answer, d);
    }

    cout << answer;
}

// 0 1 2 2 2

// 0 0 0
// 0 1 0
// 2 1 3
// 2 4 3
// 4 4 6

// 3 1 2 1

// 3 0
// 3 4
// 5 4
