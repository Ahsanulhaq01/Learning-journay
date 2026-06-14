#include <iostream>
using namespace std;

// Recursive function to calculate factorial
int factorial(int n) {
    if (n <= 1)
        return 1;
    return n * factorial(n - 1);
}

int main() {
    int value = factorial(5);
    cout << value << " is the factorial value!" << endl;
    return 0;
}