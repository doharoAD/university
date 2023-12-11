'''
Работу выполнил студент группы Иэозс-62-22 Муратов Артемий Денисович

ЗАДАЧА:

Заменить в третьем столбце матрицы A (5×7) все нули на единицы,
а в пятом столбце матрицы  B (4×5) — все единицы на нули
'''
import random

class Matrix:
    def __init__(self, rows, cols):
        # Создаем матрицу с заданным числом строк и столбцов
        self.rows = rows
        self.cols = cols
        self.data = self.generate_matrix()

    def generate_matrix(self):
        # Заполняем матрицу случайными числами от 0 до 9
        matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(random.randint(0, 9))
            matrix.append(row)
        return matrix

    def display(self):
        # Выводим матрицу на экран
        for row in self.data:
            print(row)

class ModifiedMatrix(Matrix):
    def replace_zeros_in_third_column(self):
        # Заменяем все нули в третьем столбце на единицы
        for i in range(self.rows):
            if self.data[i][2] == 0:
                self.data[i][2] = 1

class AnotherModifiedMatrix(Matrix):
    def replace_ones_in_fifth_column(self):
        # Заменяем все единицы в пятом столбце на нули
        for i in range(self.rows):
            if self.data[i][4] == 1:
                self.data[i][4] = 0


"""
if __name__ == "__main__":
    # Создаем матрицу A (5x7) и выводим её до модификации
    matrix_A = ModifiedMatrix(5, 7)
    print("Матрица A до модификации:")
    matrix_A.display()

    # Модифицируем матрицу A
    matrix_A.replace_zeros_in_third_column()

    # Выводим матрицу A после модификации
    print("\nМатрица A после замены нулей в третьем столбце на единицы:")
    matrix_A.display()

    # Создаем матрицу B (4x5) и выводим её до модификации
    matrix_B = AnotherModifiedMatrix(4, 5)
    print("\nМатрица B до модификации:")
    matrix_B.display()

    # Модифицируем матрицу B
    matrix_B.replace_ones_in_fifth_column()

    # Выводим матрицу B после замены единиц в пятом столбце на нули
    print("\nМатрица B после замены единиц в пятом столбце на нули:")
    matrix_B.display()
"""