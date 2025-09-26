#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<vector<int>> paper;
int answer[3] = {0, 0, 0};

bool check(int size, int sy, int sx) {
    int num = paper[sy][sx];
    for (int i=0; i<size; i++) {
        for (int j=0; j<size; j++) {
            if (paper[sy + i][sx + j] != num) return false;
        }
    }
    return true;
}

void devide(int size, int sy, int sx) {
    if (check(size, sy, sx)) {
        int idx = paper[sy][sx] + 1;
        answer[idx] += 1;
        return;
    }
    int new_size = size / 3;
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            devide(new_size, sy + (i * new_size), sx + (j * new_size));
        }
    }
}

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        paper.push_back(vector<int>());
        for (int j=0; j<N; j++) {
            int num;
            cin >> num;
            paper[i].push_back(num);
        }
    }

    devide(N, 0, 0);
    cout << answer[0] << endl;
    cout << answer[1] << endl;
    cout << answer[2] << endl;
}