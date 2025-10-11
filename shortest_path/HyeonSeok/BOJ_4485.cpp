#include <iostream>
#include <vector>
#include <queue>
#include <array>

using namespace std;

int N;
vector<vector<int>> graph;
priority_queue<array<int, 3>> pq;
vector<array<int, 2>> dirs = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
vector<vector<int>> dist;

int main() {
    int idx = 0;
    while (1) {
        idx++;
        cin >> N;
        if (N == 0) break;

        graph.clear();
        pq = priority_queue<array<int, 3>>();
        dist.clear();
        dist.assign(N, vector<int>(N, 3000));
        
        int temp;
        for (int i=0; i<N; i++) {
            graph.push_back(vector<int>());
            for (int j=0; j<N; j++) {
                cin >> temp;
                graph[i].push_back(temp);
            }
        }

        pq.push({-graph[0][0], 0, 0});
        while (!pq.empty()) {
            auto [cost, py, px] = pq.top();
            pq.pop();
            if (-cost > dist[py][px]) continue;
            for (auto [dy ,dx] : dirs) {
                int ty = py + dy;
                int tx = px + dx;
                if (ty < 0 || tx < 0 || ty >= N || tx >= N) continue;
                if (-cost + graph[ty][tx] >= dist[ty][tx]) continue;
                pq.push({cost - graph[ty][tx], ty, tx});
                dist[ty][tx] = -cost + graph[ty][tx];
            }
        }
        cout << "Problem " << idx << ": " << dist[N-1][N-1] << endl;
    }
}