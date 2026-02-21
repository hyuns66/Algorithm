#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int T, N;

int main() {
    cin >> T;
    for (int t=0; t<T; t++) {
        cin >> N;
        priority_queue<long long> q;
        long long answer = 0;
        for (int i=0; i<N; i++) {
            int num;
            cin >> num;
            q.push(-num);
        }

        while (q.size() > 1) {
            long long first = q.top();
            q.pop();
            long long second = q.top();
            q.pop();
            q.push(first + second);
            answer += first + second;
        }

        cout << -answer << endl;
    }
}