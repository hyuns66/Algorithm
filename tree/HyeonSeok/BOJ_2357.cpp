#include <iostream>
#include <vector>

using namespace std;

vector<int> min_tree;
vector<int> max_tree;
vector<int> numbers;

int make_max_tree(int node_idx, int left, int right) {
    // 리프노드 인 경우 입력받은 숫자 그대로 노드 생성
    if (left == right) return max_tree[node_idx] = numbers[left];

    // 중간 노드인 경우 자식들의 최대값 구해서 노드 생성
    int middle = (left + right) / 2;
    int left_max = make_max_tree(node_idx * 2, left, middle);
    int right_max = make_max_tree(node_idx * 2 + 1, middle + 1, right);
    return max_tree[node_idx] = max(left_max, right_max);
}

int make_min_tree(int node_idx, int left, int right) {
    // 리프노드 인 경우 입력받은 숫자 그대로 노드 생성
    if (left == right) return min_tree[node_idx] = numbers[left];

    // 중간 노드인 경우 자식들의 최대값 구해서 노드 생성
    int middle = (left + right) / 2;
    int left_min = make_min_tree(node_idx * 2, left, middle);
    int right_min = make_min_tree(node_idx * 2 + 1, middle + 1, right);
    return min_tree[node_idx] = min(left_min, right_min);
}

pair<int, int> query(int node_idx, int q_left, int q_right, int start, int end) {
    if (start > q_right || end < q_left) return {1000000001, 0};
    if (start >= q_left && end <= q_right) {
        return {min_tree[node_idx], max_tree[node_idx]};
    }

    int mid = (start + end) / 2;
    auto [left_min, left_max] = query(node_idx * 2, q_left, q_right, start, mid);
    auto [right_min, right_max] = query(node_idx * 2 + 1, q_left, q_right, mid + 1, end);
    return {min(left_min, right_min), max(left_max, right_max)};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N;
    cin >> M;

    min_tree.resize(N*4);
    max_tree.resize(N*4);

    for (int i=0; i<N; i++) {
        int temp;
        cin >> temp;
        numbers.push_back(temp);
    }

    make_max_tree(1, 0, N-1);
    make_min_tree(1, 0, N-1);
    
    for (int i=0; i<M; i++) {
        int left, right;
        cin >> left;
        cin >> right;
        auto [q_min, q_max] = query(1, left - 1, right - 1, 0, N-1);
        cout << q_min << " " << q_max << "\n";
    }
}

//                             5
//             30                              5
//         30            38              20          5
//     30      100    38    50        51    20    81    5    
// 75    30                        51    52      