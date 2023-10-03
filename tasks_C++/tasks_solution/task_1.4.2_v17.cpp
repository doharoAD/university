#include <iostream>
#include <cmath>

using namespace std;

int main() {
    float x, dx, x1, a, y;
    int n, i;

    cout << "Введите значение А: ";
    cin >> a;

    x1 = 2 * a;
    dx = a / 5;

    cout << "Введите кол-во вычислений: ";
    cin >> n;

    if (n < 1) {
        cout << "Неверные данные" << endl;
    }
    else {
        x = x1;
        cout << "№    X        Y" << endl;
        for (i = 1; i <= n; i++) {
            if (x < 0) {
                y = exp(1.0 / 3 * log(3)) * a * (1 - pow(exp(3 * log(-x)), 2));
            }
            else {
                y = sqrt(sqrt(16 * exp(4 * log(a)) + 4 * pow(x, 2) * pow(a, 2)) - pow(x, 2) - pow(a, 2));
            }
            cout << i << "   " << x << "   " << y << endl;
            x += dx;
        }
    }

    return 0;
}
