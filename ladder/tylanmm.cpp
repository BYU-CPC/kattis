#include <iostream>
#include <cmath>
#define PI 3.1415926

int main() {
    int h, v;
    std::cin >> h >> v;
    std::cout << ceil(h / sin(PI * v / 180)) << std::endl;
    return 0;
}