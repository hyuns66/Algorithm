#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N;

int main(){
    cin >> N;
    vector<int> numbers(N, 0);

    for (int i=0; i<N; i++) {
        cin >> numbers[i];
    }

    vector<vector<long long>> dp(N-1, vector<long long>(21, 0));
    dp[0][numbers[0]] = 1;

    for (int i=1; i<N-1; i++) {
        for (int j=0; j<21; j++) {
            if (dp[i-1][j] == 0) continue;
            if (j + numbers[i] <= 20) {
                dp[i][j+numbers[i]] += dp[i-1][j];
            }
            if (j - numbers[i] >= 0) {
                dp[i][j-numbers[i]] += dp[i-1][j];
            }
        }
    }

    cout << dp[N-2][numbers[N-1]];
}