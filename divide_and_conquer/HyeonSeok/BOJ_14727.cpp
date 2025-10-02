#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> histogram;
int N;

long long devide(int start, int end) {
    if (start > end) return -1;
    if (start == end) {
        return histogram[start];
    }
    int mid = (start + end) / 2;
    // 좌우에 존재하는 직사각형 넓이중 가장 큰것만 남기기
    long long result = max(devide(start, mid), devide(mid + 1, end));
    // 중심 통과하는 최대 크기 구하기
    int right = mid + 1;
    int left = mid;
    int mid_height = min(histogram[left], histogram[right]);
    while (right < end || left > start) {   // 한 쪽이라도 확장가능한 경우 로직 진행 (상세 조건은 로직 자체적으로 처리)
        if (right < end && (left == start || histogram[right+1] >= histogram[left-1])) {
            right++;
            mid_height = min(mid_height, histogram[right]);
        } else {
            left--;
            mid_height = min(mid_height, histogram[left]);
        }
        long long mid_width = right - left + 1;
        result = max(result, mid_width * mid_height);
    }
    return result;
}

int main() {
    cin >> N;

    int temp;
    for (int i=0; i<N; i++) {
        cin >> temp;
        histogram.push_back(temp);
    }

    long long answer = devide(0, N-1);
    cout << answer;
}