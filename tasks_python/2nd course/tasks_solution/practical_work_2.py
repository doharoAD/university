'''
Работу выполнил студент группы ИЭОЗС-62-22 Муратов А.Д. 
Номер варианта - 14

Задания:

1.3. Практические задачи на вычисления в цикле
1.3.3. Накопление сумм
'''

# Импортируем библиотеку tabulate для создания таблиц: pip install tabulate
from tabulate import tabulate

# Определяем класс OilWell для расчета пенсии
class PensionCalculator:

    # инициализация
    def __init__(self, p, Z, q):
        self.p = p # Процент пенсионных отчислений
        self.Z = Z # Начальная заработная плата в январе
        self.q = q # Процент увеличения заработной платы каждый месяц
        self.total_contributions = 0 # Общая сумма пенсионных отчислений

    def calculate_contributions(self):
        data = [] # Список для хранения данных о каждом месяце
        for month in range(1, 13):
            # Рассчитываем сумму пенсионных отчислений за текущий месяц
            self.total_contributions += self.Z * self.p

             # Добавляем данные о текущем месяце в список
            data.append([month, f"{self.Z:.2f}", f"{self.total_contributions:.2f}"])

             # Увеличиваем заработную плату и процент увеличения на следующий месяц
            self.Z *= (1 + self.q)
            self.q += 1

        # Вывод таблицы с результатами
        headers = ["Месяц", "Заработная плата", "Сумма пенсионных отчислений"]
        print(tabulate(data, headers=headers, tablefmt="grid"))


# Функция для проверки ввода числа с плавающей точкой
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Пожалуйста, введите число.")
if __name__ == "__main__":
    # Ввод данных с проверкой
    p = get_float_input("Введите процент пенсионных отчислений (в десятичных долях): ")
    Z = get_float_input("Введите заработную плату в январе: ")
    q = get_float_input("Введите процент увеличения заработной платы каждый месяц (в десятичных долях): ")

    # Создание экземпляра класса PensionCalculator
    calculator = PensionCalculator(p, Z, q)

    # Рассчет пенсионных отчислений за год и вывод результатов
    calculator.calculate_contributions()