#include <iostream>
#include <vector>
#include <cmath>

double euclidean_distance(const std::vector<double>& a, const std::vector<double>& b) {
    double sum = 0.0;
    for (size_t i = 0; i < a.size(); i++) {
        double diff = a[i] - b[i];
        sum += diff * diff;
    }
    return std::sqrt(sum);
}

int main() {
    size_t n;
    std::cin >> n; // Read the size of the arrays

    std::vector<double> array1(n), array2(n);

    for (size_t i = 0; i < n; i++) {
        std::cin >> array1[i];
    }

    for (size_t i = 0; i < n; i++) {
        std::cin >> array2[i];
    }

    double distance = euclidean_distance(array1, array2);
    std::cout << distance << std::endl;

    return 0;
}

