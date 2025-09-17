#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> board;

bool check(int y, int x, int num) {
    // 가로줄
    for (int tx=0; tx<9; tx++) {
        if (board[y][tx] == num) return false;
    }
    // 세로줄
    for (int ty=0; ty<9; ty++) {
        if (board[ty][x] == num) return false;
    }
    // 네모
    int sy, sx;
    sy = (y / 3) * 3;
    sx = (x / 3) * 3;
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            if (board[sy+i][sx+j] == num) return false;
        }
    }
    // 세 가지 조건 다 통과하면 true 리턴
    return true;
}

void print_and_finish() {
    for (int y=0; y<9; y++) {
        for (int x=0; x<9; x++) {
            cout << board[y][x];
        }
        cout << endl;
    }
    exit(0);
}

void backtracking(int idx) {
    if (idx >= 81) {
        print_and_finish();
        return;
    }
    int y, x;
    y = idx / 9;
    x = idx % 9;
    if (board[y][x] == 0) {
        vector<int> possible;
        for (int num = 1; num <= 9; num++) {
            if (check(y, x, num)) {
                possible.push_back(num);
            }
        }
        for (int num : possible) {
            board[y][x] = num;
            backtracking(idx + 1);
            board[y][x] = 0;
        }
    } else {
        backtracking(idx + 1);
    }
    
}

int main() {
    for (int i=0; i<9; i++) {
        string temp;
        cin >> temp;
        board.push_back({});
        for (char c : temp) {
            int num = c - '0';
            board[i].push_back(num);
        }
    }

    backtracking(0);
}