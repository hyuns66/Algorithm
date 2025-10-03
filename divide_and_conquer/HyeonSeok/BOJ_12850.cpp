#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int D;
vector<vector<long long>> default_graph = {
    {0, 1, 1, 0, 0, 0, 0, 0},
    {1, 0, 1, 1, 0, 0, 0, 0},
    {1, 1, 0, 1, 1, 0, 0, 0},
    {0, 1, 1, 0, 1, 1, 0, 0},
    {0, 0, 1, 1, 0, 1, 0, 1},
    {0, 0, 0, 1, 1, 0, 1, 0},
    {0, 0, 0, 0, 0, 1, 0, 1},
    {0, 0, 0, 0, 1, 0, 1, 0},
};

vector<vector<long long>> pow_graph(
    const vector<vector<long long>>& a, 
    const vector<vector<long long>>& b
) {
    vector<vector<long long>> new_graph = {
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
    };
    for (int y=0; y<8; y++) {
        for (int x=0; x<8; x++) {
            for (int k=0; k<8; k++) {
                new_graph[y][x] += a[y][k] * b[k][x];
            }
            new_graph[y][x] = new_graph[y][x] % 1000000007;
        }
    }
    return new_graph;
}

vector<vector<long long>> devide(int scale) {
    if (scale == 1) {
        return default_graph;
    }
    vector<vector<long long>> half_pow = devide(scale / 2);
    vector<vector<long long>> result = pow_graph(half_pow, half_pow);
    if (scale & 1) {
        result = pow_graph(result, default_graph);
    }
    return result;
}

int main() {
    cin >> D;
    vector<vector<long long>> result = devide(D);
    cout << result[0][0];
}