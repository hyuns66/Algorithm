#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int N, K;

void rotate(deque<int>& life, deque<int>& robots) {
    // 벨트 회전
    rotate(life.begin(), life.end()-1, life.end());
    if (robots.empty()) return;
    // 벨트와 함께 로봇 1칸씩 전진
    for (int i=robots.size()-1; i>=0; i--) {
        robots[i] += 1;
    }
    // 맨 마지막 로봇 내리는 지점이면 하차
    if (robots.back() >= N-1) {
        robots.pop_back();
    }
}

void moveRobots(deque<int>& life, deque<int>& robots) {
    if (robots.empty()) return;
    // 먼저 벨트에 올라간 로봇부터 앞으로 1칸 전진
    for (int i=robots.size()-1; i>=0; i--) {
        if (i == robots.size()-1) {
            if (robots[i] < N-1 && life[robots[i]+1] > 0) {
                robots[i]++;
                life[robots[i]]--;
                continue;
            }
        }
        // 다음 위치에 로봇이 없고 다음 위치 내구도가 남아있을 때
        bool canGo = 
            (robots[i+1] != robots[i]+1) && (life[robots[i]+1] > 0);
        if (canGo) {
            robots[i]++;
            life[robots[i]]--;
        }
    }

    // 맨 마지막 로봇 내리는 지점이면 하차
    if (robots.back() >= N-1) {
        robots.pop_back();
    }
}

void addRobot(deque<int>& life, deque<int>& robots) {
    if (life[0] > 0) {
        life[0]--;
        robots.push_front(0);
    }
}

bool check(deque<int>& life) {
    int count = 0;
    for (int l: life) {
        if (l <= 0) count++;
    }

    return count < K;
}

int main() {
    cin >> N >> K;
    deque<int> life(2*N, 0);
    deque<int> robots;

    for (int i=0; i<2*N; i++) {
        cin >> life[i];
    }

    int answer = 1;
    while (true) {
        rotate(life, robots);
        moveRobots(life, robots);
        addRobot(life, robots);
        if (!check(life)) break;
        answer++;
    }

    cout << answer << endl;
}