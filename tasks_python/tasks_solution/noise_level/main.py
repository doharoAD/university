import csv


class NoiseData:
    def __init__(self, enterprise_name, noise_level, day):
        """
        Конструктор класса NoiseData.

        Принимает на вход название предприятия, уровень шума и дату.
        Инициализирует атрибуты объекта.
        """
        self.enterprise_name = enterprise_name
        self.noise_level = int(noise_level)
        self.day = day


class NoiseDataProcessor:
    def __init__(self, file_name):
        """
        Конструктор класса NoiseDataProcessor.

        Принимает название CSV файла и сохраняет его как атрибут объекта.
        """
        self.file_name = file_name
        self.data = []

    def read_data(self):
        with open(self.file_name, newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            next(reader)
            for row in reader:
                self.data.append(NoiseData(row[0], row[2], row[1]))

    def get_max_noise(self):
        """
        Метод класса NoiseDataProcessor для поиска максимального уровня шума и даты его регистрации на предприятии.

        Возвращает список кортежей, отсортированных по убыванию максимального уровня шума.
        Каждый кортеж содержит название предприятия, максимальный уровень шума и дату его регистрации.
        """
        result = {}
        for row in self.data:
            if row.enterprise_name not in result or result[row.enterprise_name][0] < row.noise_level:
                result[row.enterprise_name] = (row.noise_level, row.day)

        sorted_result = sorted(result.items(), key=lambda x: x[1][0], reverse=True)

        return [(name, level, day) for name, (level, day) in sorted_result]


processor = NoiseDataProcessor("noise.csv")
processor.read_data()
max_noise = processor.get_max_noise()

for enterprise, noise_level, day in max_noise:
    print(f"Максимальный уровень шума - {noise_level} был зарегистрирован на предприятии '{enterprise}' в день {day}")