#include <iostream>
#include <vector>

using namespace std;
const int MOD = 1000000000;

int N;
vector<vector<vector<long long>>> dp;

int main() {
    cin >> N;
    for (int i=0; i<N+1; i++) {
        dp.push_back(vector<vector<long long>>(10, vector<long long>((1 << 10), 0)));
    }
    for (int i=1; i<10; i++) {
        dp[1][i][1 << i] = 1;
    }
    // i 번째 위치에 대해서
    for (int i=2; i<N+1; i++) {
        // 0~9 까지 대입해보고 가능한 케이스 dp 에 몇개인지 기록
        for (int num=0; num<10; num++) {
            for (int prev_mask = 0; prev_mask < (1 << 10); prev_mask++) {
                int cur_mask = prev_mask | (1 << num);
                if (num > 0) {
                    dp[i][num][cur_mask] = (dp[i][num][cur_mask] + dp[i-1][num-1][prev_mask]) % MOD;
                }
                if (num < 9) {
                    dp[i][num][cur_mask] = (dp[i][num][cur_mask] + dp[i-1][num+1][prev_mask]) % MOD;
                }
            }
        }
    }
    long long answer = 0;
    int full_mask = (1 << 10) - 1;

    for (int i = 0; i <= 9; i++) {
        // ✅ 2. 최종 합산 과정에서도 MOD 연산 적용
        answer = (answer + dp[N][i][full_mask]) % MOD;
    }
    cout << answer;
}