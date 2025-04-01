#include <iostream>
#include <cmath>
#include <unordered_map>
#include <iomanip> // Include this header for std::setprecision

std::unordered_map<int, double> cache;

double f(int n) {
    if (n == 3) {
        return 7.0;
    }
    if (cache.find(n) != cache.end()) {
        return cache[n];
    }
    double r = f(n - 1);
    double result = sqrt((2.0 / 3.0) * r + (1.0 / (r * r)));
    cache[n] = result;
    return result;
}

int main() {
    std::cout << std::fixed << std::setprecision(10) << f(1000) << " " << pow(3, 1.0 / 3.0) << std::endl;
    return 0;
}
