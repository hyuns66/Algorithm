// BOJ Mock Test

#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int n, a, b, m;

struct Node {
  int num;
  int cost;
};

int main() {
  
  cin >> n;
  cin >> a >> b;
  cin >> m;

  vector<vector<int>> graph(n, vector<int>());

  for (int i=0; i<m; i++) {
    int parent, child;
    cin >> parent >> child;

    graph[parent-1].push_back(child-1);
    graph[child-1].push_back(parent-1);
  }

  vector<bool> visited(n, false);
  deque<Node> q;
  visited[a-1] = true;
  q.push_back({a-1, 0});

  while (!q.empty()) {
    Node cur = q.front();
    q.pop_front();
    if (cur.num == b-1) {
      cout << cur.cost;
      return 0;
    }

    for (auto next: graph[cur.num]) {
      if (visited[next]) continue;
      visited[next] = true;
      q.push_back({next, cur.cost + 1});
    }
    
  }

  cout << -1;
  return 0;
}
