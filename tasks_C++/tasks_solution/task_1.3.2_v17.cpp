#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    double x, y, sum;
    int k, n;

    cout << "Ввод х: ";
    cin >> x;

    cout << "Ввод n: ";
    cin >> n;

    if (n < 1) {
        cout << "Неверные данные" << endl;
    }
    else {
        sum = 0;
        for (k = 1; k <= n; k++) {
            sum += 1.0 / k * (exp(1.2 * k) - ((k + 1) / k)) / n + log(sqrt(k * x));
        };
        y = fabs(1.0 / 7 + sqrt(x)) + sum;
        cout << fixed;
        cout << setprecision(4);
        cout << "Результат: " << y << endl;
    }
    return 0;
}
