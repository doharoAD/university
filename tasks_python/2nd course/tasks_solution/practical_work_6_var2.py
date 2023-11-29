'''
Работу выполнил студент группы Иэозс-62-22 Васильев Владислав Дмитриевич

ЗАДАЧА:
1.Если сумма SA положительных элементов главной диагонали матрицы A (7×7) больше единицы,
вывести значение  SA /SB, где  SB — сумма положительных элементов главной диагонали матрицы B (5×5).
'''
import random
class Matrix:
    def __init__(self, rows, cols):
        #Создаем матрицу с заданным числом строк и столбцов
        self.rows = rows
        self.cols = cols
        self.arr_matrix = self.generate_matrix()

    def generate_matrix(self):
        # Заполняем матрицу случайными числами
        matrix = []
        for i in range(self.rows):
            n = []
            for j in range(self.cols):
                n.append(random.randint(-9, 9))
            matrix.append(n)
        return matrix

    def print_matrix(self):
        # Выводим матрицу на экран
        for row in self.arr_matrix:
            print(row)

class Matrix_sum_diagonal(Matrix):
    def sum_main_diagonal(self):
        #ищим сумму Sа положительных элементов главной диагонали матрицы A (7×7)
        Sa = 0
        for i in range(self.rows):
            if self.arr_matrix[i][i] > 0:
                Sa += self.arr_matrix[i][i]
        return Sa

    def another_sum_diagonal(self):
         #ищим сумму Sb положительных элементов главной диагонали матрицы B (5×5)
        Sb = 0
        for i in range(self.rows):
            if self.arr_matrix[i][i] > 0:
                Sb += self.arr_matrix[i][i]
        return Sb

if __name__ == "__main__":
    #Создаем матрицу A(7,7)
    matrix_A = Matrix_sum_diagonal(7,7)

    #вывод матрицы А
    print("Матрица А (7×7)\n")
    matrix_A.print_matrix()

    #Создаем матрицу В(5,5)
    matrix_B = Matrix_sum_diagonal(5,5)

    #вывод матрицы А
    print("\nМатрица B\n")
    matrix_B.print_matrix()

    sum_Sa = matrix_A.sum_main_diagonal()
    sum_Sb = matrix_B.another_sum_diagonal()
    print(f"\nсумма Sа положительных элементов главной диагонали матрицы A (7×7): {round(sum_Sa, 3)} ")
    print(f"\nсумма Sb положительных элементов главной диагонали матрицы B (5×5): {round(sum_Sb, 3)} ")

    if sum_Sa > 1 and sum_Sb != 0:
        result = sum_Sa / sum_Sb
        print(f"\nРезультат Sa / Sb: {round(result, 3)}")
    else:
        print("\nСумма Sa не больше 1 или Sb=0")
   