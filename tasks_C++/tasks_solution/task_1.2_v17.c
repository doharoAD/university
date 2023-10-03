#include <stdio.h>
#include <math.h>

int main() {
    float x, y, h, a, b;
    int n, i;

    printf("Введите кол-во вычислений (n): ");
    scanf("%d", &n);

    printf("Введите левую границу отрезка  (а): ");
    scanf("%f", &a);

    printf("Введите правую границу отрезка  (b): ");
    scanf("%f", &b);

    if (b < a || n < 1) {
        printf("Неверные данные\n");
    }
    else {
        h = (b - a) / (n - 1);
        printf("Шаг равен: %f\n", h);
        x = a;
        for (i = 1; i <= n; i++) {
            y = (fabs((7.2 - 10 * x)) / (exp(1.0 / 3 * log(x / 9)))) * atan((4 * tan(2 * x))) / (sqrt(1.1 * exp(3 * log(x))));
            printf("%4d%10.3f%10.3f\n", i, x, y);
            x = x + h;
        }
    }

    return 0;
}
