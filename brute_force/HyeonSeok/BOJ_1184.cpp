#include <iostream>
#include <vector>
#include <map>

using namespace std;

int N;
vector<vector<int>> graph;
vector<vector<int>> g_sum;

int get_cost(int sy, int sx, int ey, int ex) {
    int left_sum = 0;
    int top_sum = 0;
    int cross_sum = 0;
    if (sy > 0) {
        top_sum = g_sum[sy-1][ex];
    }
    if (sx > 0) {
        left_sum = g_sum[ey][sx-1];
    }
    if (sy > 0 && sx > 0) {
        cross_sum = g_sum[sy-1][sx-1];
    }
    return g_sum[ey][ex] - left_sum - top_sum + cross_sum;
}


int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        graph.push_back(vector<int>());
        for (int j=0; j<N; j++) {
            int t;
            cin >> t;
            graph[i].push_back(t);
        }
    }

    // 누적합 그래프 생성
    for (int y=0; y<N; y++) {
        g_sum.push_back(vector<int>());
        for (int x=0; x<N; x++) {
            int left_sum = 0;
            int top_sum = 0;
            int cross_sum = 0;
            if (y > 0) {
                top_sum = g_sum[y-1][x];
            }
            if (x > 0) {
                left_sum = g_sum[y][x-1];
            }
            if (x > 0 && y > 0) {
                cross_sum = g_sum[y-1][x-1];
            }
            g_sum[y].push_back(graph[y][x] + left_sum + top_sum - cross_sum);
        }
    }

    int answer = 0;
    // 중앙분할점
    for (int cy=0; cy < N-1; cy++) {
        for (int cx=0; cx < N-1; cx++) {
            map<int, int> cost_count;
            // 좌상단 계산
            for (int sy=0; sy<=cy; sy++) {
                for (int sx=0; sx<=cx; sx++) {
                    int cost = get_cost(sy, sx, cy, cx);
                    if (cost_count.find(cost) == cost_count.end()) {
                        cost_count[cost] = 0;
                    }
                    cost_count[cost] += 1;
                }
            }
            // 우하단 계산
            for (int ey=cy+1; ey<N; ey++){
                for (int ex=cx+1; ex<N; ex++) {
                    int cost = get_cost(cy+1, cx+1, ey, ex);
                    answer += cost_count[cost];
                }
            }

            cost_count.clear();
            // 우상단 계산
            for (int sy=0; sy<=cy; sy++) {
                for (int sx=cx+1; sx<N; sx++) {
                    int cost = get_cost(sy, cx+1, cy, sx);
                    if (cost_count.find(cost) == cost_count.end()) {
                        cost_count[cost] = 0;
                    }
                    cost_count[cost] += 1;
                }
            }
            // 좌하단 계산
            for (int ey=cy+1; ey<N; ey++) {
                for (int ex=0; ex<=cx; ex++) {
                    int cost = get_cost(cy+1, ex, ey, cx);
                    answer += cost_count[cost];
                }
            }
        }
    }
    
    cout << answer;
}