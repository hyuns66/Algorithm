#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N, M;
vector<int> times;

int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        int time;
        cin >> time;
        times.push_back(time);
    }

    long long left = 0;
    long long right = pow(10, 18);
    long long mid;

    while (left < right) {
        mid = (left + right) / 2;
        long long total = 0;
        for (auto t: times) {
            total += (mid / t);
            // 오버플로 나면 skip
            if (total >= M) {
                break;
            }
        }
        if (total < M) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    cout << left;
}