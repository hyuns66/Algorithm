#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int  N, M, k;

int dfs(vector<vector<int>>& graph, vector<bool>& visited, vector<int>& costs, int node) {
    int result = 1000001;
    visited[node] = true;
    stack<int> s;
    s.push(node);
    while (!s.empty()) {
        int cur = s.top();
        result = min(result, costs[cur]);
        s.pop();
        for (auto tar: graph[cur]) {
            if (visited[tar]) continue;
            visited[tar] = true;
            s.push(tar);
        }
    }
    return result;
}

int main() {
    cin >> N >> M >> k;

    vector<int> costs(N, 0);
    for (int i=0; i<N; i++) {
        cin >> costs[i];
    }

    vector<vector<int>> graph(N, vector<int>());
    for (int i=0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a-1].push_back(b-1);
        graph[b-1].push_back(a-1);
    }

    vector<bool> visited(N, false);
    int totalCost = 0;
    for (int i=0; i<N; i++) {
        if (visited[i]) continue;
        int cost = dfs(graph, visited, costs, i);
        totalCost += cost;
    }

    if (totalCost <= k) {
        cout << totalCost;
    } else {
        cout << "Oh no";
    }
}