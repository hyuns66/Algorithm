#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int s, N, K, R1, R2, C1, C2;
vector<vector<int>> graph;

bool validate(int sy, int sx, int ey, int ex) {
    // cout << sy << " " << ey << endl;
    // cout << sx << " " << ex << endl;
    if (ey < R1 || sy > R2 || ex < C1 || sx > C2) return false;
    return true;
}

void devide(int sy, int sx, int size, int num) {
    if (!validate(sy, sx, sy + size - 1, sx + size - 1)) return;
    if (size == 1) {
        if (sy <= R2 && sy >= R1 && sx >= C1 && sx <= C2) {
            int y = sy - R1;
            int x = sx - C1;
            graph[y][x] = num;
        }
        return;
    }
    int new_size = size / N;
    int white_count = (N - K) / 2;
    for (int i=0; i<N * N; i++) {
        int dy = i / N;
        int dx = i % N;
        int ty = sy + dy * new_size;
        int tx = sx + dx * new_size;
        if (dy < white_count || dy >= N - white_count || dx < white_count || dx >= N - white_count) {
            devide(ty, tx, new_size, num | 0);
        } else {
            devide(ty, tx, new_size, num | 1);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> s;
    cin >> N;
    cin >> K;
    cin >> R1;
    cin >> R2;
    cin >> C1;
    cin >> C2;

    graph = vector<vector<int>> (R2 - R1 + 1, vector<int>(C2 - C1 + 1, 2));
    devide(0, 0, pow(N, s), 0);

    for (int y=0; y<=R2 - R1; y++) {
        for (int x=0; x<=C2 - C1; x++) {
            cout << graph[y][x];
        }
        cout << '\n';
    }
}