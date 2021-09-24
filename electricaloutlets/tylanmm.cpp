#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        int ans = 1;
        for (int j = 0; j < k; j++) {
            int o;
            cin >> o;
            ans += o - 1;
        }
        cout << ans << '\n';
    }
    cout << std::flush;

    return 0;
}