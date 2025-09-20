#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

int N;
vector<int> numbers;
int answer[3];

bool is_left_go(int left, int right, int ban) {
    int nl, nr;
    nl = left+1;
    nr = right-1;
    if (abs((long long) numbers[nl] + numbers[right] + numbers[ban]) < abs((long long) numbers[left] + numbers[nr] + numbers[ban])) return true;
    return false;
}

tuple<int, int, int, int> search_min_cost(int base) {
    int left = base+1, right = N-1;
    int base_num = numbers[base];
    long long min_cost = 3000000001;
    int ll = left, rr = right;
    while (left < right) {
        long long cost = abs((long long)numbers[left] + numbers[right] + base_num);
        if (cost < min_cost) {
            min_cost = cost;
            ll = left;
            rr = right;
        }
        bool is_left = is_left_go(left, right, base);
        if (is_left) {
            left += 1;
        } else {
            right -= 1;
        }
    }
    return {min_cost, numbers[ll], numbers[rr], base_num};
}

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        int num;
        cin >> num;
        numbers.push_back(num);
    }

    sort(numbers.begin(), numbers.end());
    unsigned int min_result = 3000000001;
    for (int i=0; i<N-2; i++) {
        auto [min_cost, left, right, ban] = search_min_cost(i);
        if (min_cost < min_result) {
            min_result = min_cost;
            if (ban < left) {
                answer[0] = ban;
                answer[1] = left;
                answer[2] = right;
            } else if (ban > right) {
                answer[0] = left;
                answer[1] = right;
                answer[2] = ban;
            } else {
                answer[0] = left;
                answer[1] = ban;
                answer[2] = right;
            }
        }
    }

    cout << answer[0] << " " << answer[1] << " " << answer[2];
}