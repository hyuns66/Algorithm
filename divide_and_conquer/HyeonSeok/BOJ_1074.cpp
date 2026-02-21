#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N, ty, tx;
int answer = 0;

int step(int size, int sy, int sx, int ey, int ex) {
    // cout << sy << " " << sx << " " << ey << " " << ex << endl;
    if (ty < sy || ty > ey || tx < sx || tx > ex) return 0;
    int nextSize = size / 2;
    
    for (int i=0; i<4; i++) {
        int sx_ = sx + (i % 2) * nextSize;
        int sy_ = sy + (i / 2) * nextSize;
        int ex_ = sx + (i % 2 + 1) * nextSize - 1;
        int ey_ = sy + (i / 2 + 1) * nextSize - 1;

        answer += (nextSize * nextSize) * i * step(nextSize, sy_, sx_, ey_, ex_);
    }
    return 1;
}

int main() {
    cin >> N >> ty >> tx;

    step(pow(2, N), 0, 0, pow(2, N)-1, pow(2, N)-1);
    cout << answer;
}