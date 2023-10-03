'''
Работу выполнил студент группы ИЭОЗС-62-22 Муратов А.Д. 
Номер варианта - 14

Задания:

1.3. Практические задачи на вычисления в цикле
1.3.1. Вывод результатов в виде таблицы
1.3.2. Усложненные варианты задачи § 1.3.1
'''
# Импортируем библиотеку tabulate для создания таблиц: pip install tabulate
from tabulate import tabulate

# Определяем класс OilWell для представления нефтяной скважины
class OilWell:

    # Инициализация
    def __init__(self, initial_production, increase_per_year, decrease_percentage):
        self.production = initial_production
        self.increase = increase_per_year
        self.decrease_percentage = decrease_percentage

     # Рассчитываем историю добычи на протяжении указанного количества лет
    def calculate_production(self, years):
        production_history = []

        for year in range(1, years + 1):
            if year <= 10:

                # Рассчитываем увеличение добычи в течение первых 10 лет
                self.production += self.increase / year
            else:

                # Рассчитываем уменьшение добычи после 10 лет на основе процента уменьшения
                self.production -= (self.decrease_percentage / 100) * self.production
            production_history.append([year, f"{self.production:.2f} млн тонн"])

        return production_history

# Функция для проверки ввода числа
def get_valid_input(prompt, input_type=float):
    while True:
        try:
            value = input_type(input(prompt))
            return value
        except ValueError:
            print("Ошибка! Введите корректное число.")

if __name__ == "__main__":
    # Ввод данных с клавиатуры с проверкой
    initial_production = get_valid_input("Введите начальную добычу (в миллионах тонн): ")
    increase_per_year = get_valid_input("Введите увеличение добычи в миллионах тонн ежегодно: ")
    decrease_percentage = get_valid_input("Введите процент уменьшения добычи предыдущего года: ")

    # Создаем объект класса OilWell с введенными параметрами
    oil_well = OilWell(initial_production, increase_per_year, decrease_percentage)

    # Вычисляем добычу для первых 15 лет
    production_for_15_years = oil_well.calculate_production(15)

    # Выводим результат в виде таблицы
    table_headers = ["Год", "Добыча"]
    print(tabulate(production_for_15_years, headers=table_headers, tablefmt="grid"))
