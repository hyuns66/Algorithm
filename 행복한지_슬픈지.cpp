#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string message;
    getline(cin, message);
    int idx = 0;
    int happy = 0;
    int sad = 0;
    while (idx < message.length()) {
        if (message[idx] != ':') {
            idx++;
            continue;
        }
        if (message.substr(idx, 3) == ":-)") {
            happy++;
        } else if (message.substr(idx, 3) == ":-(") {
            sad++;
        }
        idx++;
    }
    if (happy == 0 && sad == 0) {
        cout << "none";
    } else if (happy > sad) {
        cout << "happy";
    } else if (sad > happy) {
        cout << "sad";
    } else {
        cout << "unsure";
    }
}