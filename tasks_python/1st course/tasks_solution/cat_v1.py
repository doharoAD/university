class Cat:
    # атрибуты класса
    species = "кот"

    # атрибуты экземпляра: name (кличка), age (возраст)
    def __init__(self, name, age):
        self.name = name
        self.age = age

# создаём экземпляры класса
if __name__=="__main__":
    barsik = Cat("Барсик", 5)
    matroskin = Cat("Матроскин", 8)

# доступ к атрибутам класса
print("Барсик – {}".format(Cat.species))
print("Матроскин – {}".format(Cat.species))

# доступ к атрибутам экземпляров
print("Возраст: {} – {} лет".format(barsik.name, barsik.age))
print("Возраст: {} – {} лет".format(matroskin.name, matroskin.age))
