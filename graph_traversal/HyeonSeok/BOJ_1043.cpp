#include <iostream>
#include <vector>
#include <set>

using namespace std;

void create_graph(const vector<int>& party, vector<set<int>>& graph) {
    for (int pp : party) {
        for (int p : party) {
            if (pp == p) continue;
            graph[pp].insert(p);
        }
    }
}

void dfs(const vector<set<int>>& graph, vector<bool>& visited, int start_node) {
    vector<int> stack;
    stack.push_back(start_node);
    visited[start_node] = true;
    while (!stack.empty()) {
        int cur = stack.back();
        stack.pop_back();
        for (const auto& dir : graph[cur] ) {
            // 구조체 분해를 통해 배열의 원소를 dy, dx 변수에 바로 할당
            if (visited[dir]) continue;
            stack.push_back(dir);
            visited[dir] = true;
        }
    }
}

int main() {
    int N, M;
    cin >> N;
    cin >> M;

    vector<int> knows;
    int know_cnt;
    cin >> know_cnt;

    if (know_cnt > 0) {
        for (int i=0; i < know_cnt; i++ ){
            int num;
            cin >> num;
            knows.push_back(num);
        }
    }

    vector<set<int>> graph(N+1);
    vector<vector<int>> party;
    for (int i=0; i<M; i++) {
        int count;
        cin >> count;
        party.push_back({});
        for (int k=0; k<count; k++) {
            int num;
            cin >> num;
            party[i].push_back(num);
        }
        create_graph(party[i], graph);
    }

    vector<bool> is_knows(N+1, false);
    for (const auto& know_man : knows) {
        dfs(graph, is_knows, know_man);
    }

    int answer = 0;
    for (const auto& p : party) {
        bool can_say_joke{true};
        for (const auto& man : p) {
            if (is_knows[man]) {
                can_say_joke = false;
                break;
            }
        }
        if (can_say_joke) {
            answer++;
        }
    }

    cout << answer;
}