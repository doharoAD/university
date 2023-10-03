import datetime

class Building:
    # Класс, представляющий здание с информацией о его местоположении и годе постройки
    def __init__(self, district, street, number, year):
        # Конструктор класса - создает новый экземпляр класса с заданными параметрами
        self.district = district
        self.street = street
        self.number = number
        self.year = year

    def __str__(self):
        # Форматирует экземпляр класса и возвращает его строковое представление
        return f"{self.street}, {self.number} ({self.year})"

class BuildingList:
    # Класс, представляющий список зданий и методы для их управления
    def __init__(self):
        # Конструктор класса - создает пустой список зданий
        self.buildings = []

    def add_building(self, building):
        # Добавить заданное здание в список зданий
        self.buildings.append(building)

    def get_buildings_by_district_and_year(self):
        # Возвращает словарь зданий, сгруппированных по району и году постройки
        result = {}
        for building in self.buildings:
            district = building.district
            year = building.year
            if district not in result:
                result[district] = {}
            if year not in result[district]:
                result[district][year] = []
            result[district][year].append(building)
        return result

def main():
    # Основная функция для пользовательского ввода и выполнения программы
    n = int(input("Введите количество зданий: "))

    building_list = BuildingList()
    # Заполнение списка зданиями
    for i in range(n):
        print(f"Введите данные для здания {i+1}:")
        district = input("Микрорайон: ")
        street = input("Улица: ")
        number = int(input("Номер дома: "))
	#проверка на кол-во символов в номере дома
    while len(number) > 4:
            print("Длина номера дома не должна превышать 4 символа.")
            number = input("Введите номер дома: ")
    # Запрос корректного года постройки
    while True:
        year = int(input("Год постройки: "))
        current_year = datetime.datetime.now().year
        if year < 1900 or year > current_year:
            print("Введите корректный год (не раньше 1900 г. и не позже текущего года)")
        else:
            break
        building = Building(district, street, number, year)
        building_list.add_building(building)

    # Группировка зданий по районам и годам постройки
    building_by_district = building_list.get_buildings_by_district_and_year()

    # Сортировка районов по алфавиту
    sorted_districts = sorted(building_by_district.keys())

    # Вывод результатов
    for district in sorted_districts:
        print(f"Микрорайон {district}:")
        if district not in building_by_district:
            print("Нет зданий, подлежащих реконструкции")
        else:
            sorted_years = sorted(building_by_district[district].keys())
            for year in sorted_years:
                print(f"Здания, построенные в {year} году:")
                for building in building_by_district[district][year]:
                    print(f"- {building}")

if __name__ == "__main__":
    # Вызов основной функции при запуске скрипта
    main()