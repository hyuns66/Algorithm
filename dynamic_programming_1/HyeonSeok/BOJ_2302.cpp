#include <iostream>
#include <vector>

using namespace std;

int N, M;

int main() {
    cin >> N >> M;
    vector<int> dp(41, 0);

    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;

    for (int i=3; i<41; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }

    int answer = 1;
    int prev = 0;
    for (int i=0; i<M; i++) {
        int temp;
        cin >> temp;

        answer *= dp[temp-prev-1];
        prev = temp;
    }

    answer *= dp[N-prev];
    cout << answer;
}