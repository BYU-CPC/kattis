#include <iostream>
#include <string>
using std::cin;
using std::cout;

int main() {
    std::string w;
    cin >> w;
    for (char c : w) {
        if (c == 'e') cout << "ee";
        else          cout << c;
    }
    cout << std::endl;
}